from lxml import html

from django_module.models import Order


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


def test_bye(client):
    response = client.get('/bye/')
    assert response.status_code == 200
    assert response.content == b'Bye, world!'


def test_third(client):
    response = client.get('/third/')
    assert response.status_code == 200
    assert response.content == b'Third'
