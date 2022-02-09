from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskList(models.Model):
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=300)
    #charfield ,it will created a row and give maximum number of length for task ,200 to 300 letters
    done = models.BooleanField(default=False)
    #booleanfield will do, the task is done or not by default task done false we want to check the task is unique or not
    
    def __str__(self):
        return self.task +" - "+str(self.done)
    