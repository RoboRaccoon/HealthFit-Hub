from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileForm
from .models import Profile

# Create your views here.
def main(request):
    return render(request, 'home_page/index.html')




def about_us(request):
    return render(request, "info-pages/about-us.html")
def contact_us(request):
    return render(request, "info-pages/contact_us.html")
def help(request):
    return render(request, "info-pages/help.html")




def calorie_counter(request):
    return render(request, "feature_pages/calorie-counter.html")




def profile(request):
    form = ProfileForm()
    return render(request, 'Login_pages/profile.html', {'profile_form': form})

def update_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=pk)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'update_profile.html', {'form': form})



def login(request):
    return render(request, 'Login_pages/login.html')
def sign_up(request):
  return render(request, 'Login_pages/sign_up.html')
def sign_up_process(request):
  return render(request, 'Login_pages/sign_up_process.html')
def sign_up_done(request):
  return render(request, 'Login_pages/sign_up_done.html')

def privacy_policy(request):
  return render(request, 'legal_pages/privacy_policy.html')
def terms_of_service(request):
  return render(request, 'legal_pages/terms_of_service.html')

def dashboard(request):
    return render(request, "user-dashboard/dashboard.html")

def premium(request):
    return render(request, "user-dashboard/premium.html")


#buttons doesn't work yet


#request to make new account
def get_started(request):
    return render(request, 'home_page/index.html')







