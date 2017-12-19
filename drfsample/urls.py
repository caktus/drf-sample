from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from main import views as main_api


router = routers.DefaultRouter()
router.register(r'thing', main_api.ThingViewSet)

urlpatterns = [
    url(r'^docs/', include_docs_urls(title='My API')),
    url(r'^', include(router.urls)),
]
