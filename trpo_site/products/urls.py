from django.urls import path
from .views import ProductWorker

urlpatterns = [
    path('', ProductWorker.product_list, name='product_list'),
    path('add/', ProductWorker.product_add, name='product_add'),
    path('edit/<int:pk>/', ProductWorker.product_edit, name='product_edit'),
    path('delete/<int:pk>/', ProductWorker.product_delete, name='product_delete'),
]