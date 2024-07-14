from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator, MaxValueValidator





class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    about = models.TextField()
    phonenumber = PhoneNumberField(blank=False)
    country = CountryField()
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'about', 'phonenumber']


    # Add unique related_name attributes to avoid clashes
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='customuser_set'  # Unique related_name
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_permissions'  # Unique related_name
    )




class Seller(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='seller')
    skills = models.TextField(blank=True, null=True)
    portfolio = models.TextField(blank=True, null=True)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    number_of_reviews = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        # Add the user to the Seller group
        seller_group, created = Group.objects.get_or_create(name='Seller')
        self.user.groups.add(seller_group)
        super().save(*args, **kwargs)

class Buyer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='buyer')
    favorite_services = models.ManyToManyField('Service', related_name='favorited_by')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        # Add the user to the Seller group
        buyer_group, created = Group.objects.get_or_create(name='Buyer')
        self.user.groups.add(buyer_group)
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=225)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6, validators=[MinValueValidator(0.00)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', related_name='services')

    def __str__(self):
        return self.title


class Order(models.Model):
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    #TODO: 
    # Change the on_delete situation to be PROTECTED if an order is active.
    def __str__(self):
        return f"Order #{self.id}"


class Tag(models.Model):
    tag = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tag


class Rating(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='reviews')
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating for {self.service.title} by {self.buyer.username}"


class Transaction(models.Model):
    pass
