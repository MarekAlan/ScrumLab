from django.db import models
import datetime
# from django.template.defaultfilters import slugify
# from django.urls import reverse


# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=64)
    ingredients = models.TextField(null=True)
    description = models.TextField(null=True)
    created = models.DateTimeField(default=datetime.date.today)
    updated = models.DateTimeField(default=datetime.date.today)
    preparation_time = models.IntegerField(null=True)
    preparation = models.TextField(null=True)
    votes = models.IntegerField(default=0)


class Schedule(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)
    created = models.DateTimeField(default=datetime.date.today)
    recipes = models.ManyToManyField(Recipe, through='RecipePlan')

    
CHOICES = (
    ('Mon', 'Poniedziałek'),
    ('Tue', 'Wtorek'),
    ('Wed', 'Środa'),
    ('Thu', 'Czwartek'),
    ('Fri', 'Piątek'),
    ('Sat', 'Sobota'),
    ('Sun', 'Niedziela')
)


class DayName(models.Model):
    name = models.CharField(max_length=64, choices=CHOICES)
    order = models.SmallIntegerField(unique=True)


class RecipePlan(models.Model):
    meal_name = models.CharField(max_length=256)  # (śniadanie, obiad itp)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    order = models.ForeignKey(DayName, on_delete=models.CASCADE, related_name='order_id')
    day_name = models.ForeignKey(DayName, on_delete=models.CASCADE)
    

   # class Page(models.Model):
#     title = models.CharField(max_length=64)
#     description = models.TextField()
#     slug = models.SlugField(null=False, unique=True)
#
#     def __str__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return reverse('page_detail', kwargs={'slug': self.slug})
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title)
#         return super().save(*args, **kwargs)

    #link do dokumentacji https://learndjango.com/tutorials/django-slug-tutorial#slugs
    # takze wykomentowane importy !!! ORAZ admin.py
    #link do reverse z biblioteki django : https://docs.djangoproject.com/en/4.0/ref/urlresolvers/