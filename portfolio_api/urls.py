from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'profile', views.ProfileViewSet, basename='profile')
router.register(r'projects', views.ProjectViewSet)
router.register(r'tools', views.ToolViewSet)
router.register(r'experiences', views.ExperienceViewSet)
router.register(r'education', views.EducationViewSet)
router.register(r'services', views.ServiceViewSet)
router.register(r'testimonials', views.TestimonialViewSet)
router.register(r'contact', views.ContactViewSet)
router.register(r'certifications', views.CertificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]