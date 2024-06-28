from rest_framework import status, generics
from rest_framework.response import Response
from django.core.cache import cache
from hero.models import Titles
from hero.serializers import TitlesSerializer
from .utils import CacheHelper


# Create your views here.

class HeroDetail(generics.GenericAPIView):
    """
    View for retrieving, updating, or deleting a title instance.
    """
    def get(self, request, *args, **kwargs):
        """
        Retrieve a title instance by its ID.
        If the data is cached, it is served from the cache to improve performance.
        Otherwise, it is fetched from the database and then cached for future requests.
        """
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
        """
        Update a title instance.
        The updated information is also cached to ensure consistency.
        """
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
        """
        Delete a title instance.
        The corresponding cache entry is also deleted to maintain cache integrity.
        """
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
    """
    View for creating a new title instance.
    After creation, the new title is also added to the cache.
    """
    def post(self, request, *args, **kwargs):
        """
        Create a new title instance.
        The new entry is immediately cached for quick access.
        """
        serializer = TitlesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            title_id = serializer.data['tconst']
            CacheHelper.set_to_cache(title_id, serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)