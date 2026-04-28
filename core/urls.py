from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('recruiter_dashboard/', views.recruiter_dashboard, name="recruiter_dashboard"),
    path('create_job/',views.create_job, name="create_job"),
    path('delete_job/<int:job_id>/',views.delete_job, name="delete_job"),
]