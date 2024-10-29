config = {
    'language' : 'kz',
    'timezone': 'UTC'
}
def get_config (key):
    def inner():
        return config.get(key)
    return inner

get_language = get_config('language')
print(get_language())
get_timezone = get_config('timezone')
print(get_timezone())