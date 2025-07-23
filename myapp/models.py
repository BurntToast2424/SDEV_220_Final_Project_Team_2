from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Add_Item(models.Model):

	seasons = [
		("spring", "Spring"), 
		("summer", "Summer"),
		("fall", "Fall"),
		("winter", "Winter")
	]

	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	listing_name = models.CharField(max_length=200)
	listing_description = models.TextField()
	created_on = models.DateTimeField(default=timezone.now)
	price = models.DecimalField(max_digits=10, decimal_places=2)

	season = models.CharField(max_length=10, choices=seasons, default='summer')

	def publish(self) -> None:
		self.published_date = timezone.now()
		self.save()

	def __str__(self) -> str:
		return f"{self.listing_name} [${self.price}]"

class Cart(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self) -> str:
		return f"Cart of {self.user.username}"
	
	def total_items(self) -> int:
		return sum(item.quantity for item in self.items.all())
	
	def total_price(self) -> float:
		return sum(item.quantity * item.item.price for item in self.items.all())

class CartItem(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
	item = models.ForeignKey(Add_Item, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)
	
	class Meta:
		unique_together = ('cart', 'item')

	def __str__(self) -> str:
		return f"{self.quantity} x {self.item.listing_name}"
