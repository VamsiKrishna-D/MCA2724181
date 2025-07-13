from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'roll_number', 'course', 'enrollment_date']
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')

class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'student_list.html'

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'roll_number', 'course', 'enrollment_date']
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student_list')
