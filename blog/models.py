from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class Post(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(unique=True)
    title = models.CharField('Titulo', max_length=100)
    thumbnail = models.FileField(upload_to='uploads/%Y/%m/%d/')
    excerpt = models.TextField('Resumo')
    body = models.TextField('Texto')
    published_at = models.DateField('Publicado')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField('Titulo', max_length=100)
    body = models.TextField('Texto')

    def __str__(self):
        return self.title
