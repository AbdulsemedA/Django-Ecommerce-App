from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product

# Create your views here.
def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    # query_set = Product.objects.all()
    # queryset = Product.objects.filter(Q(inventory__lt=10) & Q(unit_price__lt=20))
    queryset = Product.objects.filter(inventory=F('unit_price'))



    # for product in query_set:
    #     print(product)
    # try:
    # except ObjectDoesNotExist:
    #     pass
    
    return render(request, 'hello.html', { 'name': 'mosh', 'products': list(queryset) })
