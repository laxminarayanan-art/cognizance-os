
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('mailsender',include('mailsender.urls')),
    path('admin/', admin.site.urls),
]
