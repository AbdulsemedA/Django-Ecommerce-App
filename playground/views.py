from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.db.models import Q, F
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Customer, Product, OrderItem, Order

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

# exercise 1
# get all products that are ordered sorted by their titles
    # query_set1 = Product.objects.filter(id__in = OrderItem.
    # objects.values('product_id').distinct()).order_by('title')

    # query_set1 = Product.objects.only('id', 'title')
    # query_set1 = Product.objects.defer('description')


    # for product in query_set:
    #     print(product)
    # try:
    # except ObjectDoesNotExist:
    #     pass

    # query_set1 = Product.objects.select_related('collection').all()
    # query_set1 = Product.objects.prefetch_related('promotions').all()
    # query_set1 = Product.objects.prefetch_related('promotions').select_related('collection').all()

# exercise 2
# get the last 5 orders with their customer and items ( incl product )

    # query_set1 = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    # res = Product.objects.aggregate(count=Count('id'), min_price=Min('unit_price'))
    
    # query_set1 = Customer.objects.annotate(order_count=Count('order'))

    # query_set1 = Product.objects.annotate(discounted_price=F('unit_price') * 0.8)

    return render(request, 'hello.html', { 'name': 'mosh', 'customer': list(query_set1) })
    # return render(request, 'hello.html', { 'name': 'mosh', 'res': res })
