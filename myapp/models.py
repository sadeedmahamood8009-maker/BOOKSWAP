from django.db import models

# Create your models here.
class login(models.Model):
    user_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class user(models.Model):
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    photo=models.CharField(max_length=100)
    gender=models.CharField(max_length=100,default="male")
    phone_number=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    point=models.CharField(max_length=100,default="0")
    refference=models.CharField(max_length=1000,default="")

class Book(models.Model):
    USER = models.ForeignKey(user,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    condition=models.CharField(max_length=100)
    prize=models.CharField(max_length=100)
    author_name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    photo=models.CharField(max_length=100,default="null")
    status=models.CharField(max_length=100,default="AVAILABLE")
    point=models.CharField(max_length=100,default="0")


class complaint(models.Model):
    USER = models.ForeignKey(user,on_delete=models.CASCADE)
    date=models.DateField()
    complaint=models.CharField(max_length=100)
    reply=models.CharField(max_length=100)
    status=models.CharField(max_length=100)

class notification(models.Model):
    date=models.DateField()
    notification= models.CharField(max_length=100)


class Request(models.Model):
    USER = models.ForeignKey(user, on_delete=models.CASCADE)
    BOOK = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=100)

class review(models.Model):
    USER = models.ForeignKey(user, on_delete=models.CASCADE)
    BOOK = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateField()
    review = models.CharField(max_length=100)
    rating = models.CharField(max_length=100,default="")

class chat(models.Model):
    FROM_ID = models.ForeignKey(login, on_delete=models.CASCADE,related_name="fid")
    TO_ID = models.ForeignKey(login, on_delete=models.CASCADE,related_name="tid")
    date = models.DateField()
    message = models.CharField(max_length=100)


class enquiery(models.Model):
    USER = models.ForeignKey(user, on_delete=models.CASCADE)
    date = models.DateField()
    enquiery = models.CharField(max_length=100)

class public_chat(models.Model):
    FROM_ID = models.ForeignKey(login, on_delete=models.CASCADE,related_name="fromid")
    TO_ID = models.ForeignKey(login, on_delete=models.CASCADE,related_name="toid")
    date = models.DateField()
    message = models.CharField(max_length=100)

class Group_chat(models.Model):
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE)
    date = models.DateField()
    message = models.CharField(max_length=100)

class payment(models.Model):
    USER = models.ForeignKey(user, on_delete=models.CASCADE)
    date = models.DateField()
    payment=models.CharField(max_length=100)
    status = models.CharField(max_length=100)









