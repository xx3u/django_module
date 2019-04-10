from django_module.models import (
    Order, OrderItem, Product, Store, StoreItem)


def test_order_process(db):
    product = Product.objects.create(
        name='apple',
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
    order = Order.objects.create(
        location='Almaty',
    )
    OrderItem.objects.create(
        order=order,
        product=product,
        quantity=10
    )

    order.process()
    store_item.refresh_from_db()
    assert order.price == 100
    assert order.is_paid is True
    assert store_item.quantity == 90
