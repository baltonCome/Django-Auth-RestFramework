import email
from django.forms import ValidationError
from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length = 50)
    username = serializers.CharField(max_length = 50)
    password = serializers.CharField(min_length = 8, write_only = True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email_exists = User.objects.filter(email = attrs['email']).exists()

        if email_exists:
            raise ValidationError("Email already exists")

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)

        user.save()
        Token.objects.create(user=user)

        return user


class CurrentUserPostsSerializer(serializers.ModelSerializer):

    posts = serializers.StringRelatedField(many = True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'posts']


class UserDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email']



# class CurrentUserPostsSerializer(serializers.ModelSerializer):

#     posts = serializers.HyperlinkedRelatedField(
#         many = True, 
#         view_name = "post_detail",
#         queryset = User.objects.all()
#     )

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'posts']

