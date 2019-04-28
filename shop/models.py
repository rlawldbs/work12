from django.db import models
from pytz import timezone  # 현지 시각 출력을 위하여
from django.conf import settings
from django.urls import reverse

def local_time(input_time):
    fmt = '%Y-%m-%d %H:%M'
    my_zone = timezone(settings.TIME_ZONE)
    my_local_time = input_time.astimezone(my_zone)
    return my_local_time.strftime(fmt)

class Item(models.Model):
    name = models.CharField('이름', max_length=20)
    desc = models.TextField('내용', blank=True)
    photo = models.ImageField()  # blank=True 지정하지 않은 경우
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']  # Post 객체의 기본 정렬 순서 지정

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:item_detail', kwargs={'pk': self.pk})
