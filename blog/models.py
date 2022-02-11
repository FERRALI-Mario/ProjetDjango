from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class StatusManager(models.Manager):
    def get_queryset(self):
        return super(StatusManager, self).get_queryset().filter(status='Monde')


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    STATUS = {
        ('Moi', 'moi'),
        ('Monde', 'monde')
    }
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    content = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, default='Monde', max_length=5)
    objects = models.Manager()
    published = StatusManager()

    def __str__(self):
        return f'{self.id}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-id']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.id}'
