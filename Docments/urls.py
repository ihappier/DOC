# __author__ = 'ihappier'
from django.conf.urls import url
from Docments import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<doc_no>\d+)/$', views.doc, name='doc_no'),
    url(r'^list/', views.category, name='category'),
    url(r'^about/', views.about,name='about'),
]

# if settings.DEBUG:
#     urlpatterns = urlpatterns + patterns(
#         'django.views.static',
#         (r'^media/(?P<path>.*)',
#         'serve',
#         {'document_root': settings.MEDIA_ROOT}), )
