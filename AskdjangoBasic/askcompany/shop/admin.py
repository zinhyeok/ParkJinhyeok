from django.contrib import admin
from .models import Item
# Register your models here.
# admin.site.register(Item) #기본 modelAdmin으로 동작


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'short_desc',
                    'price', 'is_publish']  # 배열 안에 것을 보여줌
    list_display_links = ['name']  # name에 링크
    search_fields = ['name']  # name으로 검색하기
    list_filter = ['is_publish', 'updated_at']  # 게시글에 필터(카테고리) 만들기

    def short_desc(self, item):
        return item.desc[:20]  # desc의 처음 20자만 가져오기
