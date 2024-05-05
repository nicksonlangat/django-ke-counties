import uuid

from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = [
            "-updated_at",
        ]


class County(BaseModel):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name_plural = "Counties"


class SubCounty(BaseModel):
    county = models.ForeignKey(
        County,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="subcounties",
    )
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name_plural = "Sub Counties"
        unique_together = (("county", "name"),)


class Ward(BaseModel):
    sub_county = models.ForeignKey(
        SubCounty,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="wards",
    )
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        unique_together = (("sub_county", "name"),)
