from django.shortcuts import redirect
from django.http import HttpResponse


def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'specialist':
			return redirect('user-page')

		elif group == 'admin':
			return view_func(request, *args, **kwargs)

		elif group == 'teamlead':
			return view_func(request, *args, **kwargs)
		else:
			return HttpResponse('none group')

	return wrapper_function

