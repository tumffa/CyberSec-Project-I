from django.urls import path
from .views import homePageView, registerView, postMessageView


urlpatterns = [
    path('', homePageView, name='home'),
    path('register/', registerView, name='register'),
    path('postmessage', postMessageView, name='post')
]
