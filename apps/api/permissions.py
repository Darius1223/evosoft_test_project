from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsDiaryOwnerPermission(BasePermission):
    message = "Adding diaries not allowed."

    def has_object_permission(self, request, view, obj) -> bool:  # noqa
        if request.method not in SAFE_METHODS:
            if obj.user != request.user:
                return False
        return True


class IsNoteOwnerPermission(BasePermission):
    message = "Adding notes not allowed."

    def has_object_permission(self, request, view, obj) -> bool:  # noqa
        if request.method not in SAFE_METHODS:
            return obj.diary.user.pk == request.user.pk
        return True
