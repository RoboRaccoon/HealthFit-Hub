from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'home_page/index.html')

#buttons doesn't work yet
def login(request):
    return (render, 'home_page/index.html')

#request to make new account
def get_started(request):
    return render(request, 'home_page/index.html')