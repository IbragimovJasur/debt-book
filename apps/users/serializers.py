from rest_framework import serializers
from .models import User, Debt

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields= ('username', 'phone', 'avatar', 'password')

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
        exclude = ('contact', 'paid', 'paid_at', 'created_at', 'updated_at', 'paid_at_auto', )

class DebtPaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        include = ('paid', 'paid_at')