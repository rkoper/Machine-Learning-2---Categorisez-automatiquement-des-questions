from django.contrib import admin
from django.urls import path, include # new
from .views import contactView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', contactView, name='contact'),
]