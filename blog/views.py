from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from .models import Contacts
from .forms import PostForm

#Main Page
def index(request):
    template = loader.get_template('blog/post_index.html')
    context = {}
    return HttpResponse(template.render(context, request))

#List Page
def post_list(request):
    template = loader.get_template('blog/post_list.html')
    contacts = Contacts.objects.order_by('pk')
    context = {
        'contacts' : contacts
    }
    return HttpResponse(template.render(context, request))

#Insert Page
def insert(request):
    #new form
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    template = loader.get_template('blog/post_edit.html')
    context = {
        'form' : form
    }
    return HttpResponse(template.render(context, request))

#Update Page
def update(request):
    template = loader.get_template('blog/post_update.html')
    contacts = Contacts.objects.order_by('pk')
    context = {
        'contacts' : contacts,
    }
    return HttpResponse(template.render(context, request))

def update_specific(request, pk):
    contacts = Contacts.objects.filter(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=contacts[0])
        if form.is_valid():
            form.save()
        return redirect('update')
    if len(contacts) == 0:
        return redirect('update')
    form = PostForm(instance=contacts[0])
    template = loader.get_template('blog/updatespecific.html')
    context = {
        'form' : form,
    }
    return HttpResponse(template.render(context, request))
         

#Delete Page
def delete(request, pk=None):
    if pk != "":
        Contacts.objects.filter(pk=pk).delete()
    template = loader.get_template('blog/post_delete.html')
    contacts = Contacts.objects.order_by('pk')
    context = {
        'contacts' : contacts,
    }
    return HttpResponse(template.render(context, request))

#Search Page
def search(request):
    searchName = request.GET.get('name','')
    if searchName != "":
        return search_specific(request, searchName)
    template = loader.get_template('blog/post_search.html')
    contacts = Contacts.objects.order_by('pk')
    context = {
        'contacts' : contacts,
    }
    return HttpResponse(template.render(context, request))

def search_specific(request, name):
    searched = Contacts.objects.filter(name__icontains=name)
    context = {
        'name' : name,
        'contacts' : searched,
    }
    template = loader.get_template('blog/searchedName.html')
    return HttpResponse(template.render(context, request))