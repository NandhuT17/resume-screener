from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('recruiter_dashboard/', views.recruiter_dashboard, name="recruiter_dashboard"),
    path('create_job/',views.create_job, name="create_job"),
]