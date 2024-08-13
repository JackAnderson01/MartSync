from django.urls import path
from .views import (
    ProductCreateView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
    ProductListView,
    
)

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),  # Retrieve all products
    path('products/create/', ProductCreateView.as_view(), name='product-create'),  # Create a new product
    path('products/<uuid:pk>/', ProductDetailView.as_view(), name='product-detail'),  # Retrieve a single product
    path('products/<uuid:pk>/update/', ProductUpdateView.as_view(), name='product-update'),  # Update a product
    path('products/<uuid:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),  # Delete a product
]
