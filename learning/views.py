from django.shortcuts import render,redirect
from .models import Student, Course, Question, Result


def register(request):

    if request.method=="POST":

        full_name=request.POST.get('full_name')

        name_parts=full_name.split()

        first_name=name_parts[0]

        last_name=" ".join(name_parts[1:]) if len(name_parts)>1 else ""

        email=request.POST.get('email')

        password=request.POST.get('password')

        phone_number=request.POST.get('phone_number')

        profile_pic=request.FILES.get(
            'profile_pic'
        )

        if Student.objects.filter(
            email=email
        ).exists():

            return render(
                request,
                'authentication/register.html',
                {'Error':'Email already exists'}
            )

        Student.objects.create(

            first_name=first_name,

            last_name=last_name,

            email=email,

            password=password,

            phone_number=phone_number,

            profile_pic=profile_pic

        )

        return redirect('login')

    return render(
        request,
        'authentication/register.html'
    )


def user_login(request):

    if request.method=="POST":

        email=request.POST.get('email')

        password=request.POST.get('password')

        student=Student.objects.filter(
            email=email,
            password=password
        ).first()

        if student:

            request.session[
                'student_id'
            ]=student.id

            return redirect(
                'home'
            )

        return render(
            request,
            'authentication/login.html',
            {'Error':'Invalid Email or Password'}
        )

    return render(
        request,
        'authentication/login.html'
    )


def home(request):

    student_id=request.session.get(
        'student_id'
    )

    if not student_id:

        return redirect(
            'login'
        )

    student=Student.objects.get(
        id=student_id
    )

    return render(
        request,
        'home/home.html',
        {'student':student}
    )


def user_logout(request):

    request.session.flush()

    return redirect(
        'login'
    )

def python_course(request):

    course = Course.objects.get(name="python")

    notes = course.notes.all().order_by("created_at")

    return render(
        request,
        "courses/python.html",
        {
            "course": course,
            "notes": notes,
        }
    )

def python_quiz(request):

    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("login")

    student = Student.objects.get(id=student_id)

    course = Course.objects.get(name="python")

    questions = Question.objects.filter(course=course)

    if request.method == "POST":

        score = 0

        total = questions.count()

        for question in questions:

            selected_answer = request.POST.get(str(question.id))

            if selected_answer == question.correct_answer:
                score += 1

        Result.objects.create(
            student=student,
            course=course,
            score=score,
            total=total
        )

        return render(
            request,
            "courses/result.html",
            {
                "score": score,
                "total": total,
            }
        )

    return render(
        request,
        "courses/quiz.html",
        {
            "course": course,
            "questions": questions,
        }
    )