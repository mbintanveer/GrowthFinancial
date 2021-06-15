from django.http import HttpResponse
from django.shortcuts import redirect

def auth_required(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('index')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def top_level_required(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				unvailable = redirect("/unavailable/")
				return unvailable

		return wrapper_func
	return decorator

#def admin_only(view_func):
#	def wrapper_function(request, *args, **kwargs):
#		group = None
#		if request.user.groups.exists():
#			group = request.user.groups.all()[0].name

#		if group == 'admin':
#			return redirect('user-page')

#		if group == 'top_level':
#			return view_func(request, *args, **kwargs)

#	return wrapper_function