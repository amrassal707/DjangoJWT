from rest_framework import serializers
from .models import book

# a serializer class to convert model to json and vice versa
class bookserializers(serializers.ModelSerializer):
    #it needs a query set to serialize and a serializer
    class Meta:
        model= book
        #acts as DTO
        fields = ['id','title', 'price', 'inventory']
        """
        Why use class meta in Django?
Class Meta is the place in your code logic where your model. fields MEET With your form. widgets.
So under Class Meta() you create the link between your model' fields and the different widgets you want to have in your form
        """
    
    