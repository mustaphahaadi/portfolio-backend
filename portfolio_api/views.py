from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.mail import send_mail
from django.conf import settings
from urllib.parse import urlparse
import logging

logger = logging.getLogger(__name__)
from .models import Profile, Project, Tool, Experience, Education, Service, Testimonial, Contact, Certification
from .serializers import (
    ProfileSerializer,
    ProjectSerializer, 
    ToolSerializer, 
    ExperienceSerializer, 
    EducationSerializer, 
    ServiceSerializer,
    TestimonialSerializer,
    ContactSerializer,
    CertificationSerializer
)


class ContactViewSet(viewsets.ModelViewSet):
    """Contact form — public can only POST (create). Admin can view all."""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    # Restrict public API to POST only
    http_method_names = ['post', 'head', 'options']

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()
            
            try:
                send_mail(
                    subject=f'New Portfolio Contact: {contact.name}',
                    message=f'Name: {contact.name}\nEmail: {contact.email}\nMessage: {contact.message}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
            except Exception as e:
                # Log the error but don't fail the request
                logger.error("Email sending failed", exc_info=True)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_fields = ['title']
    search_fields = ['title', 'description']
    ordering_fields = ['number', 'title']

class ToolViewSet(viewsets.ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all().order_by('-year')
    serializer_class = ExperienceSerializer
    filterset_fields = ['company', 'position']
    search_fields = ['company', 'position', 'description']
    ordering_fields = ['year', 'company']

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all().order_by('-year')
    serializer_class = EducationSerializer
    filterset_fields = ['institution']
    search_fields = ['institution', 'description']
    ordering_fields = ['year', 'institution']

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filterset_fields = ['title']
    search_fields = ['title', 'description']
    ordering_fields = ['title']

class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    """Testimonials — read-only for public API."""
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all().order_by('-id')
    serializer_class = CertificationSerializer
    filterset_fields = ['organization']
    search_fields = ['name', 'organization']

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    # Only allow GET requests for the public API
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        # Always return the first/only profile directly instead of an array
        instance = Profile.objects.first()
        if not instance:
            return Response(None, status=status.HTTP_200_OK)
        serializer = self.get_serializer(instance)
        data = serializer.data

        def absolute_url(value):
            if not value:
                return None
            parsed = urlparse(value)
            if parsed.scheme and parsed.netloc:
                return value
            if value.startswith('/'):
                return request.build_absolute_uri(value)
            return request.build_absolute_uri(f'/{value}')

        # Prefer URL-based profile picture (free option, no object storage needed).
        # Fallback to uploaded file if URL is not set.
        picture_url = instance.profile_picture_url
        if picture_url:
            data['profile_picture'] = absolute_url(picture_url)
        elif instance.profile_picture:
            data['profile_picture'] = absolute_url(instance.profile_picture.url)

        if instance.resume:
            data['resume'] = absolute_url(instance.resume.url)
        
        return Response(data)