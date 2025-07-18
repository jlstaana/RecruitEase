from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, ApplicantViewSet, google_sign_in

router = DefaultRouter()
router.register(r'jobs', JobViewSet)
router.register(r'applicants', ApplicantViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('google-sign-in/', google_sign_in, name='google_sign_in'),
]