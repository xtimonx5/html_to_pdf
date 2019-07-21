from django.urls import path, include
from rest_framework import routers
from .views import GeneratePdfApiView, IndexView

urlpatterns = [
    path(r'', IndexView.as_view()),
    path(r'gen_pdf', GeneratePdfApiView.as_view({
        # 'get': 'get',
        'post': 'post'
    })),
]
