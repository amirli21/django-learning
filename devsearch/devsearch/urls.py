from django.contrib import admin
from django.urls import path, include


# just for learning reasons, firstly I will create views here, that's not the best practice and shouldn't be done... Anyways, I will delete them when we are ready to go.





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),

]
