from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Course, CourseSerializer
from rest_framework import mixins, generics

# Create your views here.

class CourseListView(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request):
      return self.list(request)


    def post(self, request):
      return self.create(request)  
   


class CourseDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

                    
                   
                    
 
