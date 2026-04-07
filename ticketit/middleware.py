from django.shortcuts import redirect
from django.urls import reverse

class AuthRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of paths that don't require authentication
        public_paths = [
            reverse('login'),
            reverse('register'),
            reverse('home'),
            reverse('movie_list'),
            # reverse('movie_detail', args=[1]),  # This will be handled in the view
        ]

        # Allow all /admin/ URLs and media files to bypass authentication
        if request.path.startswith('/admin/') or request.path.startswith('/media/'):
            return self.get_response(request)

        # Check if the current path requires authentication
        if not request.user.is_authenticated and request.path not in public_paths:
            return redirect('login')

        response = self.get_response(request)
        return response 