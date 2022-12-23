from django.db import models
from category.models import category
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

class Restaurant(models.Model):
    title = models.CharField(max_length=64)
    adress = models.CharField(max_length=64)
    logo = models.ImageField(upload_to='photo/image',blank=True)
    description = models.TextField(max_length=360)
    category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def no_of_reviews(self):
        reviews = Review.objects.filter(restaurant=self)
        return len(reviews)

    def avg_review(self):
        sum = 0
        reviews = Review.objects.filter(restaurant=self)
        for review in reviews:
            sum += review.stars
        if len(reviews) > 0:
            return sum / len(reviews)
        else:
            return 0


class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='photo/image')
    stars = models.IntegerField(validators=[MinValueValidator(1),
    MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'restaurant'),)
        index_together = (('user', 'restaurant'),)
