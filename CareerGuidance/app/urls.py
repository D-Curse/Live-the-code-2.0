from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.dataAdmin, name='add'),
    path('addInfo/', views.dataAdminInfo, name='addInfo'),
    path('signup/', views.signup, name='signup'),   
    path('course_details/', views.courseDetails, name='courseDetails'),
    path('careerLibrary/', views.library, name='careerLibrary'),
    path('logout/',views.logout_view, name='logout_view'),
    path('stream/<id>', views.stream, name='stream'),
]