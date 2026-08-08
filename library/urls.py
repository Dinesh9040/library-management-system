from django.urls import path
from . import views

urlpatterns = [
    path("",views.Home,name="Homepage"),
    path("add_book/",views.ADD1,name="Add_book"),
    path("add_student",views.ADD2,name="Add_Studet"),
    path("login/",views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path("issue/",views.issue_book,name="Issue book"),
    path("return_book/<int:id>/",views.return_book,name="return_book")
    
    
    
]