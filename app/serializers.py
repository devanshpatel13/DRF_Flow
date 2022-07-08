from rest_framework import serializers
from .models import *

class HomeSerizers(serializers.ModelSerializer):
    name = serializers.CharField()
    f_name = serializers.CharField()
    class Meta:
        model = Home
        fields = ['name', 'number', 'f_name']

    def validate(self, attrs):
        # import pdb; pdb.set_trace()
        # print(attrs,"ffffffffff")
        if attrs['name'] == attrs['f_name']:
            # print("-------------++++++++++++++++++++")
            raise serializers.ValidationError({"name": "name and f_name is same "})
            # print("fffffffffffffffff")

        return attrs

    #
    # def create(self, validated_data):
    #     user = Home.objects.create(
    #           name=validated_data['name'],
    #         number=validated_data['number'],
    #         f_name = validated_data['f_name']
    #     )
    #     user.save()
    #     return user




