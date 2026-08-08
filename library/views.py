from django.contrib.auth.decorators import login_required # check the user only login user will see the home page not other

from django.contrib.auth import authenticate,login,logout
from datetime import date
from django.shortcuts import render,redirect


# Create your views here.
from .models import Book,Student,IssueBook
@login_required(login_url="login")# it find the current user logged in
def Home(request):
    Books=Book.objects.all()
    Students=Student.objects.all()
    issued_book=IssueBook.objects.all()


    return render(request,"home.html",{"books":Books,"students":Students,"issued_books":issued_book})


def ADD1(request):
    if request.method == "POST":
        title=request.POST["title"]
        author=request.POST["author"]
        isbn=request.POST["isbn"]
        quantity=request.POST["quantity"]

        Book.objects.create(
            title=title,
            author=author,
            isbn=isbn,
            quantity=quantity
        )
        return redirect("/")
    return render(request,"add_book.html")


def ADD2(request):
    if request.method == "POST":
        name=request.POST["name"]
        roll=request.POST["roll"]
        department=request.POST["department"]
        phone=request.POST["phone"]

        Student.objects.create(
            name=name,
            roll=roll,
            department=department,
            phone=phone
        )
        return redirect("/")
    return render(request,"add_student.html")


def login_view(request):
    if request.method == "POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=authenticate(request,
                          username=username,
                          password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request,"login.html",{"error":"invalid username password"})
    return render(request,"login.html")

def issue_book(request):
    Books=Book.objects.all()
    Students=Student.objects.all()
    if request.method == "POST":
        student_id=request.POST.get("student")
        book_id=request.POST.get("book")
        my_student=Student.objects.get(id=student_id)
        my_book=Book.objects.get(id=book_id)
        IssueBook.objects.create(
            student=my_student,
            book=my_book
        )
        return redirect("/")


        

    return render(request,"add_issue.html",{"books":Books,"students":Students})




def logout_view(request):
    logout(request)
    return redirect("login")


def return_book(request,id):
    issue=IssueBook.objects.get(id=id)
    issue.return_date = date.today()
    issue.save()
    return redirect("/")