from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'tim_app/login.html')

def ranking(request):
    return render(request, 'tim_app/ranking.html')