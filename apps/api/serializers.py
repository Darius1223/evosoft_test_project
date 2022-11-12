from rest_framework import serializers
from apps.core import models as core_models


class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = core_models.Diary
        fields = (
            "id",
            "title",
            "expiration",
            "kind",
            "user",
        )
        read_only_fields = ("user",)

    def save(self, **kwargs):
        request = self.context.get("request")
        if request:
            kwargs.update({"user": request.user})
        super().save(**kwargs)


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = core_models.Note
        fields = ("text", "diary")
