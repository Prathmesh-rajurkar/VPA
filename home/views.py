from django.shortcuts import render

# Create your views here.
def todo(request):
    return render(request, 'index.html')