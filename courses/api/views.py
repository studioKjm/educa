from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics
from courses.models import Subject, Course
from rest_framework import viewsets
from courses.api.serializers import SubjectSerializer, CourseSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

# class CourseEnrollView(APIView):
#     athentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     def post(self, request, pk, format=None):
#         course = get_object_or_404(Course, id=pk)
#         course.students.add(request.user)
#         return Response({'enrolled': True})

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    @action(detail=True, methods=['post'],
            authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated])

    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})






