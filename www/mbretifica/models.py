from django.db import models
from django.contrib.auth.models import User

class mbretifica(models.Model):
    id = models.AutoField(primary_key = True, auto_created = True)
    title_product = models.CharField(max_length = 50)
    date = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)