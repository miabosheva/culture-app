from django.shortcuts import render
from .models import Event, Artist
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
	# return HttpResponse("Hello, world. This is the index page.")

	queryset = Event.objects.all()
	context = {"events": queryset, "Date": datetime.now().date()}
	return render(request, "index.html", context=context)


def details(request, title):
	event = Event.objects.get(title=title)
	context = {"event": event}
	return render(request, "details.html", context=context)