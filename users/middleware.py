from .models import User
from django.http import JsonResponse


class UserIdMiddleware:
    """
    Middleware para agregar el usuario correspondiente a user_id en la solicitud.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_id = request.headers.get('user_id')
        print(request.headers)
        print("Por aqui pase", user_id)

        if user_id:
            try:
                user = User.objects.get(id=user_id)
                request.user_from_id = user
            except User.DoesNotExist:
                return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
        else:
            request.user_from_id = None

        return self.get_response(request)