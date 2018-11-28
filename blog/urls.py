from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert/', views.insert, name='insert'),
    path('list/', views.post_list, name='post_list'),
    path('update/', views.update, name='update'),
    path('update/<int:pk>', views.update_specific, name='update specific'),
    path('delete/', views.delete, name ='delete'),
    path('delete/<int:pk>', views.delete, name='delete int'),
    path('search/', views.search, name='search'),
    path('search/<str:name>/', views.search_specific),
]