from django.shortcuts import render

from polls.models import Student
def index(request):
    return render(request, "index.html")


def students(request):
    students = Student.objects.all()
    return render(request, "students.html", {"students": students})