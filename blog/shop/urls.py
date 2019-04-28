from django.urls import path,register_converter
from shop import views
from shop import converters

app_name = 'shop'

register_converter(converters.FourDigitYearConverter,'yyyy') #converters.py 안의 클래스를 등록해주기

urlpatterns = [
    path('excel/', views.response_excel),
    path('image/',views.response_image),
    path('mysum/<int:x>/<int:y>/',views.my_sum), # 뭔지 모르지만 숫자(int)가 들어오는데 그걸 x,y로 처리하겠다. 뷰의 마이썸이란 함수로 보내라
    path('archives/<yyyy:year>/', views.year_archive), #내가 직접 year를 호출할 컨버터 yyyy를 생성. 뷰의 year_archives 함수로 보내라
    path('', views.item_list),
    path('test_templates/', views.test_templates),
]

