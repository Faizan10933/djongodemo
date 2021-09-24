from django.db import models

# Create your models here.
class Todo(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, default="")
    

    def __str__(self):
        return self.title
