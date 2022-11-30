from django.db import models


class FileUploads(models.Model):
    ids = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255)
    my_file = models.FileField(upload_to='')
