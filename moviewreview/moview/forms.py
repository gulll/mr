from django import forms
from models import Movie ,Review

class MovieForm(forms.ModelForm):
	
	class Meta:
		model=Movie
		fields=('title','body','rel_date')
		
class ReviewForm(forms.ModelForm):
	
	class Meta:
		model=Review
		fields=('body','rating')