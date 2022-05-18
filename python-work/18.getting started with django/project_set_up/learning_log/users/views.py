from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """Registering a new user"""
    if request.method != 'POST':
        # Display a blank form
        form = UserCreationForm()
    else:
        # Process a complete form 
        form = UserCreationForm(date=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log in the new user by redirecting them to home
            login(request, new_user)
            return redirect('learn:index')
    
    # Display a blank or invalid form 
    context = {'form': form}
    return render(request, 'registration/register.html', context)