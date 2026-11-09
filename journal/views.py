from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from .models import Trade
import json
import re


# Create your views here.

@login_required
def index(request):
    return render(request, 'index.html')

"""
    if request.method == 'GET':
        trades = Trade.objects.all().values()
        return JsonResponse(list(trades), safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        trade = Trade.objects.create(
            user=request.user,
            company=data["name"],
            trade_type=data["ingredient"],
            quantity=int(data["quantity"]),
            price=float(data["unit"])
        )
        return JsonResponse({'message': 'Trade added', 'id': trade.id}, status=201)
        """

@csrf_exempt
@login_required
def recipes_list(request):
    if request.method == "GET":
        trades = Trade.objects.filter(user=request.user).values(
            'id', 'company', 'trade_type', 'quantity', 'price'
        )
        return JsonResponse(list(trades), safe=False)

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            print("DATA RECEIVED:", data)

            quantity = int(data["quantity"]) if data["quantity"] else 0
            raw_price = data["price"]
            clean_price = re.sub(r"[^\d.]", "", raw_price)  # удаляем всё, кроме цифр и точки
            price = float(clean_price) if clean_price else 0.0

            trade = Trade.objects.create(
                user=request.user,
                company=data["company"] or "Unnamed",
                trade_type=data["trade_type"] or "BUY",
                quantity=quantity,
                price=price
            )

            return JsonResponse({'message': 'Trade added', 'id': trade.id}, status=201)

        except Exception as e:
            print("ERROR:", e)
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def recipe_detail(request, id):
    try:
        trade = Trade.objects.get(pk=id)
    except Trade.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)

    if request.method == 'PUT':
        data = json.loads(request.body)
        trade.company = data["company"]
        trade.trade_type = data["trade_type"]
        trade.price = float(data["price"]) if data["price"] else 0.0
        trade.quantity = int(data["quantity"])
        trade.save()
        return JsonResponse({'message': 'Trade updated'})

    elif request.method == 'DELETE':
        trade.delete()
        return JsonResponse({'message': 'Trade deleted'})

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            messages.error(request, "Passwords must match.")
            return redirect("register")

        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
        except:
            messages.error(request, "Username already taken.")
            return redirect("register")

        login(request, user)
        return redirect("index")
    return render(request, "register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("login")
