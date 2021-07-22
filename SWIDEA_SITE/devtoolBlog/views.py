from django.shortcuts import get_object_or_404, render, redirect
from .models import Devtool
from .forms import ToolForm
# Create your views here.


def devtool_list(request):
    devtool = Devtool.objects.all()
    ctx = {'devtool': devtool}
    return render(request, template_name='devtool/list.html', context=ctx)


def devtool_detail(request, pk):
    devtool = Devtool.objects.get(id=pk)
    ctx = {'devtool': devtool}
    return render(request, template_name='devtool/detail.html', context=ctx)


def create_devtool(request):
    pass


def edit_devtool(request):
    pass


def delete_devtool(request):
    pass
