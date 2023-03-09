from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Create a blank form.
        form = UserCreationForm()
    else:
        # Process the data.
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("learning_logs:index")
    
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
