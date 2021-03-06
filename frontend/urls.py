from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('dashboard/', views.dashboard, name="dashboard"),
    path('add-item/',views.itemsForm, name="items_form"),
    path('update/<str:pk>/', views.updateItem, name="update_item"),
    path('delete/<str:pk>/',views.deleteItem, name="delete_item"),

    path('grocery/', views.groceryLists, name="groceryLists"),
]
