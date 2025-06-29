from django.db import models

# Create your models here.
 
class book(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=300, default="desc")
    rate = models.PositiveIntegerField(default=5)
    views = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.title