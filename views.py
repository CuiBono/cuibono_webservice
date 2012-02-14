from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

class WelcomeView(TemplateView):
	template_name = 'welcome.html'
	
class AboutView(TemplateView):
    template_name = 'about.html'
    

class TeamView(TemplateView):
    template_name = 'team.html'
	
class PartnersView(TemplateView):
    template_name = 'partners.html'
	
class NewsView(TemplateView):
    template_name = 'news.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')
