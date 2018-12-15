"""RedInvestigadores URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path, include
from core import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from core.forms import LoginForm, CustomUserCreationForm

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('about_of/', views.about_of, name='about_of'),
    path('accounts/', include('allauth.urls')),
    path('actualizar/grupo/<int:group_id>',views.group_changes, name='group_change'),
    path('actualizar/proyecto/<int:grant_id>', views.grant_changes, name='grant_change'),
    path('actualizar/publicacion/<int:publication_id>', views.publication_changes, name='publication_change'),
    path('agregar/estudiante', views.get_student_petition, name='student_petition'),
    path('agregar/tutor', views.get_tutor_petition, name='tutor_petition'),
    path('admin/', admin.site.urls),
    path('crear/articulo', views.get_publication_petition, name='publication_petition'),
    path('crear/grupo', views.get_group_petition, name='group_petition'),
    path('crear/proyecto', views.get_grant_petition, name='grant_petition'),
    path('crear/sede', views.get_affiliation_petition, name='affiliation_petition'),
    path('estados/<int:state_id>', views.get_state_info, name='estado'),
    path('estados/<int:state_id>/sedes/<int:affiliation_id>', views.get_state_affiliation_info, name='estado/sede'),
    path('<int:publication_id>/eliminar/articulo/', views.DeletePublication.as_view(),name='delete_publication'),
    path('<int:author_id>/<int:publication_id>/eliminar/autor/', views.DeleteAuthor.as_view(),name='delete_authors'),
    path('<int:group_id>/eliminar/grupo/', views.DeleteGroup.as_view(),name='delete_group'),
    path('<int:member_id>/<int:group_id>/eliminar/miembro/', views.DeleteMember.as_view(),name='delete_members'),
    path('<int:participant_id>/<int:grant_id>/eliminar/participante/', views.DeleteParticipant.as_view(),name='delete_participant'),
    path('<int:grant_id>/eliminar/proyecto/', views.DeleteGrant.as_view(),name='delete_grant'),
    path('<int:tutor_id>/<int:user_id>/eliminar/tutor/', views.DeleteTutor.as_view(),name='delete_tutor'),
    path('<int:student_id>/<int:user_id>/eliminar/estudiante/', views.DeleteStudent.as_view(),name='delete_student'),
    path('grupo/<int:group_id>', views.get_group, name='group'),
    path('home/', views.home, name='home'),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html',
        authentication_form=LoginForm), name='login'),
    path('profile/<int:user_id>', views.get_user_profile, name='profile'),
    path('profile', views.get_user_profile_without_id, name='profile'),
    path('proyecto/<int:grant_id>', views.get_grant, name='grant'),
    path('publicacion/<int:publication_id>', views.get_publication, name='publication'),
    path('research/',views.profile_changes, name='research'),
    path('search_view/', views.search_view, name='search_view'),
    path('search_view/search', views.search, name='search'),
    path('signup/', views.signup, name='signup'),
    path('sedes/', views.get_affiliations, name='sedes'),
    path('sedes/<int:affiliation_id>', views.get_affiliation, name='sede'),
    path('signup/core/account_activation_sent/',views.account_activation_sent, name='account_activation_sent'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
