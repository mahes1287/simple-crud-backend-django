from django.db import models

# Create your models here.
class Translations(models.Model):
    id = models.AutoField(primary_key=True)
    input = models.CharField(max_length=500)
    output = models.CharField(max_length=500)
    fromUser= models.CharField(max_length=500)
    # fromUser= models.ForeignKey(User, verbose_name="user")


# TODO create User and connect it, then update the fromUser field