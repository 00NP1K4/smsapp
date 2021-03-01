from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.loginpage, name='login'),
    path('text_message/', views.text_message, name='text_message'),
    path('add_contact/', views.add_contact, name = 'add_contact'),
    path('contacts/', views.contacts, name = 'contacts'),
    path('add-to-send/', views.add, name = 'add'),
    path('delete/<str:pk>/', views.delete_contact, name = 'delete_contact'),
    path('update/<str:pk>/', views.update_contact, name = 'update'),
    path('from_contact/<str:pk>/', views.from_contact, name = 'from_contact'),
    path('delete_send/<str:pk>/', views.delete_send, name = 'delete_send'),
    path('logout/', views.logoutuser, name='logout'),
    path('confirm/', views.confirm, name = 'confirm'),
]