from django.shortcuts import render

# Create your views here.
def vpa(request):
    return render(request, 'home/index.html')

