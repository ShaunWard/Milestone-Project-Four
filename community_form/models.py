from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from products.models import Product


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date_of_post = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title + str(self.author)

    def get_absolute_url(self):
        return reverse('community_form')  #Takes user to the detail page of their post
