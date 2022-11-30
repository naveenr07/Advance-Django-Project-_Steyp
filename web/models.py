from django.db import models


class FileUploads(models.Model):
    ids = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255)
    my_files = models.FileField(upload_to='')

    def __str__(self):
        return self.file_name
