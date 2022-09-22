from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
# Create your models here.


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(
            2, "Name must be greater than 2 characters")]
    )
    description= models.TextField(null=True)
    price = models.PositiveIntegerField()
    picture = models.ImageField(
        default='default.png', upload_to='products_pics', null=True, blank=True)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)





class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    product= models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.user.username}'s order"


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reference_number = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)



