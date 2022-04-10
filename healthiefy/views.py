from asyncio.windows_events import NULL
from pyexpat import model
from wsgiref.util import request_uri
from xml.etree.ElementTree import tostring
from django.shortcuts import redirect, render
from django.http import HttpResponse
import pickle
import prediction
import numpy as np;
#views
