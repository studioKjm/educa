from django.urls import path
from . import views

urlpatterns = [
    # 사용자가 소유한 강좌 목록을 관리하는 뷰
    path('mine/', views.ManageCourseListView.as_view(), name='manage_course_list'),
    # 새로운 강좌를 생성하는 뷰
    path('create/', views.CourseCreateView.as_view(), name='course_create'),
    # 기존 강좌를 수정하는 뷰
    path('<pk>/edit/', views.CourseUpdateView.as_view(), name='course_edit'),
    # 기존 강좌를 삭제하는 뷰
    path('<pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),
    # 강좌의 모듈을 업데이트하는 뷰
    path('<pk>/module/', views.CourseModuleUpdateView.as_view(), name='course_module_update'),
    # 모듈에 새로운 콘텐츠를 생성하는 뷰
    path('module/<int:module_id>/content/<model_name>/create/',
         views.ContentCreateUpdateView.as_view(), name='module_content_create'),
    # 모듈의 기존 콘텐츠를 업데이트하는 뷰
    path('module/<int:module_id>/content/<model_name>/<id>/',
         views.ContentCreateUpdateView.as_view(), name='module_content_update'),
    # 모듈의 콘텐츠를 삭제하는 뷰
    path('content/<int:id>/delete/', views.ContentDeleteView.as_view(), name='module_content_delete'),
    # 강좌의 모듈 목록을 보여주는 뷰
    path('module/<int:module_id>/', views.ModuleContentListView.as_view(), name='module_content_list'),
    # 강좌를 구매하는 뷰
    path('module/order/', views.ModuleOrderView.as_view(), name='module_order'),
    # 콘텐츠를 구매하는 뷰
    path('content/order/', views.ContentOrderView.as_view(), name='content_order'),
    # 강좌 목록을 보여주는 뷰
    path('subject/<slug:subject>/', views.CourseListView.as_view(), name='course_list_subject'),
    # 강좌 디테일 뷰
    path('<slug:slug>/', views.CourseDetailView.as_view(), name='course_detail'),

]