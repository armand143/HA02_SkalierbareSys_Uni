from django.contrib import admin
from django.urls import path
from todoList import views

urlpatterns = [
    path('',views.home, name='home'),
    path('newTodo/', views.newTodo, name= 'newTodo'),
    path('impressum/', views.impressum, name = 'impressum'),
    path('list/',views.list,name='list'),
    path('delete/<int:id>', views.delete, name = 'delete'),
    path('edit/<int:id>', views.edit, name = 'edit'),
    path('submit',views.submit,name='submit'), 
    path('update/<int:id>',views.update,name='update')
]







   
 