from django.shortcuts import render
from django.views import View

from .forms import OrderPostForm
from .models import Order


class RegisterOrderView(View):
    form_class = OrderPostForm
    template_name = 'managers/order/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial={})
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.save()
        return render(request, self.template_name, {'data': data})
