from django.db import models

# Create your models here.

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    nickname = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self):
        return self.nickname
    
class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey("User", related_name="user", on_delete=models.CASCADE, db_column="user_id")
    img = models.FileField(null=False)
    description = models.TextField(null=False)

    def __str__(self):
        return self.id


