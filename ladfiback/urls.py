from django.contrib import admin
from django.urls import path
from django.urls import path
from django.urls import include

from login import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls'))
]
