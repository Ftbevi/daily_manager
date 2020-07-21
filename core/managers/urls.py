from django.urls import path

from .views import RegisterOrderView

app_name = 'orders'

urlpatterns = [
    path('register', RegisterOrderView.as_view(), name='order_register'),
]
