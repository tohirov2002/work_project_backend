from rest_framework import viewsets

from .models import CommentsModel
from .serializers import CommentSerializers
from .permissions import IsAdminReadOnly
# Create your views here.


class CommentView(viewsets.ModelViewSet):
    queryset = CommentsModel.objects.all()
    serializer_class = CommentSerializers

