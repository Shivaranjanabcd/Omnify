from .models import Class, ClassCategory, Client
from rest_framework import serializers


class ClassCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassCategory
        fields = "__all__"


class ClassSerializer(serializers.ModelSerializer):
    class_name = ClassCategorySerializer(read_only=True)

    class Meta:
        model = Class
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class_name = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all())

    class Meta:
        model = Client
        fields = "__all__"
