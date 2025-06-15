from django.db import models


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Item(Timestamp):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    stock = models.IntegerField()
    thumbnail = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
