from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.api import serializers
from apps.api.permissions import IsDiaryOwnerPermission, IsNoteOwnerPermission
from apps.core import models as core_models


class DiaryViewSet(viewsets.ModelViewSet):
    queryset = core_models.Diary.objects.all()
    serializer_class = serializers.DiarySerializer
    permission_classes = [IsAuthenticated, IsDiaryOwnerPermission]
    filterset_fields = "__all__"


class NoteViewSet(viewsets.ModelViewSet):
    queryset = core_models.Note.objects.all()
    serializer_class = serializers.NoteSerializer
    permission_classes = [IsAuthenticated, IsNoteOwnerPermission]
    filterset_fields = "__all__"
