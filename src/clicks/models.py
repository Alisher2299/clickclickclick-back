from django.db import models

from clicks.utils import get_location_info


class UserClick(models.Model):
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=200, unique=True)
    latitude = models.DecimalField(max_digits=16, decimal_places=13)
    longitude = models.DecimalField(max_digits=16, decimal_places=13)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200, blank=True, null=True)
    click_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.country:
            country, city = get_location_info(float(self.latitude), float(self.longitude))
            self.country = country
            self.city = city

            country_statistic, created = CountryStatistic.objects.get_or_create(country=self.country)
            country_statistic.click_count += self.click_count
            country_statistic.save()

        super().save(*args, **kwargs)


class CountryStatistic(models.Model):
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    country = models.CharField(max_length=200, unique=True)
    click_count = models.PositiveBigIntegerField(default=0)
