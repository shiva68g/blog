from django.db import models

class modelblogs(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="pic")
    description = models.TextField()
    data = models.TextField()

    def __str__(self):
        return self.title