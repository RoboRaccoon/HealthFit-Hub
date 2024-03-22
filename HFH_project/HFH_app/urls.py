from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),

    path('about_us/', views.about_us, name="about_us", ),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('help/', views.help, name="help"),

    path('calorie_counter/', views.calorie_counter, name="calorie_counter"),
    path('add_eaten_food/<int:food_id>/', views.add_eaten_food, name='add_eaten_food'),
    path('delete_eaten_food/<int:food_id>/', views.delete_eaten_food, name='delete_eaten_food'),

    path('profile/', views.profile, name="profile"),
    path('login/', views.login, name="login"),
    path('sign_up/', views.sign_up, name="sign_up"),

    path('privacy_policy/', views.privacy_policy, name="privacy_policy"),
    path('terms_of_service/', views.terms_of_service, name="terms_of_service"),

]