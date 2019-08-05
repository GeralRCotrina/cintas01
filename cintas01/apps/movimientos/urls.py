
from django.urls import path, re_path
from apps.movimientos import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login


urlpatterns = [
	re_path(r'^$', views.index,name='index'),
	re_path(r'index', views.index,name='index'),
	re_path(r'^mylogin$', views.mylogin,name='mylogin'),
    re_path(r'^logout$',logout_then_login,name='logout'),

	re_path(r'^c_filtrar/',login_required(views.AlpListar.as_view()),name='c_filtrar'),
	re_path(r'^c_lis_alp/?/$',login_required(views.CinLstAlp.as_view()),name='c_lis_alp'),
	re_path(r'^c_reordenar/',login_required(views.ReordenarCintas.as_view()),name='c_reordenar'),
	re_path(r'^c_ubicar/?/$',login_required(views.ActulizarUbicacion.as_view()),name='c_ubicar'),
]






