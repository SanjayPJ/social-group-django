from django.shortcuts import render
from .models import Group
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_list_or_404
from posts.models import Post
# Create your views here.


class GroupListView(ListView):
    model = Group


def group_list(request):
    group_list = Group.objects.all()
    return render(request, 'groups/group_list.html', {
        'group_list': group_list
    })


class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    fields = ('name', 'description')


class GroupUpdateView(UpdateView):
    model = Group
    fields = ('name', 'description')
    template_name = 'groups/group_update_form.html'


class GroupDetailView(DetailView):
    model = Group

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_list = Post.objects.filter(group=self.object)
        context['post_list'] = post_list
        context['is_there'] = self.object.members.all
        return context


class GroupDeleteView(DeleteView):
    model = Group
    success_url = reverse_lazy('groups:main')
