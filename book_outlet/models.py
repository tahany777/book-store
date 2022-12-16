from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinLengthValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False) #Harry Potter 1 => harry-poter-1

    def get_absolute_url(self):
        # return reverse("book_detail", args=[self.id])
        return reverse("book_detail", args=[self.slug])


    def save(self, *args, **kwargs):
        #make sure that added for all data in the database
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.title}({self.rating})"