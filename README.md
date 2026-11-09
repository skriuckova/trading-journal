# My Trading Journal

A full-stack personal finance web application for recording and managing stock trades.

My Trading Journal allows registered users to maintain their own personal trading history, including transaction type, quantity, and price. Each user has access only to their own trade data.

## Demo

🎥 [Watch the project demo on YouTube](https://youtu.be/Yj2aKa22pIg)

## Features

- User registration and authentication
- User-specific trading data
- Add new stock transactions
- View saved trades
- Edit existing transactions
- Delete transactions
- Persistent data storage
- Dynamic JavaScript interactions
- Responsive web interface

## Technologies

- Python
- Django
- JavaScript
- SQLite
- HTML
- CSS

## Application Interface

![My Trading Journal Dashboard](trading-journal-dashboard.png)

The main dashboard displays the user's recorded stock transactions, including:

- Stock name
- Buy/Sell transaction type
- Quantity
- Price
- Edit and delete controls

## Run Locally

Clone the repository:

```bash
git clone https://github.com/skriuckova/trading-journal.git
cd trading-journal
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
DJANGO_SECRET_KEY=your-secret-key-here
```

Run database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## What I Learned

This project helped me strengthen my understanding of:

- Full-stack web development with Django
- Database models and persistent data storage
- User authentication
- CRUD operations
- Connecting frontend JavaScript with backend functionality
- Building user-specific application logic
- Structuring a complete web application

## Project Background

My Trading Journal was developed as my final project for Harvard's CS50's Web Programming with Python and JavaScript course.

This repository serves as a public portfolio showcase of the project. The original course submission and source-code repository remain private.

## Author

**Sonia Kriučkova**

Computer Science & Engineering student interested in software development, data analysis, AI/automation, and full-stack development.
