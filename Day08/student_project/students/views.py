
# Create your views here.
from django.shortcuts import render, redirect
from .models import Student

def list_students(request):
    students = Student.objects.all()
    return render(request, 'list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        rollno = request.POST['rollno']
        name = request.POST['name']
        marks = request.POST['marks']
        Student.objects.create(rollno=rollno, name=name, marks=marks)
        return redirect('list_students')
    return render(request, 'add.html')

def edit_student(request, rollno):
    student = Student.objects.get(rollno=rollno)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.marks = request.POST['marks']
        student.save()
        return redirect('list_students')
    return render(request, 'edit.html', {'student': student})

def delete_student(request, rollno):
    student = Student.objects.get(rollno=rollno)
    if request.method == 'POST':
        student.delete()
        return redirect('list_students')
    return render(request, 'students/delete.html', {'student': student})

def green(request):
    return render(request, 'green.html')



