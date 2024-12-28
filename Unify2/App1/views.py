from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth.hashers import make_password
from .forms import UserRegistrationForm
from .models import User, UserProfile  # Import your custom User model
from django.contrib.auth import logout

def homepage(request):
    return render(request, 'homepage.html', {'user': request.user})

def layout2(request):
    return render(request, 'layout2.html')

def logout_view(request):
    logout(request)  # This will log out the user
    return redirect('homepage')  # Redirect the user to the homepage or wherever you want

# User Registration View
def register(request):
    # Check if the request is a POST request
    if request.method == 'POST':
    
        # Create a new form instance and populate it with the data from the request
        form = UserRegistrationForm(request.POST, request.FILES)

        # Validates the form data against the rules defined in UserRegistrationForm (like
        # required fields and field types).
        # If validation fails, it skips to the end and renders the form again with error
        # messages.
        if form.is_valid():

            user = form.save(commit=False)

            # Hashes the password entered by the user for security. Plaintext passwords 
            # should never be stored in the database.
            user.password = make_password(form.cleaned_data['password'])

            # Save the user to the database with the hash password
            user.save()

            profile_picture = form.cleaned_data.get('profile_picture')

            user_profile = UserProfile.objects.create(user=user, profile_picture=profile_picture)

            messages.success(request, 'Account created successfully.')

            return redirect('login')
    else:
        # Display the registration form
        form = UserRegistrationForm()

    # Render the registration form
    # In the register.html template, the 'form' variable is typically used to display 
    # the form fields dynamically.
    # Renders all the form fields as <p> elements.
    return render(request, 'register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            # Query your custom User model
            user = User.objects.get(email=email)

            # Check if the password is correct
            if user.check_password(password):
                # Log the user in
                login(request, user)
                return redirect('homepage')  # Redirect to homepage or dashboard
            else:
                messages.error(request, 'Invalid login credentials.')
        except User.DoesNotExist:
            messages.error(request, 'User does not exist.')

    return render(request, 'login.html')
