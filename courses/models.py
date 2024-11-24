from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField

# Subject 모델 정의
class Subject(models.Model):
    # 제목 필드
    title = models.CharField(max_length=200)
    # 슬러그 필드
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        # 제목을 기준으로 정렬
        ordering = ['title']

    def __str__(self):
        # 객체를 문자열로 표현
        return self.title

# Course 모델 정의
class Course(models.Model):
    # 소유자 필드 (User 모델과 외래 키 관계)
    owner = models.ForeignKey(User, related_name='courses_created', on_delete=models.CASCADE)
    # 주제 필드 (Subject 모델과 외래 키 관계)
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE)
    # 제목 필드
    title = models.CharField(max_length=200)
    # 슬러그 필드
    slug = models.SlugField(max_length=200, unique=True)
    # 개요 필드
    overview = models.TextField()
    # 생성 날짜 필드
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # 생성 날짜를 기준으로 내림차순 정렬
        ordering = ['-created']

    def __str__(self):
        # 객체를 문자열로 표현
        return self.title

# Module 모델 정의
class Module(models.Model):
    # 코스 필드 (Course 모델과 외래 키 관계)
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    # 제목 필드
    title = models.CharField(max_length=200)
    # 설명 필드
    description = models.TextField(blank=True)
    # 순서 필드 (OrderField 사용)
    order = OrderField(blank=True, for_fields=['course'])

    def __str__(self):
        # 객체를 문자열로 표현
        return f'{self.order}. {self.title}'

    class Meta:
        # 순서를 기준으로 정렬
        ordering = ['order']

# Content 모델 정의
class Content(models.Model):
    # 모듈 필드 (Module 모델과 외래 키 관계)
    module = models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE)
    # 콘텐츠 타입 필드 (ContentType 모델과 외래 키 관계)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                     limit_choices_to={'model__in': ('text', 'video', 'image', 'file')})
    # 객체 ID 필드
    object_id = models.PositiveIntegerField()
    # GenericForeignKey 사용
    item = GenericForeignKey('content_type', 'object_id')
    # 순서 필드 (OrderField 사용)
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        # 순서를 기준으로 정렬
        ordering = ['order']

# ItemBase 추상 모델 정의
class ItemBase(models.Model):
    # 소유자 필드 (User 모델과 외래 키 관계)
    owner = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE)
    # 제목 필드
    title = models.CharField(max_length=250)
    # 생성 날짜 필드
    created = models.DateTimeField(auto_now_add=True)
    # 업데이트 날짜 필드
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # 추상 모델로 설정
        abstract = True

    def __str__(self):
        # 객체를 문자열로 표현
        return self.title

# Text 모델 정의 (ItemBase 상속)
class Text(ItemBase):
    # 내용 필드
    content = models.TextField()

# File 모델 정의 (ItemBase 상속)
class File(ItemBase):
    # 파일 필드
    file = models.FileField(upload_to='files')

# Image 모델 정의 (ItemBase 상속)
class Image(ItemBase):
    # 파일 필드
    file = models.FileField(upload_to='images')

# Video 모델 정의 (ItemBase 상속)
class Video(ItemBase):
    # URL 필드
    url = models.URLField()




