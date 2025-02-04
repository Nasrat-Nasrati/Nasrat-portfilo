from django.contrib import admin
from django.utils.html import format_html
from .models import About,Projects,Portfolio,Services,Contact

class AdminAbout(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'photo_preview', 'email', 'years_of_experience', 'location')
    search_fields = ('full_name', 'title', 'email', 'location', 'specialties')
    list_filter = ('years_of_experience', 'location', 'services')
    ordering = ('full_name',)

    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'title', 'photo', 'short_bio', 'location')
        }),
        ('Professional Summary', {
            'fields': ('bio', 'years_of_experience', 'specialties')
        }),
        ('Education & Experience', {
            'fields': ('education', 'work_experience')
        }),
        ('Skills & Technologies', {
            'fields': ('programming_languages', 'frameworks', 'tools')
        }),
        ('Services', {
            'fields': ('services',)
        }),
        ('Contact & Social Links', {
            'fields': ('email', 'phone_number', 'linkedin', 'github', 'twitter')
        }),
        ('Achievements & Projects', {
            'fields': ('certifications', 'projects')
        }),
    )

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:5px;"/>', obj.photo.url)
        return "No Image"

    photo_preview.short_description = "Profile Photo"

# Register the model
admin.site.register(About, AdminAbout)



class AdminProject(admin.ModelAdmin):
    list_display = ('name','slug','technology','start_date','end_date','role')
    search_fields =('name','slug','technology','role')
    list_filter =('name','slug','technology','role')
    ordering =('slug',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Projects,AdminProject)



class AdminPortfolio(admin.ModelAdmin):
    list_display = ('title', 'slug', 'about', 'created_at', 'updated_at', 'github')
    search_fields = ('title', 'slug', 'about__full_name', 'skills', 'programming_languages', 'frameworks')
    list_filter = ('created_at', 'updated_at', 'skills', 'programming_languages', 'frameworks')
    ordering = ('-created_at',)  # Order by latest created portfolio first
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('projects',)  # Enable better project selection in admin
    readonly_fields = ('created_at', 'updated_at')  # Prevent modification of timestamps

admin.site.register(Portfolio, AdminPortfolio)



class AdminServices(admin.ModelAdmin):
    list_display = ("name", "icon_display", "is_featured", "order", "created_at")
    list_filter = ("is_featured", "created_at")
    search_fields = ("name", "short_description", "detailed_description")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("order", "name")

    def icon_display(self, obj):
        """Displays the icon in the admin panel if using FontAwesome."""
        if obj.icon:
            return format_html(f'<i class="{obj.icon}"></i> {obj.icon}')
        return "-"
    
    icon_display.short_description = "Icon Preview"

admin.site.register(Services,AdminServices)



class AdminContact(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone')
    list_filter = ('full_name',)
    search_fields = ('full_name', 'email', 'phone')
    readonly_fields = ('created_at', 'updated_at')  # These fields are now valid

admin.site.register(Contact, AdminContact)