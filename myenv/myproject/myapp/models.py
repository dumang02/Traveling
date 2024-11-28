from django.db import models

# Create your models here.

class login(models.Model):
    username=models.CharField(max_length=30,default="UMANG")
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=30)
    
    def __str__(self):
        return self.email
    
    

class tour(models.Model):
     pack_id=models.AutoField(primary_key=True)
     name=models.CharField(max_length=50)
     
     def __str__(self):
         return self.name

    
class package(models.Model):
    # id=models.AutoField(primary_key=True)
    pic=models.ImageField(upload_to='media/')
    place=models.CharField(max_length=30)
    days=models.IntegerField()
    tour_pack=models.ForeignKey(tour,on_delete=models.CASCADE)
    person=models.IntegerField()
    explor=models.CharField(max_length=200)
    price=models.IntegerField()
        
    def __str__(self):
        return self.place
    