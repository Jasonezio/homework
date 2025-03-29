from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from .models import ModelPost
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
# Create your views here.
def home(request):
        return render(request, "wellcome_page.html")


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


                