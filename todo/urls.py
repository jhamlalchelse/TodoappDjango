from django.urls import path
from todo import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add-todo/', views.add_todo, name='addtodo'),
    path('edit/<str:pk>', views.edit_item, name='edittodo'),
    path('delete/<str:id>', views.delete_item, name='deletetodo'),
    path('uncross/<str:pk>', views.uncross, name='uncross'),
    path('crossoff/<str:pk>', views.crossoff, name='crossoff'),
]
