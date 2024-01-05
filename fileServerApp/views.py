from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FileSerializer
from .models import Blog
# Create your views here.


@api_view(['GET', 'POST'])
def index(request):

    if request.method == 'GET':
        obj = Blog.objects.all()
        serializer = FileSerializer(obj, many=True)
        data = serializer.data
        return Response(data)
        pass
    elif request.method == 'POST':
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


