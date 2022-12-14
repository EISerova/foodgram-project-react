from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CustomUserViewSet,
    FavoriteViewSet,
    IngredientViewSet,
    RecipeViewSet,
    TagViewSet,
)

app_name = "api"

router = DefaultRouter()

router.register(r"collect", RecipeViewSet, basename="collect")
router.register(r"tags", TagViewSet, basename="tags")
router.register(r"favorites", FavoriteViewSet, basename="favorites")
router.register(r"users", CustomUserViewSet, basename="users")
router.register(r"ingredients", IngredientViewSet, basename="ingredients")

urlpatterns = [
    path("", include(router.urls)),
    path("", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
