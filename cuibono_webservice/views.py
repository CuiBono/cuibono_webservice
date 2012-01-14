from django.shortcuts import render_to_response
from django.views.generic import TemplateView

class WelcomeView(TemplateView):
	template_name = 'welcome.html'
	
class AboutView(TemplateView):
    template_name = 'about.html'
    
#Not sure about this one... There is probably a better generic view to use here.
class SubmitView(TemplateView):
    template_name = 'submit.html'

	
	
