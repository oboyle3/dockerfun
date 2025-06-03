from django.shortcuts import render

# Create your views here.
def custom_page(request):
    return render(request, 'enigmaapp/custom_page.html')