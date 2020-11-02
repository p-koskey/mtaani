from django.shortcuts import render, redirect, get_object_or_404
from django.http  import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm,UpdateUserForm,UpdateProfileForm,NeighbourHoodForm
from .models import Profile, User, Neighbourhood
# Create your views here.
@login_required(login_url='login')
def index(request):
     return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('welcome')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form}) 


@login_required(login_url='login')
def profile(request, username):
    return render(request, 'profile.html')


@login_required(login_url='login')
def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateProfileForm(instance=request.user.profile)
    
    return render(request, 'editprofile.html', {'user_form': user_form, 'prof_form': prof_form})

def create_mtaa(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            mtaa = form.save(commit=False)
            mtaa.admin = request.user.profile
            mtaa.save()

            return redirect('mitaa')
    else:
        form = NeighbourHoodForm()
    return render(request, 'newmtaa.html', {'form': form})

def mitaa(request):
    mitaa = Neighbourhood.objects.all()
    mitaa = mitaa[::-1]
   
    return render(request, 'mitaa.html', {"mitaa":mitaa})

def join_mtaa(request, id):
    neighbourhood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('mitaa')