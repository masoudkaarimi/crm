from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('user/', views.user_view, name='user'),
    path('account/', views.account_view, name='account'),

    path('', views.home_view, name='home'),
    path('products/', views.products_view, name='products'),
    path('customer/<str:pk>/', views.customer_view, name='customer'),

    path('create_order/<str:pk>/', views.create_order_view, name='create_order'),
    path('update_order/<str:pk>/', views.update_order_view, name='update_order'),
    path('delete_order/<str:pk>/', views.delete_order_view, name='delete_order'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'), name="password_reset_complete"),
]
