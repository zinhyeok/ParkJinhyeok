from django.db import models

# Create your models here.


class Idea(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to="media/%Y/%m/%d/", null=True, blank=True)
    desc = models.TextField()
    interest = models.PositiveIntegerField(default=0)
    devtool = models.ForeignKey("devTools.devTool", on_delete=models.CASCADE)
