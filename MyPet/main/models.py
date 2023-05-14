from django.db import models
from django.contrib.auth.models import User
# Create your models here.
    
class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,db_column="user_id")
    img = models.ImageField(null=False, upload_to="post/%Y%m%d")
    description = models.TextField(null=False)
    likes=models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)


