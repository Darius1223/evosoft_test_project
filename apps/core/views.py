from django.http import JsonResponse, HttpRequest


def health_check(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"health": "ok"})
