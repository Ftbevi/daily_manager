from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    TYPE_ORDES = [
        ('expense', 'expense'),
        ('revenue', 'expense'),
    ]
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    type_order = models.CharField(max_length=7, choices=TYPE_ORDES, default='EXPENSE')

    def __str__(self):
        return f'{self.user.username} - date{self.created}, {self.value}'
