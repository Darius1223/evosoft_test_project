from rest_framework import routers

from apps.api import viewsets

router = routers.DefaultRouter()
router.register(r"diaries", viewsets.DiaryViewSet)
router.register(r"notes", viewsets.NoteViewSet)
