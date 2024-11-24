from django import template

# 템플릿 라이브러리 인스턴스 생성
register = template.Library()

@register.filter
def model_name(obj):
    # 객체의 모델 이름을 반환
    try:
        return obj._meta.model_name
    except AttributeError:
        # 객체에 모델 이름이 없으면 None 반환
        return None