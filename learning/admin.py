from django.contrib import admin
from .models import Student, Course, Notes


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