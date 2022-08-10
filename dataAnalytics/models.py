from django.db import models


# Create your models here.
class CSVFILE(models.Model):
    file_name = models.FileField(upload_to='dataAnalytics')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return self.file_name.name
