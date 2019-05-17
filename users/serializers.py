from rest_framework import serializers
from users.models import MyUser


class MyUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = MyUser
        fields = ('username', 'first_name', 'last_name', 'email', 'avatar', 'password')

    def create(self, validated_data):
        user = MyUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        if validated_data.get('password') and validated_data.get('password') != instance.password:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance
