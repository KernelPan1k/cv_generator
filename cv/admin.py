from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin

# Register your models here.
from cv.models import Grade, Experience, Technology, Preference, CV


class GradeInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Grade


class ExperienceInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Experience


class TechnologyInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Technology


class PreferenceInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Preference


class CvAdmin(admin.ModelAdmin):
    inlines = (GradeInline, ExperienceInline, TechnologyInline, PreferenceInline)

    fieldsets = (
        (None, {
            'fields': ('full_name', 'address', 'Contact', 'sites')
        }),
        ('Information', {
            'fields': ('information',),
        }),
        ('Knowledge', {
            'fields': ('knowledge',),
        }),
    )


admin.site.register(CV, CvAdmin)
