from django.urls import path

from .views import IndexOrders, RegisterOrderView

app_name = 'orders'

urlpatterns = [
    path('register', RegisterOrderView.as_view(), name='order_register'),
    path('', IndexOrders.as_view(), name='list_register'),
]
