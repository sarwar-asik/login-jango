from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


    # def __str__(self):
    #     return self.username

    # class Meta:  # This should be inside the User class
    #     app_label = 'userapi'