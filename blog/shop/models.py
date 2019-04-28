from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

