from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200,db_index=True,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('clients_by_category',args=[self.slug])

class Client(models.Model):
    category = models.ForeignKey(Category,related_name='Clients', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200,db_index=True,unique=True)
    cover_image = models.ImageField(upload_to="Clients/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('category',)
        verbose_name = 'client'
        verbose_name_plural = 'clients'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('client_detail',args=[self.id, self.slug])

class Photo(models.Model):
    client = models.ForeignKey(Client,related_name='photos', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='Clients/photos/%Y')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated',)
    def __str__(self):
        return self.name

class Video(models.Model):
    client = models.ForeignKey(Client,related_name='videos', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    video = models.FileField(upload_to='Clients/videos/%Y')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated',)
    def __str__(self):
        return self.name
