from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
	path("", views.home, name="home"),
	path('register/', views.register, name='register'),
	path('about/', views.about, name='about'),
	path('contact/', views.contact, name='contact'),
	path('accounts/profile/', views.profile, name='profile'),
	path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
	path('cart/', views.cart_details, name='cart_details'),
	path('cart/add/<int:item_id>', views.add_to_cart, name='add_to_cart'),
	path('cart/remove/<int:item_id>', views.remove_from_cart, name='remove_from_cart'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
	
]
