from django.shortcuts import render
import json


def take_fields(data):
    fields = []
    for key in data:
        if type(data[key]) == list and type(data[key][0]) == dict:
            list_father = [key]
            for item in data[key]:
                list_father.append(take_fields(item))
            fields.append(list_father)
        else:
            fields.append([key])
    return fields


def json_fields(request):

    fields = None

    if request.method == 'POST' and request.POST['content']:
        fields = request.POST['content']
        fields = json.loads(fields)
        fields = take_fields(fields)

    return render(request, 'karate/json_fields.html', {'fields': fields})
