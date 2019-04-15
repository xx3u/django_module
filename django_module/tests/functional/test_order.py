import pytest


def test_order_process_is_ok(db, data):
    product, store, store_item, customer, order, order_item, payment = data
    order.process()
    store_item.refresh_from_db()
    assert order.price == 100
    assert order.is_paid is True
    assert store_item.quantity == 90
    assert order.customer.name is 'John'
    assert order.customer.user.username == 'john'


def test_order_process_quantity_if_order_more_than_store(db, data):
    product, store, store_item, customer, order, order_item, payment = data
    order_item.quantity = 200
    order_item.save()
    with pytest.raises(Exception) as e:
        order.process()
    assert str(e.value) == 'Not enough stock'


def test_order_process_payment_if_amount_less_than_order(db, data):
    product, store, store_item, customer, order, order_item, payment = data
    payment.amount = 10
    payment.save()
    with pytest.raises(Exception) as e:
        order.process()
    assert str(e.value) == 'Not enough money'
