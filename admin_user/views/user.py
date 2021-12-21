from rest_framework.response import Response
from rest_framework import status, generics


class SignUp(generics.CreateAPIView):
# Override authentication/permission classes so that I don't need any permission to access this
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        print('yay')
        return Response({})