from django.db import models

# Create your models here.


class Idea(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to='idea_image/%Y/%m/%d', null=True, blank=True)
    content = models.TextField()

    interest = models.IntegerField(default=0)
    devtool = models.ForeignKey(
        to='devtoolBlog.Devtool', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
