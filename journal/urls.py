from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes', views.recipes_list, name='recipes_list'),
    path('recipes/<int:id>', views.recipe_detail, name='recipe_detail'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register_view, name='register'),
]
