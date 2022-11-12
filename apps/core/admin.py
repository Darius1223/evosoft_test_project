from django.contrib import admin

from apps.core.models import Diary, User, Note


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    pass


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
