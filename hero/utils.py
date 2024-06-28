from django.core.cache import cache

'''
TODO:
    - Connect to kafka producer an consumer
'''
class CacheHelper:
    """
    A utility class for managing cache operations.
    This class provides methods to interact with Django's cache framework,
    allowing for the retrieval, setting, and deletion of cached data.
    """
    @staticmethod
    def get_cache_key(title_id):
        """
        Generate a cache key for a given title ID.

        Parameters:
        - `title_id` (str): The unique identifier for the title.

        Returns:
        - `str`: A formatted string that serves as a unique cache key.
        """
        return f"title_{title_id}"

    @staticmethod
    def get_from_cache(title_id):
        """
        Retrieve data from the cache using the title ID.

        Parameters:
        - `title_id` (str): The unique identifier for the title.

        Returns:
        - `dict`: The cached data if present, otherwise None.
        """
        cache_key = CacheHelper.get_cache_key(title_id)
        return cache.get(cache_key)

    @staticmethod
    def set_to_cache(title_id, data):
        """
        Store data in the cache associated with the title ID.

        Parameters:
        - `title_id` (str): The unique identifier for the title.
        - `data` (dict): The data to be cached.

        Returns:
        - None
        """
        cache_key = CacheHelper.get_cache_key(title_id)
        cache.set(cache_key, data)

    @staticmethod
    def delete_from_cache(title_id):
        """
        Delete the cached data associated with the title ID.

        Parameters:
        - `title_id` (str): The unique identifier for the title.

        Returns:
        - None
        """
        cache_key = CacheHelper.get_cache_key(title_id)
        cache.delete(cache_key)
