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
        
class Question(models.Model):

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    question = models.TextField()

    option1 = models.CharField(max_length=200)

    option2 = models.CharField(max_length=200)

    option3 = models.CharField(max_length=200)

    option4 = models.CharField(max_length=200)

    correct_answer = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class Result(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    score = models.IntegerField()

    total = models.IntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.student.first_name} - {self.score}/{self.total}"        