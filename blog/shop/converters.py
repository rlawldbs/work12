import datetime

class FourDigitYearConverter:
    regex = r'\d{4}' #숫자 4번을 의미 = r'\d{4}'

    def to_python(self,value):
        if 2010 <= int(value) <= datetime.datetime.now().year: #정상적인 해당기간일 때는 int를 바꿔서 보내고 아니면 처리하지 말자
            return int(value)
        else:
            return None

    def to_url(self,value):
        return '{%04d}'.format(value) #만약 세자리 찍었을 때 모자라는 값은 0이라도 채워라 =%04d