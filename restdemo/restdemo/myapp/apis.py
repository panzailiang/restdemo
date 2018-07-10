# -*- encoding: utf8 -*-
from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import mixins 
from rest_framework import status
from rest_framework import schemas
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer
from rest_framework.compat import coreapi, coreschema

import logging
logger = logging.getLogger(__name__)

class UserViewSet(viewsets.ModelViewSet):
    """
    用户API接口

    retrieve:
    get a single user.

    list: 
    获取 **用户** 列表
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    用户组API接口
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class MembershipViewSet(viewsets.ViewSet):
    """
    Group Memebership API Endpoint.
    """
    # schema = schemas.AutoSchema(manual_fields=[
    #     coreapi.Field('group_pk', required=True, location='path', schema=coreschema.String(description='group id desc')),
    #     coreapi.Field('id', required=True, location='path', schema=coreschema.String(description='user id')),
    # ])

    def get_group(self):
        group_pk = self.kwargs['group_pk']
        return Group.objects.get(pk=group_pk)

    def get_user(self):
        return User.objects.get(pk=self.kwargs['pk'])

    def list(self, request, *args, **kwargs):
        group = self.get_group()
        user_list_slr = UserSerializer(group.user_set, many=True, context={'request': request})
        return Response(user_list_slr.data)

    def retrieve(self, request, *args, **kwargs):
        """
        获取group的membership

        * group_pk: group id
        """
        print('start retrieve')
        logger.info('get membership')
        group = self.get_group()
        user = get_object_or_404(group.user_set, pk=self.kwargs['pk'])
        user_slr = UserSerializer(user, context={'request': request})
        return Response(user_slr.data)

    def update(self, request, *args, **kwargs):
        'update api'
        group = self.get_group()
        user = self.get_user()
        group.user_set.add(user)
        user_slr = UserSerializer(user, context={'request': request})
        return Response(user_slr.data)
    
    def destroy(self, request, *args, **kwargs):
        group = self.get_group()
        user = self.get_user()
        group.user_set.remove(user)
        return Response(status = status.HTTP_204_NO_CONTENT)
