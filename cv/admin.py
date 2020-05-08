from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin

# Register your models here.
from cv.models import Grade, Experience, Technology, Preference, CV


def duplicate_cv(modeladmin, request, queryset):
    foreign_klass = [Experience, Grade, Preference, Technology]
    for obj in queryset:
        old_id = obj.id
        obj.id = None
        obj.identifier = "%s (copy)" % obj.identifier
        obj.save()

        for foreign in foreign_klass:
            for foreign_obj in foreign.objects.filter(cv=old_id):
                foreign_obj.id = None
                foreign_obj.cv = obj
                foreign_obj.save()


duplicate_cv.short_description = "Duplicate cv"


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
    list_display = ("identifier",)
    inlines = (GradeInline, ExperienceInline, TechnologyInline, PreferenceInline)
    actions = [duplicate_cv]

    fieldsets = (
        (None, {
            'fields': ('identifier', 'full_name', 'address', 'contact', 'hobby', 'color')
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
