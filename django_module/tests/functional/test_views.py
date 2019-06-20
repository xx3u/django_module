from lxml import html

from django_module.models import Order, Product


def test_hello(db, client, data):
    client.login(username='john', password='testjohn')
    response = client.get('/')
    assert response.status_code == 200
    response = response.content.decode('utf-8')
    assert 'Hello, world!' in response
    assert 'john' in response
    response = html.fromstring(response)
    orders = Order.objects.filter(customer__user__username='john')
    assert len(response.cssselect('li')) == orders.count()


def test_order_view(db, client, data):
    response = client.get('/orders/1/')
    assert response.status_code == 200
    response = response.content.decode('utf-8')
    response = html.fromstring(response)
    items = response.cssselect('.list-group-item')
    assert items[0].text == 'TV 10'
    assert response.cssselect('#product') != []
    assert response.cssselect('#quantity') != []


def test_order_add_same(db, client, data):
    response = client.post('/orders/1/', {'product': 1, 'quantity': 10})
    assert response.status_code == 200
    response = response.content.decode('utf-8')
    response = html.fromstring(response)
    items = response.cssselect('.list-group-item')
    assert items[0].text == 'TV 20'


def test_order_add_new(db, client, data):
    notebook = Product.objects.create(name='Notebook', price=20)
    response = client.post(
        '/orders/1/',
        {'product': notebook.id, 'quantity': 30}
    )
    assert response.status_code == 200
    response = response.content.decode('utf-8')
    response = html.fromstring(response)
    items = response.cssselect('.list-group-item')
    assert items[0].text == 'TV 10'
    assert items[1].text == 'Notebook 30'


def test_order_add_empty_quantity(db, client, data):
    response = client.post('/orders/1/', {'product': 1, 'quantity': ''})
    assert response.status_code == 400
    response = response.content.decode('utf-8')
    assert response == 'Quantity must be a positive int'


def test_order_add_nonint_quantity(db, client, data):
    response = client.post('/orders/1/', {'product': 1, 'quantity': 'asd'})
    assert response.status_code == 400
    response = response.content.decode('utf-8')
    assert response == 'Quantity must be a positive int'


def test_order_add_zero_quantity(db, client, data):
    response = client.post('/orders/1/', {'product': 1, 'quantity': 0})
    assert response.status_code == 400
    response = response.content.decode('utf-8')
    assert response == 'Quantity must be a positive int'


def test_order_add_negative_quantity(db, client, data):
    response = client.post('/orders/1/', {'product': 1, 'quantity': -10})
    assert response.status_code == 400
    response = response.content.decode('utf-8')
    assert response == 'Quantity must be a positive int'


def test_bye(client):
    response = client.get('/bye/')
    assert response.status_code == 200
    assert response.content == b'Bye, world!'
