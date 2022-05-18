from django.shortcuts import render

# Create your views here.
def index(request):
    """Home page view"""
    context = {}
    return render(request, "index.html", context)