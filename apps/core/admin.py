from django.contrib import admin

from apps.core.models import Diary, User, Note


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    pass
