from django.contrib import admin
from .models import Student, Course, Notes, Question, Result

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        'first_name',
        'last_name',
        'email',
        'phone_number'
    )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'description'
    )


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'course',
        'created_at'
    )

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):

    list_display = (
        'question',
        'course',
        'correct_answer'
    )


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):

    list_display = (
        'student',
        'course',
        'score',
        'total',
        'created_at'
    )    