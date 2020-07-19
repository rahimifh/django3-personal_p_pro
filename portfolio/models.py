from django.db import models

# Create your models here.

class Project(models.Model):

        title =models.CharField(max_length = 100)
        description =models.CharField(max_length= 250)
        image = models.ImageField(upload_to='portfolio/images/')
        url =models.URLField(blank=True)

        def __str__(self):
            return self.title

class  messagedata (models.Model):
    full_name =models.CharField(max_length=100)
    email =models.CharField (max_length=100)
    phone = models.CharField (max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.full_name
