from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import Recipe
from recipe import serializer
# Create your views here.


class RecipeViewSet(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    serializer_class = serializer.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Retrieve the recipes for the authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by(-'id')

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == 'list':
            return serializer.RecipeSerializer
        return self.serializer_class