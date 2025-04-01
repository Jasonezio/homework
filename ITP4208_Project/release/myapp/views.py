from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import ModelPost, Weather_data
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
import datetime
# Create your views here.

def load_img(request, path):
    print(path)
    return HttpResponse(path)

def get_sun(request):
    for date in Weather_data.get_sun_time():
        if datetime.datetime.today().strftime('%Y-%m-%d') == date[0]:
                return JsonResponse(date, safe=False)


class ViewModelPost(ListView):
        queryset = ModelPost.objects.all()
        template_name = 'list.html'

class CreateModelPost(LoginRequiredMixin, CreateView):
        login_url = '/login/'
        model = ModelPost
        fields = '__all__'
        template_name = 'create_ModelPost_form.html'

        def form_valid(self, form):
                model = form.save(commit=False)
                model.save()
                return HttpResponseRedirect(reverse('list'))
                
class UpdateModelPost(UpdateView):
        model = ModelPost
        fields = ['title', 'author', 'content']
        template_name = 'update_ModelPost_form.html'

        def get_object(self, queryset=None):
                id = self.kwargs['id']
                return self.model.objects.get(id=id)

        def form_valid(self, form):
                model = form.save(commit=False)
                model.save()
                return HttpResponseRedirect(reverse('list'))

class DeleteModelPost(DeleteView):
        model = ModelPost
        template_name = 'delete_ModelPost_form.html'

        def get_success_url(self):
                return reverse('list')


                