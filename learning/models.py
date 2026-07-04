from django.db import models

class Student(models.Model):

    first_name=models.CharField(max_length=50)

    last_name=models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    email=models.EmailField(unique=True)

    password=models.CharField(max_length=100)

    phone_number=models.CharField(max_length=15)

    profile_pic=models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.first_name