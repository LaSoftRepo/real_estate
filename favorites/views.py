# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
# Create your views here.
from django.template.loader import render_to_string
from django.views.generic import TemplateView

from common.helpers import get_client_ip
from favorites.models import Favorites
from rieltor_object.models import NewBuilding, Building, Ofice, Daily
from seo.mixins import SEOMixin


class FavoritesPage(SEOMixin, TemplateView):
    template_name = 'favorites/favorites.html'

    def get_context_data(self, **kwargs):
        context = super(FavoritesPage, self).get_context_data(**kwargs)
        ip = get_client_ip(self.request)
        context['newbuildings'] = NewBuilding.objects.filter(favorites__ip=ip)
        context['buildings'] = Building.objects.filter(favorites__ip=ip)
        context['ofices'] = Ofice.objects.filter(favorites__ip=ip)
        context['dailys'] = Daily.objects.filter(favorites__ip=ip)
        context['all_objects'] = context['newbuildings'].count() + context['buildings'].count()\
                                 + context['ofices'].count() + context['dailys'].count()
        context['link_objects'] = render_to_string('favorites/link_object.html', {
            'buildings': context['buildings'],
            'ofices': context['ofices'],
            'dailys': context['dailys'],
            'newbuildings': context['newbuildings'],
        })
        return context


def set_favorites(request, content_type, object_id):
    obj = ContentType.objects.get_for_id(content_type).model_class().objects.get(id=object_id)
    favorites, create = Favorites.objects.get_or_create(
        ip=get_client_ip(request)
    )
    if not obj.favorites.filter(ip=favorites.ip).exists():
        obj.favorites.add(favorites)
    else:
        obj.favorites.remove(favorites)
    return HttpResponse('ok')


