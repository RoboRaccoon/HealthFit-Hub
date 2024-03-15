from django.shortcuts import render
from .forms import ProfileForm

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
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            return render(request,'Login_pages/profile.html',{'form':form})
    else:
        form = ProfileForm()
    return render(request, 'Login_pages/profile.html', {'profile_form': form})

def login(request):
    return render(request, 'Login_pages/login.html')
def sign_up(request):
  return render(request, 'Login_pages/sign_up.html')



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







