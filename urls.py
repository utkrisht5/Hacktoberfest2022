from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name="index"),
    path('victimSignup', views.victimSignup, name="victimSignup"),
    path('victimLogin', views.victimLogin, name='victimLogin'),
    path('authoritySignup', views.authoritySignup, name="authoritySignup"),
    path('authorityLogin', views.authorityLogin, name="authorityLogin"),
    path('authorityHome', views.authorityHome, name="authorityHome"),
    path('victimHome', views.victimHome, name="victimHome"),
    path('victimLogout', views.victimLogout, name="victimLogout"),
    path('authorityLogout', views.authorityLogout, name="authorityLogout"),
    path('victimComplaint/<int:id>', views.victimComplaint, name='victimComplaint'),
    path('pastComplains', views.pastComplains, name='pastComplains'),
    path('editComplain/<int:id>', views.editComplain, name='editComplain'),
    path('publicComplains', views.publicComplains, name='publicComplains'),
]
