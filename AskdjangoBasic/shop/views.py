import re
import logging
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, request
from .models import Item
from .forms import ItemForm
from django.views.generic import CreateView, UpdateView
# 주요request 속성
# request.method: GET,POST 요청인지 알려줌
# request.META: META정보(요청 header포함)
# request.GET,request.POST

# DB 추가:insert, 수정:update , 삭제:delete


def achieve_year(request, year):
    return HttpResponse('{}년도에 대한내용'.format(year))


def item_list(request):
    qs = Item.objects.all()  # 호출 예정 아직 호출 X, qurey는 꼭 필요할 때 호출됨)
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(neme__icontains=q)  # 대소문자 무시
    return render(request, 'shop/item_list.html', {  # shop/은 namespace 정확한 template을 불러주기 위해 이용
        'item_list': qs,
        'q': q,
    })


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shop/item_detail.html', {
        'item': item
    })


item_new = CreateView.as_view(model=Item, form_class=ItemForm)
item_edit = UpdateView.as_view(model=Item, form_class=ItemForm)
# def item_new(request, item=None):
#     if request.method == 'POST':
#         form = ItemForm(Required.POST, request.FILES)
#         if form.is_valid():
#             item = form.save()  # MODELForm에서 제공
#     else:
#         form = ItemForm()

#     return render(request, 'shop/item_form.html', {
#         'form': form
#     })


# def item_edit(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     return item_new(request, item)
