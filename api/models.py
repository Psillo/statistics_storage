from django.db import models


class Statistic(models.Model):
    date = models.DateField()
    clicks = models.PositiveIntegerField(
        default=0
    )
    views = models.PositiveIntegerField(
        default=0
    )
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    cpc = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False
    )
    cpm = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False
    )

    class Meta:
        ordering = ["-date"]

    def save(self, *args, **kwargs):
        if self.cost != 0 and self.clicks != 0 and self.views != 0:
            self.cpc = self.cost / self.clicks
            self.cpm = self.cost / self.views * 1000
        else:
            self.cpc = 0
            self.cpm = 0
        super().save(*args, **kwargs)
