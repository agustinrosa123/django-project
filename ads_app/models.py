from django.db import models
from django.conf import settings

class Ad(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    description = models.TextField(null=True, blank=True)
    picture = models.BinaryField(null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
