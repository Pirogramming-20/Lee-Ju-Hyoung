from django.shortcuts import render, redirect
from .form import DevToolForm
from .models import DevTool

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
        form.save()
    return redirect('devtool:list')

def detail(request, pk):
    devtools = DevTool.objects.get(id=pk)
    ctx = {'devtool': devtools}
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
    