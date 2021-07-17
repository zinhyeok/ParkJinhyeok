from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    # +=인거 주의!!
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
