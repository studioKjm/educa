from django.contrib import admin
from .models import Subject, Course, Module

# Subject 모델을 위한 관리자 클래스 등록
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    # 관리자 화면에 표시할 필드 설정
    list_display = ['title', 'slug']
    # 제목 필드를 기반으로 슬러그 필드 자동 생성
    prepopulated_fields = {'slug': ('title',)}

# Module 모델을 위한 인라인 클래스 정의
class ModuleInline(admin.StackedInline):
    model = Module

# Course 모델을 위한 관리자 클래스 등록
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # 관리자 화면에 표시할 필드 설정
    list_display = ['title', 'subject', 'created']
    # 필터링 옵션 설정
    list_filter = ['created', 'subject']
    # 검색 필드 설정
    search_fields = ['title', 'overview']
    # 제목 필드를 기반으로 슬러그 필드 자동 생성
    prepopulated_fields = {'slug': ('title',)}
    # 인라인 모델 설정
    inlines = [ModuleInline]