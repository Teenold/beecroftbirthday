from django.db import models

# Create your models here.
class Happy(models.Model):
    first_name = models.CharField(max_length=200)
    message = models.TextField()
    
    def __str__(self):
        return self.first_name
    
    