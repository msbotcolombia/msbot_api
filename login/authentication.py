from rest_framework_simplejwt.authentication import JWTAuthentication


class CustomJWTAuthentication(JWTAuthentication):
    def get_header(self, request):
        header = super().get_header(request)
        if header:
            return header.split()[1]
        return None
