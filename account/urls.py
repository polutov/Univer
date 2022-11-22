from django.urls import path
from .views import *

urlpatterns = [
    path('signup', signup),
    path('email_confirm', email_confirm),
    path('signin', signin),
    path('signout', signout),
    path('profile', profile),
    path('pass_reset', pass_reset),
]