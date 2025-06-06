from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('profile/', views.profile, name = "student_profile"),
    path('delete/<int:id>', views.delete_student, name = "delete_student")
]
