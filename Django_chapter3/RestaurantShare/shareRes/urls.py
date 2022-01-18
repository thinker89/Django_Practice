from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurantDetail/delete', views.deleteRestaurant, name='resDelete'),
    path('restaurantDetail/<str:res_id>', views.restaurantDetail, name='resDetailPage'),
    path('restaurantDetail/updatePage/update', views.updateRestaurant, name='resUpdatePage'),
    path('restaurantDetail/updatePage/<str:res_id>', views.restaurantUpdate, name='resUpdatePage'),
    path('restaurantCreate/', views.restaurantCreate, name='resCreatePage'),
    path('restaurantCreate/create', views.createRestaurant, name='resCreate'),
    path('categoryCreate/', views.categoryCreate, name='cateCreatePage'),
    path('categoryCreate/create', views.createCategory, name='cateCreate'),
    path('categoryCreate/delete', views.deleteCategory, name='cateDelete'),
]
