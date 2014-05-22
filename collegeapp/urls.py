from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from collegeapp import views

urlpatterns = patterns('',
    url(r'^$', views.UrlHandlers().collegeadmin, name='collegeadmin')
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()