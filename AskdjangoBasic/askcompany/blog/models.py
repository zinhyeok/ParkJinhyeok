from askcompany.utils import uuid_upload_to
from django.db import models
from askcompany.utils import uuid_upload_to
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(blank=True, upload_to=uuid_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    # on_delete 소속된 부모(Post)가 삭제 되면 다 삭제(CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
