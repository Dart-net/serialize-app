from collections import OrderedDict
from django.conf.urls import url

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse

from . import views