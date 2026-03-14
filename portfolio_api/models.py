from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100, default="Mustapha Haadi Bugnaba")
    roles = models.JSONField(help_text="Provide a list of roles, e.g. [\"Software Developer\", \"Problem Solver\"]", default=list)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Profile"

class Project(models.Model):
    number = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50)
    github_url = models.URLField(blank=True, null=True, help_text="GitHub repository URL")
    live_url = models.URLField(blank=True, null=True, help_text="Live demo URL")

    def __str__(self):
        return self.title

class Tool(models.Model):
    STATUS_CHOICES = [
        ('expert', 'Expert'),
        ('proficient', 'Proficient'),
        ('learning', 'Learning'),
        ('installed', 'Installed'),
    ]
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    version = models.CharField(max_length=30, blank=True, default="latest", help_text="Version e.g. 24.0.7")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='proficient', help_text="Proficiency level")

    def __str__(self):
        return self.name

class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    year = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.position} at {self.company}"

class Education(models.Model):
    year = models.CharField(max_length=50)
    institution = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.institution

class Service(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=200)
    text = models.TextField()
    avatar = models.URLField(blank=True, null=True, help_text="URL to avatar image")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Testimonial from {self.name}"

    class Meta:
        ordering = ['-created_at']

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

    class Meta:
        ordering = ['-created_at']

class Certification(models.Model):
    name = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    issue_date = models.CharField(max_length=50, blank=True, null=True, help_text="e.g., Aug 2023")
    expiration_date = models.CharField(max_length=50, blank=True, null=True, help_text="e.g., Aug 2026 or No expiration")
    credential_id = models.CharField(max_length=100, blank=True, null=True)
    credential_url = models.URLField(blank=True, null=True, help_text="URL to credential verification")
    icon = models.CharField(max_length=50, default="fas fa-certificate", help_text="FontAwesome icon class")

    def __str__(self):
        return f"{self.name} by {self.organization}"
