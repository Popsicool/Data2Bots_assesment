from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('business.urls')),
    path('', include('django.contrib.auth.urls')),
    path('account', include('authz.urls')),
]

'''i created two separate applications for this test project
(1) authz: this handles all form of user authentication into the web pplication
(2)business: this application is where other activities outside authentication is being carried out

'''

'''handle404 to render custom error pages for pages not found
handle500 to render custom error page for case of server error'''

handler404 = 'business.views.error_404'
handler500 = 'business.views.error_500'