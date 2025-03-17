# members/views.py
from django.shortcuts import render, redirect
from .forms import LoginForm

# Home view
def home_view(request):
    return render(request, 'members/hello_world.html')  # This renders the 'hello_world.html' template

# Login view (without Django authentication)
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']

            # Check if credentials are valid (this is just a simple example)
            if name == 'admin' and password == 'password123':  # Replace with your own condition
                request.session['logged_in'] = True  # Mark user as logged in in the session
                return redirect('home')  # Redirect to the home page after successful login
            else:
                form.add_error(None, 'Invalid username or password')

    else:
        form = LoginForm()  # Create an empty form for GET request

    return render(request, 'members/login.html', {'form': form})
