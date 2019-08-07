from django.conf.urls import url,include
from django.urls import path
from . import views

from Campus_Recruitment_project import  settings

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name="student"
urlpatterns=[
    path('',views.log,name="login"),
    path('stuReg/(?P<company_id>[0-9]+)/ajax',views.ajax,name="ajax"),
    path('stuReg',views.stuReg,name="stuReg"),
    path('stuReg/student_panel',views.student_panel,name="student_panel"),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
