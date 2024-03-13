from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'home_page/index.html')

#------------------------------------------------------------------------------------------
def about_us(request):
    return render(request, "info_pages/about_us.html")
def contact_us(request):
    return render(request, "info_pages/contact_us.html")
#------------------------------------------------------------------------------------------

def calorie_counter(request):
    return render(request, "feature_pages/calorie-counter.html")
#------------------------------------------------------------------------------------------

def profile(request):
    return render(request, "Login_pages/profile.html")
def login(request):
    return render(request, 'Login_pages/login.html')
def sign_up(request):
  return render(request, 'Login_pages/sign_up.html')
#------------------------------------------------------------------------------------------
def privacy_policy(request):
  return render(request, 'legal_pages/privacy_policy.html')
def terms_of_service(request):
  return render(request, 'legal_pages/terms_of_service.html')
#------------------------------------------------------------------------------------------


#buttons doesn't work yet


#request to make new account
def get_started(request):
    return render(request, 'home_page/index.html')