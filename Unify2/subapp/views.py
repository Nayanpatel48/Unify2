from django.shortcuts import render, redirect
# here 'render' is used to render the HTML page along with context data
# here 'redirect' will redirect the user to the next page after successful operation.

from .forms import UserRegistrationForm
# A Django ModelForm imported from the forms.py file, which handles the user registration process.

from .models import UserProfile, Item

from django.contrib.auth import authenticate, login

from django.contrib import messages
# this will help to display a one time message (success/ error)

from django.contrib.auth.decorators import login_required
# a Django utility which ensures that only authenticated user will be able to access the specific
# view

from django.contrib.auth import logout
# a function provided by Django for log out the user

from .forms import ItemSearchForm, ItemUploadForm
# Forms defined earlier for searching and uploading items.

def register(request):
    # This defines the register view function, which takes an HttpRequest object (request) as 
    # its argument.
    if request.method == 'POST':
        # POST: Indicates that the form has been submitted, and the data is available in 
        # request.POST and request.FILES.

        form = UserRegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            # Checks if the submitted data meets the validation criteria defined in the 
            # UserRegistrationForm and the underlying model (UserProfile).

            form.save()
            # Saves the valid form data to the database.

            return redirect('success')
            # Redirects the user to a success page (e.g., a "Registration Successful" page) 
            # after the form is successfully saved.
    else:
        form = UserRegistrationForm()
        # An empty form is created for display when the user visits the registration page.

    return render(request, 'register.html', {'form': form})
    #Renders the register.html template with the form context variable.
    #If the form is empty (GET request) or contains invalid data (POST 
    # request), it is passed back to the template for display.

def success(request):
    return render(request, 'success.html')

def user_list(request):
    users = UserProfile.objects.all()
    # UserProfile.objects.all() is a Django ORM query that retrieves all 
    # records from the UserProfile table in the database.

    return render(request, 'user_list.html', {'users': users})
# this function retrieves all the UserProfile objects from the database & render 
# them in the HTML template

# below function based-view handles the user login functionality. It will check 
# the user credentials such as username and password and loggs in if they are valid.
def login_view(request):
    # Redirect already-logged-in users to the dashboard
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        # Process login form
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    # For GET requests, render the login form
    return render(request, 'login.html')

# This fuction based-view should check if the user is authenticated.
@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html', {'user' : request.user})
    # {'user' : request.user} is a context data passed to the tamplate

# This function-based view will handle the logout request by user
def logout_view(request):
    logout(request)
    # this function call performs the logout operation

    return redirect('login')
    # After the user has been logged out they are redirected to the login.html page

# View for searching items
@login_required
def search_items(request):
    form = ItemSearchForm(request.GET or None)
    results = None
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Item.objects.filter(name__icontains=query)
    return render(request, 'search_items.html', {'form': form, 'results': results})

# View for uploading items
@login_required
def upload_item(request):
    if request.method == 'POST':
        form = ItemUploadForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.uploaded_by = request.user  # Associate the item with the logged-in user
            item.save()
            return redirect('dashboard')  # Redirect to dashboard after upload
    else:
        form = ItemUploadForm()
    return render(request, 'upload_item.html', {'form': form})



