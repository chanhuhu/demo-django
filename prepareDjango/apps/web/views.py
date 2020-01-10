from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from prepareDjango.apps.web.forms import LoginForm
from prepareDjango.apps.web.models import User


class HomePage(View):

    def get(self, request):
        context = dict()
        context['form'] = LoginForm()
        # x = User.objects.filter(username="usr_korn")
        # x = User.objects.filter(username__startwith="usr_korn")
        # x.first()
        return render(request, "web/index.html", context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponse(form.cleaned_data['username'])
        context = dict()
        context['form'] = form
        return render(request, "web/index.html", context)