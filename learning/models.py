from django.db import models

class Student(models.Model):

    GENDER_CHOICES=[
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    ]

    first_name=models.CharField(max_length=50)

    middle_name=models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    last_name=models.CharField(max_length=50)

    email=models.EmailField(unique=True)

    password=models.CharField(max_length=100)

    phone_number=models.CharField(max_length=15)

    birth_date=models.DateField(
        blank=True,
        null=True
    )

    gender=models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default='Male'
    )

    subject=models.CharField(
        max_length=100,
        default=''
    )

    address=models.TextField(
        blank=True,
        null=True
    )

    city=models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    state=models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    parent_contact=models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    profile_pic=models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.first_name