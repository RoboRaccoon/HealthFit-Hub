from django.shortcuts import render
from .forms import ProfileInfoForm, ProfileForm
from . import models
from django.shortcuts import redirect


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
        infoForm = ProfileInfoForm(request.POST)
        if infoForm.is_valid():
            age = infoForm.cleaned_data['age']
            gender = infoForm.cleaned_data['gender']
            weight = infoForm.cleaned_data['weight']
            height = infoForm.cleaned_data['height']
            print(age, gender, weight, height)
            profile_instance = infoForm.save()
            print('Profile saved:', profile_instance)
        else:
            print(infoForm.errors)
        return render(request, 'user-dashboard/dashboard.html', {'profile_form': infoForm})
    else:
        form = ProfileForm()
        return render(request, 'Login_pages/profile.html', {'profile_form': form})


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


def add_eaten_food(request, food_id):
    food = models.Food.objects.get(id=food_id)
    foodAdded = models.FoodsEatenList(id=1)
    foodAdded.save()
    foodAdded.foodEaten.add(food)
    foodAdded.save()
    print('This was the food added to list: ')
    print(foodAdded.id)
    print(foodAdded.foodEaten)
    # foodAdded.foodEaten.add(food)
    # foodAdded.save()
    print("Food item info: ")
    print(food.id)
    print(food.name)
    return redirect('calorie_counter')


# buttons doesn't work yet


# request to make new account
def get_started(request):
    return render(request, 'home_page/index.html')
