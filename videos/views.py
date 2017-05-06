# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from common.mixins import ViewsCountMixin
from videos.models import Videos


class VideosList(ListView):
    model = Videos
    template_name = 'videos/video_list.html'


class VideosDetail(ViewsCountMixin, DetailView):
    model = Videos
    template_name = 'videos/video_detail.html'
    pk_url_kwarg = 'pk'