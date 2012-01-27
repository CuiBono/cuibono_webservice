from django.shortcuts import render_to_response
from django.views.generic import TemplateView

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

