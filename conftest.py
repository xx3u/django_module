import pytest

from django_module.models import (
    Order, OrderItem, Product, Store, StoreItem, Customer, Payment)

from django.contrib.auth.models import User


@pytest.fixture
def data():
    product = Product.objects.create(
        name='TV',
        price=10
    )
    store = Store.objects.create(
        location='Almaty'
    )
    store_item = StoreItem.objects.create(
        store=store,
        product=product,
        quantity=100
    )
    user = User.objects.create_user(
        username='john',
        password='testjohn'
    )
    customer = Customer.objects.create(
        name='John',
        user=user
    )
    order = Order.objects.create(
        price=10,
        is_paid=True,
        location='Almaty',
        customer=customer
    )
    order_item = OrderItem.objects.create(
        order=order,
        product=product,
        quantity=10
    )
    payment = Payment.objects.create(
        order=order,
        amount=1000,
        is_confirmed=True
    )
    return (
        product, store, store_item, customer, order,
        order_item, payment, user
    )
