from django.db import models


class Uploadfiles(models.Model):
    file_name = models.CharField(max_length=100)
    my_files = models.FileField(upload_to="")
