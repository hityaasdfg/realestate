"""project URL Configuration

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
from django.urls import path , include
from home import views
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from employee import views  

from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()
urlpatterns = [



    
    path('addproperty/', views.emp),  
    path('admin/', admin.site.urls),
    path('', include('home.urls' , namespace='home')),
    path('property/', include('property.urls' , namespace='property')),
    path('agents/', include('agents.urls' , namespace='agents')),
    path('about/', include('about.urls' , namespace='about')),
    path('contact/', include('contact.urls' , namespace='contact')),
    path('signup/', accounts_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('reset/',
    auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'
    ),
    name='password_reset'),

    path('reset/done/',
    auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
    name='password_reset_done'),
    path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
    auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
    name='password_reset_confirm'),

    path('reset/complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
    name='password_reset_complete'),


    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
    name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
    name='password_change_done'),

]


urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Property RESERVATION ADMIN"
admin.site.site_title = "Property RESERVATION ADMIN"
admin.site.site_index_title = "Welcome To Property Reservation Admin"