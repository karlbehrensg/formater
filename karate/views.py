from django.shortcuts import render


def json_fields(request, json_origin=None):
    fields = json_origin
    return render(request, 'karate/json_fields.html', {'fields': fields})
