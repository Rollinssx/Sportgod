from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from datetime import timedelta
from .models import Product, Category


# Create your views here.


from datetime import timedelta
from django.utils.timezone import now

def home(request):
    last_30_days = now() - timedelta(days=30)
    products = Product.objects.all()
    product_count = products.count()

    # Get New Arrivals
    new_arrivals = Product.objects.filter(created_at__gte=last_30_days).order_by('-created_at')

    # Get Best Sellers (top 5 most sold)
    best_sellers = Product.objects.order_by('-sold_count')[:3]

    basketball_category = Category.objects.get(name='Basketball')  # Get the category object
    basketball_products = Product.objects.filter(category=basketball_category)[:7]

    skiing_category = Category.objects.get(name='Skiing')
    skiing_products = Product.objects.filter(category=skiing_category)[:7]

    # Remove products that are in both lists
    new_arrivals = new_arrivals.exclude(id__in=best_sellers.values_list('id', flat=True))

    context = {'new_arrivals': new_arrivals, 'best_sellers': best_sellers, 'products': products,
               'product_count': product_count, 'basketball_products': basketball_products,
               'skiing_products': skiing_products
               }
    return render(request, 'base/home.html', context)


def product_view(request, pk):
    product = get_object_or_404(Product, id=pk)

    basketball_category = Category.objects.get(name='Basketball')  # Get the category object
    basketball_products = Product.objects.filter(category=basketball_category)[:7]

    skiing_category = Category.objects.get(name='Skiing')
    skiing_products = Product.objects.filter(category=skiing_category)[:7]

    context = {'product': product, 'basketball_products': basketball_products, 'skiing_products': skiing_products}
    return render(request, 'base/single.html', context)





