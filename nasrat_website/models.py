from django.db import models
from django.utils.text import slugify

class About(models.Model):
    full_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    short_bio = models.CharField(max_length=300)
    location = models.CharField(max_length=255, blank=True, null=True)
    age = models.PositiveIntegerField()
    degree = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    freelance = models.BooleanField(default=True)
    biography = models.TextField()

    def __str__(self):
        return self.full_name


class SocialLink(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='social_links')
    platform = models.CharField(max_length=50)  # e.g., LinkedIn, GitHub, Twitter
    url = models.URLField()

    def __str__(self):
        return f"{self.platform} - {self.about.full_name}"


class Specialty(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='specialties')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Education(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='educations')
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} at {self.institution}"


class WorkExperience(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='work_experiences')
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.company}"


class Skill(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField()  # Proficiency level as a percentage

    def __str__(self):
        return self.name


class Certification(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='certifications')
    name = models.CharField(max_length=255)
    issuing_organization = models.CharField(max_length=255)
    issue_date = models.DateField()

    def __str__(self):
        return self.name


class Resume(models.Model):
    name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    summary = models.TextField()

    def __str__(self):
        return self.name


class ContactDetail(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='contact_details')
    type = models.CharField(max_length=50)  # e.g., email, phone, address
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.type}: {self.value}"


class EducationDetail(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='education_details')
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.degree} at {self.institution}"


class ExperienceDetail(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='experience_details')
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.company}"
    
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    technologies_used = models.TextField()

    def __str__(self):
        return self.title


class PortfolioItem(models.Model):
    CATEGORY_CHOICES = [
        ('app', 'App'),
        ('product', 'Product'),
        ('branding', 'Branding'),
        ('books', 'Books'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='portfolio_items')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='portfolio/')
    detail_link = models.URLField(blank=True, null=True)
    preview_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.project.title
    
    