import datetime
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from .models import * 

def index(request):
	try:
		category = json.loads(request.COOKIES['category'])
	except:
		category = {}
		print('category:', category)

	try:
		filteredSearch = category['style']
	except:
		filteredSearch = ''

	try:
		hearted = json.loads(request.COOKIES['hearted'])
	except:
		hearted = {}
		print('hearted:', hearted)

	likeList = []
	for heart in hearted:
		likeList.append(int(heart))

	try:
		search = json.loads(request.COOKIES['search'])
	except:
		search = {}
		print('search:', search)

	try:
		searchSize = search['size']
		print(searchSize)
	except:
		searchSize = 6

	
	if filteredSearch != 'Browse All' and filteredSearch != '':
		if filteredSearch == 'favourite':
			songs = Music.objects.filter(id__in = likeList).order_by('-date_added')[:searchSize]
		else:
			songs = Music.objects.filter(genre__contains = filteredSearch).order_by('-date_added')[:searchSize]
	else:
		songs = Music.objects.all().order_by('-date_added')[:searchSize]

	context = {'songs':songs, 'likeList':likeList, 'searchSize': searchSize}
	return render(request, 'store/index.html', context)

def pricing(request):
	return render(request, 'store/pricing.html')

def contact(request):
	return render(request, 'store/contact.html')

def checkout(request):
	return render(request, 'store/checkout.html')

def sendRequest(request):
	request_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)


	Contact.objects.create(
		name = data['contact']['name'],
		email = data['contact']['email'],
		subject = data['contact']['subject'],
		question = data['contact']['question'],
		request_id = request_id,
		replied = False,
	)

	return JsonResponse('Question sent..', safe=False)