from django.urls import path
from django.urls import include
urlpatterns = [
    # existing url patterns
    path('', include('base.urls')),
]
