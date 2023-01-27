from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")

    def __str__(self):
        return f"title={self.title}, description={self.description}, technology={self.technology}, image={self.image}"