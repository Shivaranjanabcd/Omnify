from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ClassSerializer, ClassCategorySerializer, ClientSerializer
from .models import Class, Client
from rest_framework.views import APIView
from django.utils import timezone
from django.db.models import F
from rest_framework import status


class Class_view(APIView):
    def get(self, request):

        classes = Class.objects.select_related("class_name").filter(
            date__gt=timezone.now()
        )
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        if Class.objects.get(class_name__id=data["class_name"]).slots > 0:
            Class.objects.filter(class_name__id=data["class_name"]).update(
                slots=F("slots") - 1
            )
            serializer = ClientSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)

        return Response({"error": "slots not available"}, status=400)


class Show(APIView):
    def get(self, request):
        email = request.GET.get("email")
        if not email:
            return Response(
                {"error": "No Email found!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        bookings = Client.objects.filter(c_email=email)
        serializer = ClientSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
