from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="/"),
    path('blogs/',views.addblog, name="add-blogs"),
    path('blogview/<int:id>',views.viewBlog, name="blogview"),
    
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),

    path('logout/', views.logoutPage, name="logout"),

]
