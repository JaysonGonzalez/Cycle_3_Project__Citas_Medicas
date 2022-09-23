from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from c3pAPP.serializers.historial_signosSerializer import POSThistorial_signosSerializer


class Historial_SignosCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = POSThistorial_signosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        #Se comenta la validacion para no ingresar username ni password en el POST
        '''tokenData = {"username": request.data["username"],
                     "password": request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)'''
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)