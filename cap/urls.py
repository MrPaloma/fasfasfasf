from django.contrib import admin
from django.urls import path, include
from apps.views import ( SignUpFormView ,Login, buscador, dashboard, grupo_normativa,home , index, liquid, 
    comision, plan, plan_edit, plan_delete, carga_rules,preguntas,signup,
	entrevistas, charts,member, configs, works, foro_comentarios,
    password_reset,SignUpOthers,success_sign_up,
    #johao
    dash,palabra_clave,delete_palclave,update_template,update_clave,normas_tecnicauso,busqueda_provedor,busq_palclave_prov)

from apps.views import busque_normativa,busqueda_clavenormativa,register_palabra_clave
    #end
from django.conf import settings

from apps.views import logout_view

from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', include('apps.urls')),
    #path('', login, name='login'),
    path('foro/', include('foro.urls')),
    path('normativas/', include('normas.urls')),
    path('cursos/', include('cursos.urls')),
    path('', Login.as_view(), name='login'),
    path('login/', Login.as_view(), name='login'),
    path('home/', dashboard, name='home'),
    path('grupo-normativa/<int:tn>', grupo_normativa, name='grupo-normativa'),
    path('buscador', buscador, name='buscador'),

    path('db-admin/', admin.site.urls),
    path('success_sign_up/', success_sign_up, name='success_sign_up'),
    path('logout/', logout_view, name='logout'),
    #path('sign-up/', signup, name='sign-up'),
    #path('normas/', include('apps.normas.urls',namespace='Normas')),
    #path('foro/', include('apps.foro.urls',namespace='Normas')),
    
    path('dash/', dash, name='dash'),

    path('carga_rules/', carga_rules, name='carga_rules'),
    # path('member/', member, name='member'),

    # path('foro/', foro, name='foro'),
    # path('foro_temas/', foro_temas, name='foro_temas'),
    # path('foro_comentarios/', foro_comentarios, name='foro_comentarios'),
    
    #path('sign-up-user/', SignUpFormView.as_view(),name='sign-up-user'),
    path('sign-up/', SignUpOthers.as_view(), name='sign-up'),
    path('password_reset/', password_reset, name='password_reset'),
    path('preguntas/', preguntas, name='preguntas'),


    #johao
    path('search_normat/',busqueda_clavenormativa,name='search_normat'),
    path('bus_normaclave/',busque_normativa,name='bus_normaclave'),
    #palabra clave
    path('register_clave/<int:codigo>',palabra_clave,name='register_clave'),
    path('date_palabraclave/<int:codigo>',register_palabra_clave,name='date_palabraclave'),
    path('delete_clave/<int:codigo>',delete_palclave,name='delete_clave'),
    
    path('update_template/<int:codigo>',update_template,name='update_template'),
    path('update_clave/<int:codigo>',update_clave,name='update_clave'),
    #

    path('norma_tecuso/',normas_tecnicauso,name='norma_tecuso'),
    path('bus_provedor/',busqueda_provedor,name='bus_provedor'),
    path('bus_palclave/',busq_palclave_prov,name='bus_palclave'),
     
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),


    #endjohao#


    # path('plan', plan, name='plan'),
    # path('plan/plan_edit/<int:pk>/', plan_edit, name='plan_edit'),
    # path('plan/plan_edit/', plan_edit, name='plan_edit'),
    # path('plan/plan_delete/<int:pk>/', plan_delete, name='plan_delete'),

    # path('users/', users, name='users'),
    # url(r'^users/users_create$', users_create, name='users_create'),
    # url(r'^users/users_save$', users_save, name='users_save'),
    # url(r'^users/users_edit/(?P<id>\d+)$', users_edit, name='users_edit'),
    # url(r'^users/users_edit/users_update/(?P<id>\d+)$', users_update, name='users_update'),
    # url(r'^users/users_delete/(?P<id>\d+)$', users_delete, name='users_delete'),
    #path('users_edit/<int:pk>/', users_edit, name='users_edit'),
    # path('configs/', configs, name='configs'),
]
admin.site.site_header = 'Administracion - Normativa'
if settings.DEBUG == True:
    from django.conf.urls.static import static
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)