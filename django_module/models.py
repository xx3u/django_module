from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )


class Store(models.Model):
    location = models.CharField(max_length=100, blank=True)


class StoreItem(models.Model):
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='store_items'
    )
    quantity = models.IntegerField()
    location = models.CharField(max_length=100, blank=True)


class Customer(models.Model):
    name = models.CharField(max_length=100)


class Cart(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='carts'
    )


class Order(models.Model):
    location = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    is_paid = models.BooleanField(default=False)

    def process(self):
        store = Store.objects.get(location=self.location)
        for item in self.items.all():
            store_item = StoreItem.objects.get(
                store=store,
                product=item.product,
            )
            store_item.quantity -= item.quantity
            store_item.save()

        self.price = sum(
            (item.product.price * item.quantity for item in self.items.all())
        )
        self.is_paid = True
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items')
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='order_items'
    )
    quantity = models.IntegerField()
