from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
     url(r'^all/$', 'moview.views.movies'),
     url(r'^get/(?P<movie_id>\d+)/$', 'moview.views.movie'),
     url(r'^login/(\w*)', 'moview.views.login', name='login'),
     url(r'^search/$', 'moview.views.search_movies'),
     url(r'^home/$', 'moview.views.home_page'),
     url(r'^add_review/(?P<movie_id>\d+)/$', 'moview.views.add_review'),
     
)