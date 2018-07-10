from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    membership = serializers.HyperlinkedIdentityField(view_name='membership-list', lookup_url_kwarg='group_pk')
    class Meta:
        model = Group
        fields = ('id', 'url', 'name', 'membership')