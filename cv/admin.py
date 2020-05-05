from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin

# Register your models here.
from cv.models import Grade, Experience, Technology, Preference, CV


class GradeInline(admin.TabularInline):
    model = Grade
    extra = 0


class ExperienceInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Experience
    extra = 0


class TechnologyInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Technology
    extra = 0


class PreferenceInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Preference
    extra = 0
    max_num = 4


class CvAdmin(admin.ModelAdmin):
    list_display = ("identifier", )
    inlines = (GradeInline, ExperienceInline, TechnologyInline, PreferenceInline)

    fieldsets = (
        (None, {
            'fields': ('identifier', 'full_name', 'address', 'contact',)
        }),
        ('Information', {
            'fields': ('information',),
        }),
        ('Knowledge', {
            'fields': ('knowledge',),
        }),
    )

    class Media:
        js = ['cv/js/ckeditor-sortable.js', ]


admin.site.register(CV, CvAdmin)
