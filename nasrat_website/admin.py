from django.contrib import admin
from .models import (
    About, SocialLink, Specialty, Education, WorkExperience, Skill, Certification,
    Resume, ContactDetail, EducationDetail, ExperienceDetail,
    Project, PortfolioItem
)

# Inline models
class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1

class SpecialtyInline(admin.TabularInline):
    model = Specialty
    extra = 1

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

class WorkExperienceInline(admin.TabularInline):
    model = WorkExperience
    extra = 1

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

class CertificationInline(admin.TabularInline):
    model = Certification
    extra = 1

# ✅ Fix: Define inline models for Resume
class ContactDetailInline(admin.TabularInline):
    model = ContactDetail
    extra = 1

class EducationDetailInline(admin.TabularInline):
    model = EducationDetail
    extra = 1

class ExperienceDetailInline(admin.TabularInline):
    model = ExperienceDetail
    extra = 1

# Admin classes
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'email', 'freelance')
    search_fields = ('full_name', 'title', 'email')
    inlines = [SocialLinkInline, SpecialtyInline, EducationInline, WorkExperienceInline, SkillInline, CertificationInline]

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_title')
    search_fields = ('name', 'job_title')
    inlines = [ContactDetailInline, EducationDetailInline, ExperienceDetailInline]  # ✅ Fixed!

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
    search_fields = ('title', 'technologies_used')
    list_filter = ('start_date', 'end_date')

@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('project', 'category')
    search_fields = ('project__title', 'category')
    list_filter = ('category',)

# Register other models
admin.site.register(SocialLink)
admin.site.register(Specialty)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Skill)
admin.site.register(Certification)
admin.site.register(ContactDetail)
admin.site.register(EducationDetail)
admin.site.register(ExperienceDetail)
