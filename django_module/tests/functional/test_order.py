import pytest

from django_module.models import Payment, Order, OrderItem

from django_module.exceptions import StoreException, PaymentException


def test_order_process_is_ok(db, data):
    (product, store, store_item,
        customer, order, order_item, payment, user) = data
    assert order.price == 100
    order.process()
    store_item.refresh_from_db()
    assert order.is_paid is True
    assert store_item.quantity == 90
    assert order.customer.name is 'John'
    assert order.customer.user.username == 'john'


def test_order_item_price_signal_ok(db, data):
    (product, store, store_item,
        customer, order, order_item, payment, user) = data
    assert order.price == 100
    OrderItem.objects.create(order=order, product=product, quantity=20)
    assert order.items.count() == 1
    order.items.first().quantity == 30
    assert order.price == 300


def test_order_item_paid_signal_ok(db, data):
    (product, store, store_item,
        customer, order, order_item, payment, user) = data
    assert order.is_paid is True


def test_order_process_quantity_if_order_more_than_store(db, data):
    (product, store, store_item,
        customer, order, order_item, payment, user) = data
    order_item.quantity = 200
    order_item.save()
    with pytest.raises(StoreException) as e:
        order.process()
    assert str(e.value) == 'Not enough stock'


def test_order_process_payment_if_amount_less_than_order(db, data):
    (product, store, store_item,
        customer, order, order_item, payment, user) = data
    payment.amount = 10
    payment.save()
    with pytest.raises(PaymentException) as e:
        order.process()
    assert str(e.value) == 'Not enough money'


def test_order_process_for_multiple_payments(db, data):
    (product, store, store_item,
        customer, order, order_item, payment, user) = data
    payment.amount = 40
    payment.save()
    Payment.objects.create(
        order=order,
        amount=60,
        is_confirmed=True
    )
    order.process()
    store_item.refresh_from_db()
    assert order.price == 100
    assert order.is_paid is True
    assert store_item.quantity == 90


def test_order_process_fail_if_payment_is_not_confirmed(db, data):
    (product, store, store_item,
        customer, order, order_item, payment, user) = data
    payment.is_confirmed = False
    payment.save()
    with pytest.raises(PaymentException) as e:
        order.process()
    assert str(e.value) == 'Not enough money'


def test_order_process_fail_if_location_is_not_available(db, data):
    (product, store, store_item,
        customer, order, order_item, payment, user) = data
    order = Order.objects.create(
        price=10,
        is_paid=True,
        location='Astana',
        customer=customer
    )
    order.save()
    with pytest.raises(StoreException) as e:
        order.process()
    assert str(e.value) == 'Location is not available'
