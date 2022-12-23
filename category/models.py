from django.db import models
#from django.urls import reverse

# Create your models here.
class category(models.Model):
    category = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    image = models.ImageField(upload_to='photo/image',blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    #def get_url(self):
        #return reverse('products_by_thaishop_category', args=[self.slug])

    def __str__(self):
        return self.category