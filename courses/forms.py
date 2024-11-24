from django import forms
from django.forms.models import inlineformset_factory
from .models import Course, Module

# Course와 Module 모델을 위한 인라인 폼셋 생성
ModuleFormSet = inlineformset_factory(
    Course,  # 부모 모델
    Module,  # 자식 모델
    fields=['title', 'description'],  # 포함할 필드
    extra=2,  # 추가할 빈 폼의 수
    can_delete=True  # 폼 삭제 가능 여부
)