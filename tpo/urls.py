from django.conf.urls import url
from . import views
from django.urls import path
app_name='tpo'
urlpatterns=[
    path('',views.tpo,name="yoo"),
    path('logtpo',views.logtpo,name="logtpo"),
    path('/<company_id>/placed',views.placed,name="pl"),
    path('/<company_id>/delete',views.dlt,name="dlt"),
]
