from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name = "home"),
    #path('login/', views.login_user , name = "login"),
    path('logout/', views.logout_user , name = "logout"),
    path('register/', views.register_user , name = "register"),
    path('record/<int:pk>/', views.customer_record , name = "record"),
    path('delete_record/<int:pk>/', views.delete_record , name = "delete_record"),
    path('add_record/', views.add_record , name = "add_record"),
    path('update_record/<int:pk>/', views.update_record , name = "update_record"),
    path('search/', views.search_records, name='search_records'),
    path('export/', views.export_records_csv, name='export_records_csv'),
    path('verify-email/<uuid:token>/', views.verify_email, name='verify_email'),
]