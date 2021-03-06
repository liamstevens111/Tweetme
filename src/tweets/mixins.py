from django import forms
from django.forms.utils import ErrorList

class FormUserNeededMixin(object):

	# Mixin for displaying an error to user when attempting to create a tweet, 
	# this is different from deneying access to the page or redirecting such as LoginRequiredMixin
	
	def form_valid(self, form):
		# This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
		if self.request.user.is_authenticated():
			form.instance.user = self.request.user
			return super(FormUserNeededMixin, self).form_valid(form)
		else:
			form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue"])
			return self.form_invalid(form)


class UserOwnerMixin(object):
	def form_valid(self, form):
		if form.instance.user == self.request.user:
			return super(UserOwnerMixin, self).form_valid(form)
		else:
			form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["This user is not allowed to modifiy this data"])
			return self.form_invalid(form)
