from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from .forms import OrderPostForm
from .models import Order


class IndexOrders(ListView):
    model = Order
    template_name = 'managers/order/list.html'


class RegisterOrderView(View):
    form_class = OrderPostForm
    template_name = 'managers/order/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial={})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/orders')
        return render(request, self.template_name, {'form': form})
