from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, request
from .models import Item
import re
import logging
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


def item_new(request, item=None):
    error_list = []
    initial = {}

    if request.method == 'POST':
        data = request.POST
        files = request.FILES

        name = data.get('name')
        desc = data.get('desc')
        price = data.get('price')
        photo = files.get('photo')
        is_publish = data.get('is_publish') in (True, 't', 'True', '1')

        # 유효성 검사
        if len(name) < 2:
            error_list.append('name을 2글자 이상 입력해주세요.')

        if re.match(r'^[\da-zA-Z\s]+$', desc):
            error_list.append('한글을 입력해주세요.')

        if not error_list:
            # 저장 시도
            if item is None:
                item = Item()

            item.name = name
            item.desc = desc
            item.price = price
            item.is_publish = is_publish

            if photo:
                item.photo.save(photo.name, photo, save=False)

            try:
                item.save()
            except Exception as e:
                error_list.append(e)
            else:
                return redirect(item)

        initial = {
            'name': name,
            'desc': desc,
            'price': price,
            'photo': photo,
            'is_publish': is_publish,
        }
    else:
        if item is not None:
            initial = {
                'name': item.name,
                'desc': item.desc,
                'price': item.price,
                'photo': item.photo,
                'is_publish': item.is_publish,
            }

    return render(request, 'shop/item_form.html', {
        'error_list': error_list,
        'initial': initial,
    })


def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return item_new(request, item)
