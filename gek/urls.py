"""gek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles import views

from common.views import MainView, SaveApplication

urlpatterns = [
    url(r'^$', MainView.as_view(), name='main'),
    url(r'^search/[\w-]*$', MainView.as_view(), name='main'),
    url(r'^superadmin/', admin.site.urls),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^common/', include('common.urls', namespace='common')),
    url(r'^admin/', include('admin2.urls', namespace='admin2')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^p24/', include('privat24.urls', namespace='privat24')),
    url(r'^liqpay/', include('liqpayapp.urls', namespace='liqpay')),

    # SITE
    url(r'^articles/', include('articles.urls', namespace='articles')),
    url(r'^services/', include('services.urls', namespace='services')),
    url(r'^objects/', include('rieltor_object.urls', namespace='objects')),
    url(r'^trust/', include('trust.urls', namespace='trust')),
    url(r'^contacts/', include('contact.urls', namespace='contacts')),
    url(r'^video/', include('videos.urls', namespace='videos')),
    url(r'favorites/', include('favorites.urls', namespace='favorites')),
    url(r'plan/', include('plan.urls', namespace='plan')),
    url(r'tests/', include('polls.urls', namespace='polls')),
    url(r'save-application/$', SaveApplication.as_view(), name='save_application'),
    url(r'^', include('landing.urls', namespace='landings')),

]
urlpatterns += [
    url(r'^static/(?P<path>.*)$', views.serve),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
