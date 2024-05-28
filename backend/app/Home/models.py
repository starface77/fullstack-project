from django.shortcuts import render

# Create your models here.
def Home(request):
    return render(request, 'Home.html')
