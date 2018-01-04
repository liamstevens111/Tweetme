from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Tweet

# Create your views here.


# Create

# Update

# Delete

# Retreive / Read

class TweetDetailView(DetailView):
	queryset = Tweet.objects.all()
	template_name = "tweets/detail_view.html"

	# def get_object(self):
	# 	pk = self.kwargs.get("pk")
	# 	return Tweet.objects.get(id = pk)    # Features similiar to this pre-built in

class TweetListView(ListView):
	queryset = Tweet.objects.all()
	template_name = "tweets/list_view.html"

	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)
		return context

# def tweet_detail_view(request, pk = None):
# 	obj = Tweet.objects.get(pk = pk) # Get from DB
#   obj = get_object_or_404(Tweet, pk = pk)
# 	context = {
# 		"object": obj
# 	}

# 	return render(request, "tweets/detail_view.html", context)

# def tweet_list_view(request):
# 	queryset = Tweet.objects.all()
# 	context = {
# 		"object_list": queryset
# 	}

# 	return render(request, "tweets/list_view.html", context)