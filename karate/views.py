from django.shortcuts import render
import json


def json_fields(request):

    fields = None

    if request.method == 'POST':
        fields = request.POST['content']

    return render(request, 'karate/json_fields.html', {'fields': fields})
