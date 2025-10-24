from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product, OrderItem

# Create your views here.
def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    # query_set1 = Product.objects.all()
    
    # queryset1 = Product.objects.filter(Q(inventory__lt=10) & Q(unit_price__lt=20))
    # queryset2 = Product.objects.filter(inventory=F('unit_price'))
    # queryset3 = Product.objects.order_by('unit_price', '-title')
    # prod1 = Product.objects.order_by('unit_price')[0]
    # prod2 = Product.objects.earliest('unit_price')
    # query3 = Product.objects.values('id', 'title', 'collection__title')
    # query4 = Product.objects.values_list('id', 'title', 'collection__title')

# exercise, get all products that are ordered sorted by their titles

    # query_set1 = Product.objects.filter(id__in = OrderItem.
    # objects.values('product_id').distinct()).order_by('title')

    # query_set1 = Product.objects.only('id', 'title')
    # query_set1 = Product.objects.defer('description')


    # for product in query_set:
    #     print(product)
    # try:
    # except ObjectDoesNotExist:
    #     pass

    query_set1 = Product.objects.select_related('collection').all()
    
    return render(request, 'hello.html', { 'name': 'mosh', 'products': list(query_set1) })
