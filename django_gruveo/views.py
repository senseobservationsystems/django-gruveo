from rest_framework import views, status
from rest_framework.response import Response
from django_gruveo.serializers import GruveoTokenSerializer

class GruveoTokenSignerView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = GruveoTokenSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)