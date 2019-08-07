from django.conf.urls import url,include
from django.urls import path
from . import views
app_name="company"
urlpatterns=[
    path('',views.home,name="home"),
    path('login',views.log,name="login"),
    path('stuLog/',include('student.urls', namespace="stu")),
    path('tpo/',include('tpo.urls', namespace="tp")),
    path('signUp',views.signUp,name="signUp"),
    path('<stu_Roll_number>/list',views.ishu,name="list"),
    path('<stu_Roll_number>/select',views.selected,name="select"),
    path('<company_id>/hired',views.hired,name="hired"),
    path('company_panel',views.company_panel,name="company_panel"),
    path('search',views.search,name="search"),
]
