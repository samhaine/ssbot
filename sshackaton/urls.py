"""sshackaton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from plugin_base.plugin import get_handler
from foosball_plugin.plugin import FoosballPlugin
from autofeed_plugin.plugin import AutofeedPlugin
from compintel_plugin.plugin import CompintelPlugin

urlpatterns = [
    url(r'^ssbot/', include('ssbot.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^foosball/handleMessage/$', get_handler(FoosballPlugin)),
    url(r'^autofeed/handleMessage/$', get_handler(AutofeedPlugin)),
    url(r'^compintel/handleMessage/$', get_handler(CompintelPlugin))
]
