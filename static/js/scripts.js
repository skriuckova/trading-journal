function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

document.addEventListener('DOMContentLoaded', function () {
    loadRecipes();

    document.getElementById('addRecipeBtn').addEventListener('click', function () {
        const recipeList = document.getElementById('recipeList');
        const tr = document.createElement('tr');

        tr.innerHTML = `
            <td contenteditable="true" data-label="Company">Stock</td>
            <td contenteditable="true" data-label="Type">Buy/Sell</td>
            <td contenteditable="true" data-label="Quantity">0</td>
            <td contenteditable="true" data-label="Price">USD</td>
            <td data-label="Actions">
                <button class="save-btn">Save</button>
                <button class="delete-btn">Delete</button>
            </td>
        `;

        recipeList.appendChild(tr);

        tr.querySelector('.save-btn').addEventListener('click', function () {
            saveNewRecipe(tr);
        });

        tr.querySelector('.delete-btn').addEventListener('click', function () {
            tr.remove();
        });
    });
});

function loadRecipes() {
    fetch('/recipes')
        .then(response => response.json())
        .then(data => {
            const recipeList = document.getElementById('recipeList');
            recipeList.innerHTML = '';

            data.forEach(recipe => {
                const tr = document.createElement('tr');
                tr.dataset.id = recipe.id;

                tr.innerHTML = `
                    <td contenteditable="false" data-label="Company">${recipe.company}</td>
                    <td contenteditable="false" data-label="Type">${recipe.trade_type}</td>
                    <td contenteditable="false" data-label="Quantity">${recipe.quantity}</td>
                    <td contenteditable="false" data-label="Price">${recipe.price}</td>
                    <td data-label="Actions">
                        <button class="edit-btn">Edit</button>
                        <button class="delete-btn">Delete</button>
                        <button class="save-btn" style="display:none;">Save</button>
                    </td>
                `;

                recipeList.appendChild(tr);

                tr.querySelector('.delete-btn').addEventListener('click', () => {
                    deleteRecipe(tr.dataset.id);
                });

                tr.querySelector('.edit-btn').addEventListener('click', () => {
                    editRecipe(tr);
                });

                tr.querySelector('.save-btn').addEventListener('click', () => {
                    saveRecipe(tr.dataset.id, tr);
                });
            });
        });
}

function saveNewRecipe(row) {
    const newRecipe = {
        company: row.cells[0].textContent,
        trade_type: row.cells[1].textContent,
        quantity: row.cells[2].textContent,
        price: row.cells[3].textContent
    };

    fetch('/recipes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(newRecipe)
    })
    .then(response => response.json())
    .then(data => {
        console.log("Saved:", data);
        row.remove();
        loadRecipes();
    })
    .catch(error => {
        console.error("Save failed:", error);
    });
}

function deleteRecipe(id) {
    fetch(`/recipes/${id}`, {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': csrftoken
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log("Deleted:", data);
        loadRecipes();
    });
}

function editRecipe(row) {
    row.querySelectorAll('td').forEach((cell, index) => {
        if (index < 4) cell.contentEditable = "true";
    });
    row.querySelector('.edit-btn').style.display = "none";
    row.querySelector('.save-btn').style.display = "inline";
}

function saveRecipe(id, row) {
    const updatedRecipe = {
        company: row.cells[0].textContent,
        trade_type: row.cells[1].textContent,
        quantity: row.cells[2].textContent,
        price: row.cells[3].textContent
    };

    fetch(`/recipes/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(updatedRecipe)
    })
    .then(response => response.json())
    .then(data => {
        console.log("Updated:", data);
        loadRecipes();
    });
}
