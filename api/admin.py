from django.contrib import admin

from .models import Statistic


class StatisticAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Statistic._meta.get_fields()
    ]


admin.site.register(Statistic, StatisticAdmin)
