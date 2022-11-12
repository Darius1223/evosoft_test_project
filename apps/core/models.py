from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from loguru import logger


class KindChoices(models.TextChoices):
    PUBLIC = "PB", _("Public")
    PRIVATE = "PR", _("Private")


class Diary(models.Model):
    """Дневник"""

    title = models.CharField(verbose_name="Название дневника", max_length=200)
    expiration = models.DateField(
        verbose_name="Срок блокировки дневника",
        help_text="Дата, после которой можно удалить дневник",
        blank=True,
        null=True,
    )
    kind = models.CharField(verbose_name="Тип дневника", max_length=2, choices=KindChoices.choices)
    user = models.ForeignKey(verbose_name="Пользователь", to="User", on_delete=models.CASCADE)

    def clean(self) -> None:
        if self.kind != KindChoices.PRIVATE.value:
            logger.debug("Diary must me have private mode to save expiration field.")
            raise ValidationError(
                "Поле 'Срок блокировки дневника' быть назначена только у private дневников",
            )
        super().clean()

    def __str__(self) -> str:
        return f"Дневник '{self.title}' [#{self.pk}]"

    class Meta:
        verbose_name = "Дневник"
        verbose_name_plural = "Дневники"


class Note(models.Model):
    """Страница дневника"""

    text = models.TextField(verbose_name="Текст")
    diary = models.ForeignKey(to=Diary, verbose_name="Дневник", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Страница [#{self.pk}]"

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"


class User(AbstractUser):
    """Пользователь (владелец) дневника)"""

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
