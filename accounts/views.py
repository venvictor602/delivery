from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login, logout
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from . import forms
from .forms import MyUserCreationForm, ProfileEditForm
from django.conf import settings

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    subject = request.POST['subject']
    message = request.POST['message']
    contact = Contact(name=name, email=email, subject=subject,phone=phone, message=message)

    contact.save()
    messages.success(request, 'Your message was sent successfully, We will get back to you soon')
  return render(request,'contact.html')





def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/account_settings/')
    else:
        form = MyUserCreationForm()
        if request.method == 'POST':
            form = MyUserCreationForm(request.POST)
            if form.is_valid():
                user=form.save()
                
                # Check if the profile already exists
                if not hasattr(user, 'profile'):
                    # Create the user profile
                    profile = Profile.objects.create(user=user)
                
                username = form.cleaned_data.get('username')
                messages.success(request, 'Account Created Successfully')
                return redirect('/login/')
            else:
                messages.error(request, 'Error creating account')
        
        context={'form':form}
    return render(request,'register.html',context)





from django.contrib import messages

@login_required(login_url='login')
def edit(request):
    user_profile = request.user.profile  # Assuming you have a one-to-one relationship with the user profile

    if request.method == 'POST':
        profile_form = ProfileEditForm(instance=user_profile, data=request.POST, files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('dashboard')  # Redirect to the dashboard after editing profile
    else:
        profile_form = ProfileEditForm(instance=user_profile)

    # Check if both front_picture and back_picture are filled
    if user_profile.front_picture and user_profile.back_picture:
        return redirect('dashboard')  # Redirect to the dashboard if the profile is filled

    context = {'profile_form': profile_form}
    return render(request, 'dashboard/account_settings.html', context)








# working
# @login_required(login_url='login')
# def edit(request):
#     if request.method == 'POST':
#         profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
#         if profile_form.is_valid():
#             profile_form.save()
#             messages.success(request, 'Profile updated successfully')
#             return redirect('dashboard')  # Redirect to the dashboard after editing profile
#         else:
#             messages.error(request, 'Error updating your profile')
#     else:
#         profile_form = ProfileEditForm(instance=request.user.profile)

#     context = {'profile_form': profile_form}
#     return render(request, 'dashboard/account_settings.html', context)

# # Your other views go here



# @login_required(login_url='login')
# def edit(request):
    if request.method == 'POST':
        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        profile_form = ProfileEditForm(instance=request.user.profile)
        return redirect('dashboard')
        
    context={'profile_form': profile_form}

    return render(request,'dashboard/account_settings.html',context)


# def loginPage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password =request.POST.get('password')

#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'Login Successful')
#             return redirect('/account_settings/')
                      
#         else:
#             messages.info(request, 'Username OR password is incorrect')
#     return render(request,'login.html')




def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('account_settings')  # Redirect to the edit view after successful login
        else:
            messages.info(request, 'Username OR password is incorrect')
    
    return render(request, 'login.html')





def logoutUser(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
  if request.method == 'POST':
    sender_name = request.POST['sender_name']
    sender_origin = request.POST['sender_origin']
    froms = request.POST['froms']
    tos = request.POST['tos']
    item_description = request.POST['item_description']
    reciver_name = request.POST['reciver_name']
    reciver_email = request.POST['reciver_email']
    reciver_address = request.POST['reciver_address']
    reciver_phone = request.POST['reciver_phone']
    Weight_And_Dimension = request.POST['Weight_And_Dimension']

    contact = Quote(sender_name=sender_name, sender_origin=sender_origin, tos=tos,froms=froms, item_description=item_description,reciver_name=reciver_name,reciver_email=reciver_email,reciver_address=reciver_address,reciver_phone=reciver_phone,Weight_And_Dimension=Weight_And_Dimension)

    contact.save()
    messages.success(request, 'Your message was sent successfully, We will get back to you soon')
  return render(request,'dashboard/dashboard.html')

def track(request):
  return render(request,'dashboard/tracking.html')


def search(request):
    pick = Tracking.objects.order_by('-date_created')
    pickups = []

    if 'trackingid' in request.GET:
        trackingid = request.GET['trackingid']
        if trackingid:
            pickups = Tracking.objects.filter(trackingid__iexact=trackingid)

    # Access the related Timeline object for each Tracking object
    for pickup in pickups:
        related_timeline = pickup.timeline  # Access the related Timeline object
        # Now you can access the properties of the related Timeline object, e.g., related_timeline.Date

    context = {'pickups': pickups, 'pick': pick}
    return render(request, 'dashboard/search.html', context)
