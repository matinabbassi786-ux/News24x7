from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import News
from .Serializer import Newsserializers
from rest_framework.views import APIView


@api_view(['GET', 'POST'])
class News_list(APIView):
     def get(self, request, format=None):
        serializer  = Newsserializers(News)
        return Response(serializer.data)
