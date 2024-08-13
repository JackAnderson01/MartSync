from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Store
from .serializers import StoreSerializer
from products.serializers import ProductSerializer
from products.models import  Product
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound


class StoreCreateView(generics.CreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        # Add any additional logic here before saving the store
        serializer.save(user=self.request.user)
        # Example: Send notification to the user after store creation
        # send_notification_to_user(self.request.user, "Store created successfully!")


class StoreUpdateView(generics.UpdateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]


    def perform_update(self, serializer):
        # Add any additional logic here before updating the store
        serializer.save()
        # Example: Log the update
        # log_store_update(serializer.instance)


class StoreDeleteView(generics.DestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]


    def perform_destroy(self, instance):
        # Add any additional logic here before deleting the store
        # Example: Archive store data
        # archive_store_data(instance)
        instance.delete()


class StoreDetailView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]




class StoreListView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]



class StoreProductsListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        store_id = self.kwargs['store_id']
        queryset = Product.objects.filter(store__id=store_id)
        
        if not queryset.exists():
            raise NotFound(detail=f"No products found for store ID: {store_id}")

        return queryset