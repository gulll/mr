from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    (r'^movies/',include('moview.urls')),
    # url(r'^$', 'moviewreview.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$','moviewreview.views.login'),
    url(r'^accounts/logout/$','moviewreview.views.logout'),
    url(r'^accounts/auth/$','moviewreview.views.auth_view'),
    url(r'^accounts/loggedin/$','moviewreview.views.loggedin'),
    url(r'^accounts/invalid/$','moviewreview.views.invalid_login'),
    url(r'^accounts/register/$','moviewreview.views.register_user'),
    url(r'^accounts/register_success/$','moviewreview.views.register_success'),
    
    
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
