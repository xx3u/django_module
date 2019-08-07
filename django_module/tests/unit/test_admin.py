from django_module.models import (
    Product, Store, StoreItem, Customer, OrderItem, Order)

from django.contrib.auth.models import User


def test_str_product(db):
    product = Product.objects.create(name='TV', price=0)
    assert str(product) == 'TV'


def test_str_store(db):
    store = Store.objects.create(location='Almaty')
    assert str(store) == 'Almaty'


def test_str_storeitem(db):
    product = Product.objects.create(
        name='TV', price=0)
    storeitem = StoreItem.objects.create(
        product=product, quantity=0,
        store=Store.objects.create(location=''))
    assert str(storeitem) == 'TV'


def test_str_customer(db):
    user = User.objects.create_user(username='Tanya', password='')
    customer = Customer.objects.create(name='Tanya', user=user)
    assert str(customer) == 'Tanya'


def test_str_orderitem(db):
    product = Product.objects.create(name='TV', price=0)
    user = User.objects.create_user(username='Tanya', password='')
    customer = Customer.objects.create(name='Tanya', user=user)
    order = Order.objects.create(
        price=0, is_paid=True, location='', customer=customer)
    orderitem = OrderItem.objects.create(
        order=order, product=product, quantity=0)
    assert str(orderitem) == 'TV'
