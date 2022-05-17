from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ListingSerializer
from .models import Listing

# Create your views here.


class ListingList(APIView):
    def get(self, request, format=None):
        """
        Return a list of all listings
        """
        listings = Listing.objects.all()
        serializer = ListingSerializer(listings, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListingDetail(APIView):
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return Listing.objects.get(pk=pk)
        except Listing.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Retrieve a listing instance
        """
        listing = self.get_object(pk)
        serializer = ListingSerializer(listing, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
