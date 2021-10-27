from rest_framework import serializers
from .models import User, Debt
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #extra_kwargs = {'sms_code': {'write_only': True}}
        fields = ['phone', 'username', 'avatar', 'sms_code']

    def create(self, validated_data):
        phone = validated_data['phone']
        code = validated_data['sms_code']
        try:
            user = get_user_model().objects.get(phone=phone)
            if code == user.code:
                return Response(user, status=status.HTTP_200_OK)
            else:
                return Response(status.HTTP_401_UNAUTHORIZED)
        except:        
            user = super().create(validated_data)
            user.save()
        return user
    

class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        exclude = ('owner', 'paid', 'paid_at', 'created_at', 'updated_at', 'paid_at_auto', )

class DebtPaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = ('paid', 'paid_at')