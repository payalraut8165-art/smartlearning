from django.shortcuts import render, redirect
from .models import Student

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        birth_date = request.POST.get('birth_date')
        gender = request.POST.get('gender')
        subject = request.POST.get('subject')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        parent_contact = request.POST.get('parent_contact')
        profile_pic = request.FILES.get('profile_pic')

        if not (first_name and last_name and email and password and phone_number):
            return render(request, 'authentication/register.html', {"Error": "Please fill required fields."})

        if Student.objects.filter(email=email).exists():
            return render(request, 'authentication/register.html', {"Error": "Email already registered."})

        Student.objects.create(
            first_name=first_name, middle_name=middle_name, last_name=last_name,
            email=email, password=password, phone_number=phone_number,
            birth_date=birth_date, gender=gender, subject=subject,
            address=address, city=city, state=state,
            parent_contact=parent_contact, profile_pic=profile_pic
        )
        return redirect('login')

    return render(request, 'authentication/register.html')


def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        student = Student.objects.filter(email=email, password=password).first()

        if student:
            request.session['student_id'] = student.id
            return redirect('home')
        
        return render(request, 'authentication/login.html', {'Error': 'Invalid Email or Password'})

    return render(request, 'authentication/login.html')


def home(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('login')
    
    student = Student.objects.get(id=student_id)
    return render(request, 'home/home.html', {'student': student})


def user_logout(request):
    if 'student_id' in request.session:
        del request.session['student_id']
    return redirect('login')