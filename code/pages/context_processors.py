from django.conf import settings

def debug(request):
    return dict(debug=settings.DEBUG)

def facebook_application_id(request):
    return dict(facebook_application_id=settings.FACEBOOK_APPLICATION_ID)
