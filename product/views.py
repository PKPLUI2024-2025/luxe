from decimal import Decimal
import json
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.utils.html import strip_tags
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse

def show_product_page(request):
    user = request.user

    context = {
        'user': user,
    }

    return render(request, "product_page.html", context)