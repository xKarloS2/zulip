from django.conf.urls import patterns, url

i18n_urlpatterns = patterns('',
    url(r'^json/approve_transfer$', 'approved_transfer.views.approve_transfer'),
)

urlpatterns = patterns('', *i18n_urlpatterns)
