from django.db import models

class Maincategory(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)


    def __str__(self):
        return self.name
    
class Subcategory(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    maincategory=models.ForeignKey(Maincategory,on_delete=models.CASCADE)
    subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    color=models.CharField(max_length=20)
    size=models.CharField(max_length=20)
    stock=models.CharField(max_length=20,default="In Stock",null=True,blank=True)
    description=models.TextField()
    baseprice=models.CharField(max_length=20)
    discount=models.IntegerField(default=0,null=True,blank=True)
    finalprice=models.IntegerField()
    pic1=models.FileField(upload_to="uploads",default="",null="True",blank="True")
    pic2=models.FileField(upload_to="uploads",default="",null="True",blank="True")
    pic3=models.FileField(upload_to="uploads",default="",null="True",blank="True")
    pic4=models.FileField(upload_to="uploads",default="",null="True",blank="True")
    pic5=models.FileField(upload_to="uploads",default="",null="True",blank="True")

    def __str__(self):
        return self.name
    

class Buyer(models.Model):
        id=models.AutoField(primary_key=True)
        name=models.CharField(max_length=50)
        username=models.CharField(max_length=50,unique=True)
        email=models.EmailField(max_length=50)
        phone=models.CharField(max_length=15)
        addressline1=models.CharField(max_length=150)
        addressline2=models.CharField(max_length=150)
        addressline3=models.CharField(max_length=150)
        pin=models.CharField(max_length=10)
        city=models.CharField(max_length=50)
        state=models.CharField(max_length=50)
        pic6=models.FileField("uploads",default="",null="True",blank="True")
        
        def  __str__(self):
           return str(self.id)+""+self.username

