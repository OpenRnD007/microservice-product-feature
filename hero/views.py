from rest_framework import status, generics
from rest_framework.response import Response
from django.core.cache import cache
from hero.models import Titles
from hero.serializers import TitlesSerializer
from .utils import CacheHelper


# Create your views here.

class HeroDetail(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        title_id = kwargs.get('id', None)
        if title_id is not None:
            # Check if the data is in the cache
            cached_title = CacheHelper.get_from_cache(title_id)

            if cached_title is not None:
                # If cache data exists, serve it
                print('Served from Cache')
                return Response(cached_title)
            else:
                # If not in cache, fetch from database
                try:
                    title = Titles.objects.get(tconst=title_id)
                    serializer = TitlesSerializer(title)
                    # Store the data in the cache for next time
                    CacheHelper.set_to_cache(title_id, serializer.data)
                    print('Served from DB')
                    return Response(serializer.data)
                except Titles.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, *args, **kwargs):
        title_id = kwargs.get('id', None)
        if title_id is not None:
            try:
                title = Titles.objects.get(tconst=title_id)
                serializer = TitlesSerializer(title, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    CacheHelper.set_to_cache(title_id, serializer.data)
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Titles.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, *args, **kwargs):
        title_id = kwargs.get('id', None)
        if title_id is not None:
            try:
                title = Titles.objects.get(tconst=title_id)
                title.delete()
                CacheHelper.delete_from_cache(title_id)
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Titles.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class HeroAdd(generics.GenericAPIView):

    def post(self, request, *args, **kwargs):
        serializer = TitlesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            title_id = serializer.data['tconst']
            CacheHelper.set_to_cache(title_id, serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)