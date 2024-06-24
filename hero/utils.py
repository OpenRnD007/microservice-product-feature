from django.core.cache import cache

'''
TODO:
    - Connect to kafka producer an consumer
'''
class CacheHelper:
    @staticmethod
    def get_cache_key(title_id):
        return f"title_{title_id}"

    @staticmethod
    def get_from_cache(title_id):
        cache_key = CacheHelper.get_cache_key(title_id)
        return cache.get(cache_key)

    @staticmethod
    def set_to_cache(title_id, data):
        cache_key = CacheHelper.get_cache_key(title_id)
        cache.set(cache_key, data)

    @staticmethod
    def delete_from_cache(title_id):
        cache_key = CacheHelper.get_cache_key(title_id)
        cache.delete(cache_key)
