from functools import wraps
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

def custom_auth_required(user_types=None, allow_owner_only=False):
    """
    A decorator to enforce authentication and authorization based on user type.
    :param user_types: List of allowed user types (e.g., ['author']).
    :param allow_owner_only: If True, only the owner of the object can access it.
    """
    if user_types is None:
        user_types = []

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(view, request, *args, **kwargs):
            # Authenticate the user
            auth = TokenAuthentication()
            try:
                user, _ = auth.authenticate(request)
                request.user = user
            except AuthenticationFailed:
                return JsonResponse({"detail": "Authentication failed"}, status=401)

            # Check user type
            if user.user_type not in user_types:
                return JsonResponse(
                    {"detail": "You do not have permission to perform this action."},
                    status=403,
                )

            # If user type is 'author', check if 'is_permitted' is True
            if user.user_type == 'author' and not user.is_permitted:
                return JsonResponse(
                    {"detail": "You are not permitted to perform this action."},
                    status=403,
                )

            # If owner-only access is enabled, check ownership
            if allow_owner_only:
                obj = view.get_object()
                if obj.blogger != user:
                    return JsonResponse(
                        {"detail": "You are not allowed to modify this blog."},
                        status=403,
                    )

            return view_func(view, request, *args, **kwargs)

        return _wrapped_view

    return decorator
