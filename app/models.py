from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField('admin', default=False)
    is_agent = models.BooleanField('agent', default=False)
    is_lead = models.BooleanField('lead', default=False)

class Agent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="agent")

    def __str__(self):
        return str(self.user)
    
class Lead(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"