
from django.db import models
from django.contrib.auth.models import User

class ReviewUser(models.Model):

    user = models.OneToOneField(User)

    # foxycart customer id
    customer_id = models.IntegerField()

