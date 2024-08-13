from django.urls import path
from .views import (
    StoreCreateView,
    StoreDetailView,
    StoreUpdateView,
    StoreDeleteView,
    StoreListView,
    StoreProductsListView
)

urlpatterns = [
    path('stores/', StoreListView.as_view(), name='store-list'),  # Retrieve all stores
    path('stores/create/', StoreCreateView.as_view(), name='store-create'),  # Create a new store
    path('stores/<uuid:pk>/', StoreDetailView.as_view(), name='store-detail'),  # Retrieve a single store
    path('stores/<uuid:pk>/update/', StoreUpdateView.as_view(), name='store-update'),  # Update a store
    path('stores/<uuid:pk>/delete/', StoreDeleteView.as_view(), name='store-delete'),  # Delete a store
    path('stores/<uuid:store_id>/products/', StoreProductsListView.as_view(), name='store-products-list'),

]
