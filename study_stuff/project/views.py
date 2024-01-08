from django.shortcuts import render,redirect

from project.models import Project
from .forms import ProjectFom
# Create your views here.

def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects
    }
    return render(request,'project/template.html', context)
def project_creator(request):
    form = ProjectFom()
    if request.method == 'POST':
        form = ProjectFom(request.POST)
        if form.is_valid():
            form.save(request)
            return redirect('home')
    context = {'form':form}
    return render(request,'project/project-form.html',context)
def project_update(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectFom(instance=project,)
    if request.method == 'POST':
        form = ProjectFom(request.POST , instance=project,)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'project/project-form.html',context)
def project_delete(request,pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('home')
    context = {'object':object}
    return render(request,'project/delete.html',context)