from rest_framework.throttling import UserRateThrottle

class tencallsperminute(UserRateThrottle):
    scope = 'ten' # this line will be added in the settings.py file for configuring this class as a throttle class
    