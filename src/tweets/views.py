from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.db.models import Q

from django.views.generic import (
				CreateView, 
				DetailView, 
				DeleteView, 
				ListView,
				UpdateView
				)

from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Tweet




# Create

class TweetCreateView(FormUserNeededMixin, CreateView):
	form_class = TweetModelForm
	template_name = "tweets/create_view.html"
	#success_url = reverse_lazy("tweet:detail", ) - moved to model
	login_url = '/admin/'

# Update

class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
	queryset = Tweet.objects.all()
	form_class = TweetModelForm
	template_name = "tweets/update_view.html"
	#success_url = "/tweet/" -  - moved to model


# Delete

class TweetDeleteView(LoginRequiredMixin, UserOwnerMixin, DeleteView):
	#queryset = Tweet.objects.all()
	model = Tweet
	template_name = "tweets/delete_confirm.html"
	success_url = reverse_lazy("tweet:list")

# Retreive / Read

class TweetDetailView(DetailView):
	queryset = Tweet.objects.all()
	template_name = "tweets/tweet_detail.html"

	# def get_object(self):
	# 	pk = self.kwargs.get("pk")
	# 	return Tweet.objects.get(id = pk)    # Features similiar to this pre-built in

class TweetListView(ListView):
	# queryset = Tweet.objects.all()
	# template_name = "tweets/list_view.html"
	# if not template, the model_view name is used, ie tweet_list

	def get_queryset(self, *args, **kwargs):
		qs = Tweet.objects.all()
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(Q(content__icontains=query) |
					Q(content__icontains=query) |
					Q(user__username__icontains=query)
					)
		return qs

	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)
		context['create_form'] = TweetModelForm()
		context['create_url'] = reverse_lazy("tweet:create")
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