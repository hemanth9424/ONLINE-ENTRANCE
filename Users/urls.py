from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('login/', views.Login, name='login'),
    path('signup/', views.SignUp, name='signup'),
    path('logout/', views.Logout, name='logout'),
    path('index/', views.GetUserLists, name='AdminIndex'),
    path('getresult/', views.GetResult, name='getresult'),
    path('feedback/', views.GetFeedbackLists, name='feedback'),
    path('deleteaccount/', views.DeleteAccount, name='deleteaccount'),
    path('updateprofile/', views.UpdateProfile, name='updateprofile'),
    path('getUserDetails/', views.GetUserLists, name='getUserDetails'),
    path('modeltest/<program>', views.TakeModelTest, name='modeltest'),
    path('report/<str:id>/mark', views.MarkReport, name="mark-report"),
    path('getExamDetails/', views.GetExamsLists, name='getExamDetails'),
    path('updatepassword/', views.UpdatePassword, name='updatepassword'),
    path('AddNewQuestion/', views.AddNewQuestion, name='AddNewQuestion'),
    path('getReportsLists/', views.GetReportsLists, name='getReportsLists'),
    path('programselector/', views.ProgramSelector, name='programselector'),
    path('feedback/<str:id>/mark', views.MarkFeedBack, name="mark-feedback"),
    path('report/edit-report/<str:id>', views.EditReports, name='edit-report'),
    path('modeltest/<str:programme>/<str:subject>', views.GetSpecificQuestions),
    path('getSubjectDetails/', views.GetSubjectLists, name='getSubjectDetails'),
    path('getUserDetails/edit-user/<str:id>', views.EditUsers, name="edit-user"),
    path('subject/edit-subject/<str:id>', views.EditSubject, name='edit-subject'),
    path('getQuestionDetails/', views.GetQuestionLists, name='getQuestionDetails'),
    path('report-question/<str:id>', views.ReportQuestions, name='report-question'),
    path('feedback/edit-feedback/<str:id>', views.EditFeedback, name='edit-feedback'),
    path('getProgrammeDetails/', views.GetProgrammeLists, name='getProgrammeDetails'),
    path('detailed-result/<slug:slug>', views.DetailedHistory, name='detailed-history'),
    path('admin-change-password/', views.AdminChangePassword, name='admin-change-password'),
    path('getQuestionDetails/edit-question/<str:id>', views.EditQuestions, name="edit-question"),
    path('report-question/<str:id>/added', views.DisplayReportedQuestion, name='report-question-added'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='FindAccount.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetView.as_view(template_name='ResetPasswordSent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='NewPassword.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='RecoverPasswordComplete.html'), name='password_reset_complete'),
    path('<str:redirect_to>/', views.GoTo, name='go_to'),
]
