from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(verbose_name="Pavadinimas")
    content = models.TextField(verbose_name="Turinys")
    date = models.DateTimeField(verbose_name="Data", auto_now_add=True)
    author = models.ForeignKey(to=User, verbose_name="Autorius", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Įrašas"
        verbose_name_plural = "Įrašai"
        ordering = ['-pk']

    def comments_count(self):
        return self.comments.count()

    comments_count.short_description = "Komentarų skaičius"

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(to="Post", verbose_name="Įrašas", on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(verbose_name="Turinys")
    date = models.DateTimeField(verbose_name="Data", auto_now_add=True)
    author = models.ForeignKey(to=User, verbose_name="Autorius", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Komentaras"
        verbose_name_plural = "Komentarai"
        ordering = ['-pk']