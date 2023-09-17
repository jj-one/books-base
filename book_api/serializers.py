from rest_framework import serializers
from .models import Book
from django.forms import ValidationError

# class BookSerializer(serializers.Serializer):

#   id = serializers.IntegerField(read_only=True)
#   title = serializers.CharField(max_length=255)
#   number_of_pages = serializers.IntegerField()
#   published_date = serializers.DateField()
#   quantity = serializers.IntegerField()

#   def create(self, validated_data):
#     return Book.objects.create(**validated_data)
  
#   def update(self, instance, validated_data):
#     instance.title = validated_data.get("title", instance.title)
#     instance.number_of_pages = validated_data.get("number_of_pages", instance.number_of_pages)
#     instance.published_date = validated_data.get("published_date", instance.published_date)
#     instance.quantity = validated_data.get("quantity", instance.quantity)
#     instance.save()
#     return instance

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = "__all__"

  # In case we wanted to add extra manual validation to a particular field
  def validate_title(self, value):
    if value.lower() == "james-java":
      raise ValidationError("james-java is not allowed as a book title")
    return value
  
  # In case we want to validate all, use
  def validate(self, data):
    if len(data["title"]) > 50:
      raise ValidationError("The title of the book seems too long")
    return data