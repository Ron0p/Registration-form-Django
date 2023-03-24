from django.shortcuts import render, redirect
from .models import Registration


def home(request):
    return redirect('register')

def register(request):
    if request.method == 'POST':
        # Get the form data from the request
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        state = request.POST.get('state')
        country = request.POST.get('country')

        # Create a new Registration object with the form data
        registration = Registration(name=name, mobile=mobile, email=email,
                                     password=password, address=address,
                                     state=state, country=country)
        # Save the object to the database
        registration.save()

        # Redirect to a success page or do something else
        return render(request, 'registration/success.html')

    # Render the registration form for GET requests
    return render(request, 'registration/registration.html')
