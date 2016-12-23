from django.conf.urls import url

from zillow_scraper_emailer_app.views import HomePageView

urlpatterns = [

    url(r'^$', HomePageView.as_view(), name='home')
]
