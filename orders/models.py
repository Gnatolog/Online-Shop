
from decimal import Decimal
from django.core.validators import MinValueValidator, \
                                   MaxValueValidator
from django.db import models
from django.conf import settings
from django.db import models    # импортируем доступ к базе данных
from shop.models import Product  # импортируем класс продуктов
from coupons.models import Coupon  #

class Order(models.Model):
    """
    Класс заказчика
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)    # поле для статуса оплаты или не оплаты заказа


    # Создаём подя для купона в заказе
    coupon = models.ForeignKey(Coupon,
                               related_name='orders',
                               null=True,
                               blank=True,
                               on_delete=models.SET_NULL)
    discount = models.IntegerField(default=0,
                                   validators=[MinValueValidator(0),
                                       MaxValueValidator(100)])

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        total_cost = self.get_total_cost_before_discount()
        return total_cost - self.get_discount()

    def get_total_cost_before_discount(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_discount(self):
        total_cost = self.get_total_cost_before_discount()
        if self.discount:
            return total_cost * (self.discount / Decimal(100))
        return Decimal(0)



class OrderItem(models.Model):
    """
    Класс заказа
    """
    order = models.ForeignKey(Order,              # внешний ключ для связи с Заказчиком
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,          # внешний ключ для связи с Заказчиком
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity