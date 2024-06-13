from django.contrib import admin
from django.urls import path, include

# playground/hello
urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls'))
]
