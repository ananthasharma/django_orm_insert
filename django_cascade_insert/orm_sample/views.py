from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django_cascade_insert.orm_sample import models


# Create your views here.


class InsertData(APIView):
    def get(self, request):
     
        group_name = request.GET.get('group_name')
        file1 = request.GET.get('file1')
        file2 = request.GET.get('file2')
        file3 = request.GET.get('file3')
        file_names = [file1,file2,file3]
        string=f"inserted Group name as {group_name} with {len(file_names)} files"
        content = {"message":string}

        group_registry = models.GroupRegistry()
        group_registry.name = group_name
        group_registry.save() #save the group
        for file_name in file_names:
            mapper = models.GroupDataRegistryMapper()
            file_registry = models.DataRegistry()
            file_registry.file_name = file_name
            file_registry.file_path = "maprfs:///some/predefined/file/location"
            file_registry.save() #save the file
            mapper.group_registry = group_registry #assign previously saved group
            mapper.data_registry = file_registry #assign previously saved file
            mapper.save() #save mapping
        
        return Response(content)