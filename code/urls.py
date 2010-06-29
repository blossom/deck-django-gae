from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'pages.views.home'),

    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)
