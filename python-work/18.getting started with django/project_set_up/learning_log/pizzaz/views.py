from django.shortcuts import render
from .models import Topping, Pizza

# Create your views here.
def index(request):
    """Home page of pizzaz"""
    pizzaz = Pizza.objects.all().order_by('date_added')
    context = {'pizzaz': pizzaz}
    return render(request, 'index.html', context)

def toppings(request, pizzaz_id):
    """Pizza page"""
    pizzaz = Pizza.objects.get(id=pizzaz_id)
    toppings = pizzaz.topping_set.order_by('date_added')
    context = {'pizzaz': pizzaz, 'toppings': toppings}
    return render(request, 'toppings.html', context)
