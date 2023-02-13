from django.db import models

# Create your models here.
class Translation(models.Model):
    id = models.AutoField(primary_key=True)
    input = models.CharField(max_length=500)
    output = models.CharField(max_length=500)
    fromUser= models.CharField(max_length=500)
    # fromUser= models.ForeignKey(User, verbose_name="user")
    def __str__(self):
        return self.input

