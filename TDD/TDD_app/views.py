from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    context = {
    	"name": "Noelle",
    	"favorite_color": "turquoise",
    	"pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, 'index.html', context)

