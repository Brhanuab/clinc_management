from django.urls import path
from .import views


urlpatterns=[

    path('creatdocter/<int:branch_id>/',views.creat_docter,name='creat_docter'),
    path('login/',views.login_view,name='login_view'),
    path('managerpage/<int:branch_id>/',views.manager_dashbord,name='manager_dashbord'),
    
           
]