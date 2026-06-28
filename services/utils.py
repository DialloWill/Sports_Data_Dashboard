from datetime import datetime, timedelta

def is_cache_valid(cache, hours=1):
    # Returns True if cache has data and is less than `hours` old
    return (
        cache["data"] is not None and
        cache["timestamp"] is not None and
        datetime.now() - cache["timestamp"] < timedelta(hours=hours)
    )