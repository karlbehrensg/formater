from django.shortcuts import render
import json


def json_fields(request):

    fields = None

    if request.method == 'POST' and request.POST['content']:
        fields = request.POST['content']
        fields = json.loads(fields)

    return render(request, 'karate/json_fields.html', {'fields': fields})
