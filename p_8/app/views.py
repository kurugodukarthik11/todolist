from django.shortcuts import render, redirect
from app.models import ToDolist


# Create your views here.
def index(request):
    all_works = ToDolist.objects.all()
    if request.method == 'POST':
        new_work = ToDolist(work=request.POST['work_name'])
        new_work.save()
        return redirect('/')
    return render(request, 'index.html', {'todos': all_works})


def delete(request, del_work):
    del_works = ToDolist.objects.get(id=del_work)
    del_works.delete()
    return redirect('/')
