from django.db import models

# Create your models here.

class Profile(models.Model):
   name = models.CharField(max_length=30, blank=False, null=False)
   email = models.EmailField(blank=False, null=False)




   


