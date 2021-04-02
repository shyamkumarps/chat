from django.db import models
import datetime



# Create your models here.
class Registration(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50, default="")
    confim_password = models.CharField(max_length=50, default="")
    DOB = models.DateField(max_length=8)
    Email = models.EmailField(max_length = 254,null=True,blank=True)
    Bio = models.TextField()

    def upload_dir(self,filename):
        path= 'model/photo/{}'.format(filename)
        return path


    photo = models.ImageField(upload_to=upload_dir, null=True,blank=True)


    def __str__(self):
        return f"{self.username} - {self.Email}"



class Login(models.Model):
    username = models.CharField(max_length=100,default="")
    password = models.CharField(max_length=50, default="")

class User(models.Model):
    username = models.CharField(max_length=100)
    Email = models.EmailField(max_length = 254,null=True,blank=True)
    

class News_Feed(models.Model):
    Title = models.CharField(max_length=100)
    Sub_Heading = models.CharField(max_length=100)
    Content = models.TextField()

    def upload_dir(self,filename):
        path = 'Content_Image/photo/{}'.format(filename)
        return path


    Content_Image = models.ImageField(upload_to=upload_dir, null=True,blank=True)
        
    Author = models.CharField(max_length=100)
    DateOfPublish = models.DateTimeField(max_length=20)

class Message(models.Model):
     sender = models.ForeignKey(User, related_name="sender",on_delete=models.CASCADE)
     reciever = models.ForeignKey(User, related_name="reciver",on_delete=models.CASCADE)
     msg_content = models.CharField(max_length=100)
     created_at = models.TimeField(auto_now=True)


