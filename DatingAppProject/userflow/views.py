from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import PreferenceForm
from userhome.models import Interest, Location
# Create your views here.

class SettingsView(TemplateView):
    template_name = "Settings.html"


class PrivacySettingsView(TemplateView):
    template_name="Privacy.html"



class FilterView(TemplateView):
    template_name = "filter.html"


class PreferenceView(CreateView):
    template_name = "Preference.html"
    form_class = PreferenceForm
    success_url = reverse_lazy('userflow:FilterView')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["interest"] = Interest.objects.all()
        context["location"] = Location.objects.all()
        return context
    def form_valid(self, form):
        user_preference = form.save(commit=False)
        user_preference.user = self.request.user 
        user_preference.save()
        
        form.cleaned_data['location'] = self.request.POST.getlist('location')
        form.cleaned_data['interests_hobbies'] = self.request.POST.getlist('interests_hobbies')

        user_preference.location.set(form.cleaned_data['location'])
        user_preference.interests_hobbies.set(form.cleaned_data['interests_hobbies'])

        return super().form_valid(form)
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)