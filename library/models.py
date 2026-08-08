from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    department=models.CharField(max_length=100)
    phone=models.IntegerField()

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    isbn=models.CharField(max_length=100)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title
    
class IssueBook(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name="issed_book")
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name="issed_book")
    issue_date=models.DateField(auto_now_add=True)
    return_date=models.DateField(null=True,blank=True)
