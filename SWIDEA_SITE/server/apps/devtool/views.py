from django.shortcuts import render, redirect
from .form import DevToolForm
from .models import DevTool
from apps.idea.models import Idea

# Create your views here.
def list(request):
    devtool = DevTool.objects.all()
    ctx = {'devtools' : devtool}
    return render(request, 'devtool/devtool_list.html', ctx)

def create(request):
    if request.method == 'GET':
        form = DevToolForm()
        ctx = {'form':form}
        return render(request, 'devtool/devtool_create.html', ctx)
    #post일때
    form = DevToolForm(request.POST)
    if form.is_valid():
        new_devtool = form.save()
        return redirect('devtool:detail', pk=new_devtool.pk)
    else :
        return redirect('devtool:list')

def detail(request, pk):
    devtools = DevTool.objects.get(id=pk)
    ideas = Idea.objects.all()
    related_ideas = devtools.idea_set.all()
    ctx = {'idea':ideas, 'devtool': devtools, 'related_ideas' : related_ideas}
    return render(request, 'devtool/devtool_detail.html', ctx)

def delete(request, pk):
    if request.method == "POST":
        DevTool.objects.get(id=pk).delete()
    return redirect('devtool:list')

def update(request, pk):
    idea=DevTool.objects.get(id=pk)
    
    if request.method=='GET':
        form = DevToolForm(instance=idea)
        ctx = {'form':form, 'pk':pk}
        return render(request, 'devtool/devtool_update.html', ctx)
    
    form=DevToolForm(request.POST, instance=idea)
    if form.is_valid():
        form.save()
    return redirect('devtool:detail', pk)
    