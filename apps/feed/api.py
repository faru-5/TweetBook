import json

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Tbook

@login_required
def api_add_tbook(request):
    # data = json.loads(request.body);
    print(json.loads(request.body))
    # body = data['body']

    # tbook = Tbook.objects.create(body=body, created_by=request.user)
    
    return JsonResponse({'success':True})

