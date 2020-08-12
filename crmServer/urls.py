from django.urls import path

from . import views

urlpatterns = {
    path('', views.index, name='index'),
    path('editCase', views.edit_case, name='editCase'),
    path('createTask', views.create_task, name='createTask'),
    path('deleteTask', views.delete_task, name='deleteTask'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
}