from django.shortcuts import render, redirect, get_object_or_404
#import database_manager
# from utils import database_manager [DEPRECATED: DO NOT USE!!!!]
from .models import Add_Item, Cart, CartItem
from django.contrib.auth.decorators import login_required
from .forms import UserCreation
from django.contrib.auth import login
from django.contrib.auth.models import User



# Create your views here.
def home(request) -> render:

	items = Add_Item.objects.all()
	return render(request, "home.html", {"items": items})

@login_required
def profile(request) -> render:
	return render(request, 'registration/profile.html')

@login_required
def remove_from_cart(request, item_id) -> redirect:
	cart = request.user.cart
	cart_item = get_object_or_404(CartItem, cart=cart, item__id=item_id)
	cart_item.delete()
	return redirect('cart_details')

@login_required
def add_to_cart(request, item_id) -> redirect:
	item = get_object_or_404(Add_Item, id=item_id)
	cart, _ = Cart.objects.get_or_create(user=request.user)
	cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
	if not created:
		cart_item.quantity += 1
		cart_item.save()
	return redirect('cart_details')

@login_required
def cart_details(request) -> render:
	cart, _ = Cart.objects.get_or_create(user=request.user)
	return render(request, 'cart_details.html', {'cart': cart})
	

def register(request) -> render:
	
	if request.method == 'POST':
		form = UserCreation(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.set_password(form.cleaned_data["password"])
			user.save()
			login(request, user)
			return redirect("/")
	else:
		form = UserCreation()
	
	return render(request, 'registration/register.html', {'form': form})

def about(request) -> render:
	return render(request, "about.html")

def contact(request) -> render:
	return render(request, 'contact.html')

def item_detail(request, pk):
	item = get_object_or_404(Add_Item, pk=pk)
	return render(request, 'item_detail.html', {'item': item})
