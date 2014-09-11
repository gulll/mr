from django.shortcuts import render
from django.shortcuts import render_to_response
from moview.models import Movie,Review
from forms import MovieForm,ReviewForm
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse
from authomatic import Authomatic
from django.utils import timezone
from authomatic.adapters import DjangoAdapter

from config import CONFIG

authomatic = Authomatic(CONFIG, 'abc')
# Create your views here.

def movies(request):
    args ={}
    args.update(csrf(request))
    args['movies'] =Movie.objects.all()
    
    if 'user' in request.session:
       args['result']=request.session['user']
    else:
       args['result']=''
         
    return render_to_response('movies.html',args)
    	                         
def movie(request,movie_id=1):
    args ={}
    args.update(csrf(request))
    args['movie'] =Movie.objects.get(id=movie_id)
    if 'user' in request.session:
       args['result']=request.session['user']
    else:
       args['result']=''
    return render_to_response('movie.html',args)
    	                         
def login(request, provider_name):
    response = HttpResponse()
    
    result = authomatic.login(DjangoAdapter(request, response), provider_name)
    if result:
        response.write('<a href="/accounts/loggedin">Home</a>')
        if result.error:
            response.write('<h2>Error: {0}</h2>'.format(result.error.message))
        
        elif result.user:
            if not (result.user.name and result.user.id):
                result.user.update()
            response.write(u'<h1>Hi {0}</h1>'.format(result.user))
            request.session['user']=result.user.name
    if 'user' in request.session:
           return render_to_response('loggedin.html',
                              {'result': request.session['user']})
    else :
          return response
          
def search_movies(request):
     if request.method == "POST":
        search_text= request.POST['search_text']
     else:
        search_text=''
        
     args={}
     args.update(csrf(request))
        
     movies=Movie.objects.filter(title__contains=search_text)
     args['movies']=movies
     
     return render_to_response('search_result.html',args)

     
def add_review(request,movie_id):
     rm=Movie.objects.get(id=movie_id)
     if request.method == "POST":
         f=ReviewForm(request.POST)
         if f.is_valid():
          r=f.save(commit=False)
          r.user=request.session['user']
          r.post_date = timezone.now()
          r.movie =rm
          r.save()
          return HttpResponseRedirect('/movies/get/%s' % movie_id)
     else:
         f=ReviewForm()
     
     args={}
     args.update(csrf(request))
     
     args['movie']=rm
     args['form']=f;
     if 'user' in request.session:
       args['result']=request.session['user']
     return render_to_response('add_review.html',args)

def home_page(request):

        
     movies=Movie.objects.all().order_by('rel_date')[:3]
     if 'user' in request.session:
         return render_to_response('home.html',{'movies':movies,'result':request.session['user']})

     return render_to_response('home.html',{'movies':movies,'result':''})     