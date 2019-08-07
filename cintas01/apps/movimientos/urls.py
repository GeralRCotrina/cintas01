
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

	re_path(r'^m_reg$',login_required(views.MovimientoCreate.as_view()),name='m_reg'),
	re_path(r'^m_reg1$',login_required(views.MovimientoCreate1.as_view()),name='m_reg1'),
	re_path(r'^c_lst_alj$',login_required(views.CinLstAlj.as_view()),name='c_lst_alj'),

	re_path(r'^a_lis/',login_required(views.AljList.as_view()),name='a_lis'),
	re_path(r'^a_reg/',login_required(views.AljCreate.as_view()),name='a_reg'),
	re_path(r'^a_edi/(?P<pk>\d+)/$',login_required(views.AljUpdate.as_view()),name='a_edi'),
	re_path(r'^a_eli/(?P<pk>\d+)/$',login_required(views.AljDelete.as_view()),name='a_eli'),

	re_path(r'^p_lis/',login_required(views.ProyList.as_view()),name='p_lis'),
	re_path(r'^p_reg/',login_required(views.ProyCreate.as_view()),name='p_reg'),
	re_path(r'^p_edi/(?P<pk>\d+)/$',login_required(views.ProyUpdate.as_view()),name='p_edi'),
	re_path(r'^p_eli/(?P<pk>\d+)/$',login_required(views.ProyDelete.as_view()),name='p_eli'),
]






