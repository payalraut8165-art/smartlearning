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

class Course(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Notes(models.Model):

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="notes"
    )

    title = models.CharField(max_length=200)

    pdf = models.FileField(upload_to="notes/")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        