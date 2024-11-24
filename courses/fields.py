from django.db import models
from django.core.exceptions import ObjectDoesNotExist

# OrderField 클래스 정의, PositiveIntegerField를 상속받음
class OrderField(models.PositiveIntegerField):
    def __init__(self, for_fields=None, *args, **kwargs):
        # for_fields 인자를 받아서 인스턴스 변수로 저장
        self.for_fields = for_fields
        # 부모 클래스의 초기화 메서드 호출
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        # 모델 인스턴스에 현재 값이 없는 경우
        if getattr(model_instance, self.attname) is None:
            try:
                # 모델의 모든 객체를 쿼리셋으로 가져옴
                qs = self.model.objects.all()
                if self.for_fields:
                    # for_fields에 있는 필드 값으로 필터링
                    query = {field: getattr(model_instance, field) for field in self.for_fields}
                    qs = qs.filter(**query)
                # 마지막 항목의 순서를 가져옴
                last_item = qs.latest(self.attname)
                value = last_item.order + 1
            except ObjectDoesNotExist:
                # 객체가 없으면 0으로 설정
                value = 0
            # 모델 인스턴스에 값 설정
            setattr(model_instance, self.attname, value)
            return value
        else:
            # 부모 클래스의 pre_save 메서드 호출
            return super().pre_save(model_instance, add)