from django.shortcuts import render, redirect
from django.http import HttpResponse 

def home_page(request):
	
	if request.method == 'POST':
		return redirect('/search/')
	return render(request, 'home.html')

def search_page(request):

	search_term = request.GET.get('course_search')
	
	return render(request, 'search.html', {'search_term': search_term})
	
