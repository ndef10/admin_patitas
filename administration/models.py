from django.db import models

# Create your models here.
class Provider(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    main_photo = models.ImageField(upload_to="providers/",
                                   blank=True, null=True)
    description = models.TextField()

# este comando se usa para traducir este modelo a la base de datos:
