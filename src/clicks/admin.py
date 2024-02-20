from django.contrib import admin

from clicks.models import UserClick, CountryStatistic


@admin.register(UserClick)
class UserClickAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "country",
        "city",
        "click_count",
    )


@admin.register(CountryStatistic)
class CountryStatisticAdmin(admin.ModelAdmin):
    list_display = (
        "country",
        "click_count",
    )
