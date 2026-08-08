from django.contrib import admin

# Register your models here.
from .models import Student,Book,IssueBook
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(IssueBook)
