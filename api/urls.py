from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views import UserAuthorization

router = routers.DefaultRouter()
router.register(r'auth_user', UserAuthorization, 'auth_user')

urlpatterns = [
    path('user/', include(router.urls)),
    path('docs/', include_docs_urls(title="app api documentation"))
]
