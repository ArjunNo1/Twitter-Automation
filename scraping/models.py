from email.policy import default
from django.db import models
# import dao
from django.utils import timezone
class Post(models.Model):
    # lst=[]
    # url = models.CharField(max_length=250, unique=True)
    dateposted = models.CharField(max_length = 200)
    text = models.TextField()
    summarized_text = models.TextField(default = "NS")
    likes = models.PositiveIntegerField()
    twtpost = models.BooleanField(default=False)  

    created_date = models.DateTimeField(default=timezone.now)
    # lst.append(dateposted)
    # lst.append(text)
    # lst.append(likes)
    # lst.append(created_date)
    def __str__(self):
        return self.text[:10]
    class Meta:
        ordering = ['dateposted']
    class Admin:
        pass
    # dao.insertData(lst,tablename)
    # Post('public.tweet')

# Create your models here.
