from django.db import models
from datetime import timedelta
from django.utils.text import slugify


# Create your models here.
class About(models.Model):
    full_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    short_bio = models.CharField(max_length=300)
    location = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField()
    years_of_experience = models.PositiveIntegerField()
    specialties = models.TextField(help_text="Comma-separated skills (e.g. Python, Django, JavaScript)")
    education = models.TextField()
    work_experience = models.TextField()
    programming_languages = models.TextField()
    frameworks = models.TextField()
    tools = models.TextField()
    services = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    certifications = models.TextField(blank=True, null=True)
    projects = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name
    

class Projects(models.Model):
    name = models.CharField(max_length=255, help_text="The name of the project")
    slug = models.SlugField(max_length=255, blank=True, unique=True) 
    description = models.TextField(help_text="A detailed description of the project")
    technology = models.CharField(max_length=255, help_text="Technologies used in the project")
    start_date = models.DateField(help_text="Start date of the project")
    end_date = models.DateField(help_text="End date of the project", null=True, blank=True)
    role = models.CharField(max_length=255, help_text="Your role in the project")
    team_size = models.IntegerField(help_text="Number of people in the team", null=True, blank=True)
    project_url = models.URLField(help_text="URL to the project (if available)", null=True, blank=True)
    github_url = models.URLField(help_text="URL to the GitHub repository (if available)", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the project was added")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the project was last updated")


    def save(self, *args, **kwargs):
        if not self.slug:  # if slug is empty, generate from name
            self.slug = slugify(self.name)
        super(Projects, self).save(*args, **kwargs)


    @property
    def duration(self):
        """
        Calculate the duration of the project based on start_date and end_date.
        Returns a string representation of the duration (e.g., "3 months").
        """
        if self.start_date and self.end_date:
            delta = self.end_date - self.start_date
            days = delta.days
            months = days // 30  # Approximate months
            years = days // 365  # Approximate years

            if years > 0:
                return f"{years} year{'s' if years > 1 else ''}"
            elif months > 0:
                return f"{months} month{'s' if months > 1 else ''}"
            else:
                return f"{days} day{'s' if days > 1 else ''}"
        elif self.start_date:
            return "Ongoing"
        else:
            return "Not specified"

    def __str__(self):
        return self.name
    

class Portfolio(models.Model):
    # Connection to About and Projects models
    about = models.OneToOneField(About, on_delete=models.CASCADE, related_name='portfolio')
    projects = models.ManyToManyField(Projects, related_name='portfolios', blank=True)

    # Portfolio Metadata
    title = models.CharField(max_length=255, help_text="Title of your portfolio (e.g., 'My Professional Portfolio')")
    slug = models.SlugField(max_length=255, blank=True, unique=True, help_text="A URL-friendly version of the title")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the portfolio was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the portfolio was last updated")

    # Skills and Expertise (can be derived from About or added separately)
    skills = models.TextField(help_text="Comma-separated list of skills (e.g., Python, Django, JavaScript)")
    programming_languages = models.TextField(help_text="Comma-separated list of programming languages you know")
    frameworks = models.TextField(help_text="Comma-separated list of frameworks you are proficient in")
    tools = models.TextField(help_text="Comma-separated list of tools you use")

    # Achievements and Certifications
    certifications = models.TextField(help_text="List of certifications (e.g., AWS Certified, Python Institute)", blank=True, null=True)
    achievements = models.TextField(help_text="Notable achievements or awards", blank=True, null=True)

    # Contact Information

    linkedin = models.URLField(blank=True, null=True, help_text="Your LinkedIn profile URL")
    github = models.URLField(blank=True, null=True, help_text="Your GitHub profile URL")
    twitter = models.URLField(blank=True, null=True, help_text="Your Twitter profile URL")

    # Personal Statement or Summary
    personal_statement = models.TextField(help_text="A brief summary of your professional journey and goals", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    


    
class Services(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the service (e.g., Web Development, Mobile App Development)")
    slug = models.SlugField(max_length=255, unique=True, blank=True, help_text="A URL-friendly version of the service name")
    icon = models.CharField(max_length=100, help_text="Icon class for the service (e.g., 'fas fa-code' for Font Awesome)", blank=True, null=True)
    short_description = models.CharField(max_length=255, help_text="A short description of the service (e.g., 'Build responsive and modern websites')")
    detailed_description = models.TextField(help_text="A detailed description of the service", blank=True, null=True)

    # Additional Metadata
    is_featured = models.BooleanField(default=False, help_text="Mark this service as featured to highlight it on your portfolio")
    order = models.PositiveIntegerField(default=0, help_text="Order in which the service will appear on the portfolio (lower numbers appear first)")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the service was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the service was last updated")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Services, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    

    
