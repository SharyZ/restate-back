from rest_framework import serializers

from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'description', 'price', 'sale_type', 'address', 'city', 'featured_image']
