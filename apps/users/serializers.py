from rest_framework import serializers
from .models import User, Debt

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields= ('username', 'phone_number', 'avatar', 'password')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user

class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        exclude = ('contact', 'updated_on',)
        