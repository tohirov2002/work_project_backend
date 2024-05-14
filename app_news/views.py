from rest_framework import viewsets
from time import time

from .models import NewsModel
from .serializers import NewsSerializers
from .permissions import IsAdminReadOnly
# Create your views here.


class NewsView(viewsets.ModelViewSet):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializers

    def retrieve(self, request, pk=None, *args, **kwargs):
        title = f"news_{pk}"
        if title in request.COOKIES:
            if time() - float(request.COOKIES[title]) > 10:
                up = True
            else:
                up = True
        else:
            up = True
        if up:
            doc = NewsModel.objects.get(pk=pk).views
            NewsModel.objects.filter(pk=pk).update(views=doc+1)
        response = super().retrieve(request, pk, *args, **kwargs)
        response.set_cookie(title, time())
        return response



    # def retrieve(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk')  # pk ni kwargs orqali olish
    #     title = f"news_{pk}"
    #     if title in request.COOKIES:
    #         if time() - float(request.COOKIES[title]) > 10:
    #             up = True
    #         else:
    #             up = True
    #     else:
    #         up = True
    #         if up:
    #             doc = NewsModel.objects.get(pk=pk).views
    #             NewsModel.objects.filter(pk=pk).update(views=doc + 1)  # update not updatae
    #         response = super().retrieve(request, *args, **kwargs)  # pk ni ham o'zgaruvchilar orasiga qo'shing
    #         response.set_cookie(title, time())
    #         return response
