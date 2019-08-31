from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    published = models.DateTimeField(db_index=True, auto_now=True)
    author = models.ForeignKey('Blogger', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_detail', args=[str(self.pk)])

    class Meta:
        ordering = ['-published']


class Comment(models.Model):
    description = models.TextField()
    published = models.DateTimeField(db_index=True, auto_now_add=True)
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, db_index=True, blank=True, null=True)
    commentator = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.description)

    class Meta:
        ordering = ['-published']


class Blogger(models.Model):
    name = models.OneToOneField(User, on_delete=models.PROTECT)
    biography = models.TextField()

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('blog:blogger_detail', args=[str(self.pk)])

    class Meta:
        ordering = ['name']
