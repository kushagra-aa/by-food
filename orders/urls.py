
from django.urls import path
from . import views

app_name='byfood'
urlpatterns = [
    path('', views.index,name='home'),
    path('food/', views.food,name='food'),
    path('login/', views.loginPage,name='login'),
    path('register/', views.register,name='register'),
    path('<int:item_id>', views.orderPage, name='order'),
    # handle routes
    path('handleLogin/', views.handleLogin, name='handleLogin'),
    path('handleRegister/', views.handleRegister, name='handleRegister'),
    path('handleOrder/', views.handleOrder, name='handleOrder'),
    path('logout/', views.handleLogout, name='logout'),
]
