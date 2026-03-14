from django.contrib import admin
from .models import Profile, Project, Tool, Experience, Education, Service, Testimonial, Contact, Certification


class ProfileAdmin(admin.ModelAdmin):
    """Singleton profile — disable add if one exists, disable delete."""
    def has_add_permission(self, request):
        if Profile.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


class ContactAdmin(admin.ModelAdmin):
    """Read-only view of contact form submissions."""
    list_display = ('name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'message', 'created_at')
    ordering = ('-created_at',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'created_at')
    search_fields = ('name', 'position', 'text')
    ordering = ('-created_at',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('number', 'title')
    search_fields = ('title', 'description')


class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'status')
    list_filter = ('status',)
    search_fields = ('name',)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'year')
    search_fields = ('position', 'company')


class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'issue_date')
    search_fields = ('name', 'organization')

# Register models
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Tool, ToolAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education)
admin.site.register(Service)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Certification, CertificationAdmin)
