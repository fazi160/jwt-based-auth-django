from django.db import models
from users.models import User
# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=150)
    details = models.TextField()
    image = models.CharField(max_length=300, blank=True, null=True)
    blogger = models.ForeignKey(User, on_delete=models.CASCADE)

class LikedBlogs(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('blog', 'users')
