from django.contrib import admin
from django.urls import include, path
from polls.nocodb_utils import get_nocodb_data
urlpatterns = [
    path('nocodb-data/', get_nocodb_data, name='nocodb_data'),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]

