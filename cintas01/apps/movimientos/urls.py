
from django.urls import path, re_path
from apps.movimientos import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login


urlpatterns = [
	re_path(r'^$', views.index,name='index'),
	re_path(r'index', views.index,name='index'),
	re_path(r'^mylogin$', views.mylogin,name='mylogin'),
    re_path(r'^logout$',logout_then_login,name='logout'),
	re_path(r'^c_filtrar/',login_required(views.CinFiltrar.as_view()),name='c_filtrar'),
]






