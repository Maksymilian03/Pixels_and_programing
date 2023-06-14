from django.db import models

# Create your models here.


class Article(models.Model):
    ID = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64)
    contents = models.TextField()
    date = models.DateField()
    like_counter = models.IntegerField(default=0)
    com_counter = models.IntegerField(default=0)
    jpg = models.ImageField(upload_to='blog/static/jpg', null=True, blank=True)

    def __str__(self):
        return f"ID: {self.ID} Title: {self.title}, Contents: {self.contents}"
