from django.shortcuts import render, redirect
#import database_manager
from utils import database_manager

# Create your views here.
def home(request) -> render:

	items = database_manager.load_database()
	return render(request, "home.html", {"shop_items": items})

def about(request) -> render:
	return render(request, "about.html")

def contact(request) -> render:
	return render(request, 'contact.html')
