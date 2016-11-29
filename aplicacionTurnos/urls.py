from django.conf.urls import url
from . import views
from .views import LoginView

urlpatterns = [
    url(r'^login$', LoginView.as_view()),
    url(r'^logout$', views.logout_view) ,
    url(r'^login$', LoginView.as_view()),
    url(r'^$', views.home),
    url(r"^cambioDia/(?P<dia>\S+)$", views.cambioDia),
    #url(r"^cambioDia/(?P<dia>\S+)/(?P<medicopk>\S+)$", views.cambioDia),
    url(r'^nuevoPaciente$', views.nuevoPaciente),
    url(r'^editarPaciente/(?P<pk>[0-9]+)/$', views.editarPaciente),
    #url(r'^eliminiar_paciente/(?P<pk>[0-9]+)/$', views.eliminarPaciente),
    url(r'^eliminarPaciente/(?P<pk>[0-9]+)/$', views.eliminarPaciente),
    url(r'^nuevoMedico$', views.nuevoMedico),
    url(r'^editarMedico/(?P<pk>[0-9]+)/$', views.editarMedico),
    url(r'^eliminarMedico/(?P<pk>[0-9]+)/$', views.eliminarMedico),
    url(r'^nuevoTratamiento$', views.nuevoTratamiento),
    url(r'^editarTratamiento/(?P<pk>[0-9]+)/$', views.editarTratamiento),
    url(r'^eliminarTratamiento/(?P<pk>[0-9]+)/$', views.eliminarTratamiento),
    url(r'^nuevoEspecialidad$', views.nuevoEspecialidad),
    url(r'^editarEspecialidad/(?P<pk>[0-9]+)/$', views.editarEspecialidad),
    url(r'^eliminarEspecialidad/(?P<pk>[0-9]+)/$', views.eliminarEspecialidad),
    url(r'^nuevoObraSocial$', views.nuevoObraSocial),
    url(r'^editarObraSocial/(?P<pk>[0-9]+)/$', views.editarObraSocial),
    url(r'^eliminarObraSocial/(?P<pk>[0-9]+)/$', views.eliminarObraSocial),
    #url(r'^nuevoTurno$', views.nuevoTurno),
    url(r'^nuevoTurno$', views.home),
    url(r'^editarTurno/(?P<pk>[0-9]+)/$', views.editarTurno),
    url(r'^eliminarTurno/(?P<pk>[0-9]+)/$', views.eliminarTurno),
    #url que espera eliminarTurno/ un numero de cualquier tamaño / letras o numero y guion cualquier tamaño /
    #url(r'^eliminarTurno/(?P<pk>[0-9]+)/(?P<dia>[-\w]+)/$', views.eliminarTurno),
    url(r'^busquedaPaciente/$', views.busquedaPaciente),
    url(r'^busquedaMedico/$', views.busquedaMedico),
    url(r'^busquedaEspecialidad/$', views.busquedaEspecialidad),
    url(r'^busquedaTratamiento/$', views.busquedaTratamiento),
    url(r'^busquedaObraSocial/$', views.busquedaObraSocial),
]
