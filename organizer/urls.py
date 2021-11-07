from django.contrib import admin
from django.contrib.auth import urls as auth_urls
from django.urls import path, include
from todo import views as todo_views

urlpatterns = [
    path('', todo_views.index, name='tasks'),
    path('remove/<int:task_id>', todo_views.remove_task, name='remove'),
    path('admin/', admin.site.urls),
    path('', include(auth_urls)),
]
