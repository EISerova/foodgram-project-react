from django_filters.rest_framework import FilterSet, filters
from rest_framework.filters import SearchFilter

from recipes.models import Recipe, Ingredient


class IngredientSearchFilter(SearchFilter):
    search_param = "name"

    class Meta:
        model = Ingredient
        fields = ("name",)


class RecipeListFilter(FilterSet):
    is_favorited = filters.BooleanFilter(method="get_is_favorited")
    is_in_shopping_cart = filters.BooleanFilter(
        method="get_is_in_shopping_cart"
    )
    tags = filters.AllValuesMultipleFilter(
        field_name="tags__slug",
        lookup_expr="exact",
    )

    class Meta:
        model = Recipe
        fields = (
            "tags",
            "author",
            "is_favorited",
        )

    def get_is_favorited(self, queryset, name, value):
        """Возвращает значение boolean по полю is_favorited."""
        if value:
            return queryset.filter(favorites__user=self.request.user)
        return queryset

    def get_is_in_shopping_cart(self, queryset, name, value):
        """Возвращает значение boolean по полю is_in_shopping_cart."""
        if value:
            return queryset.filter(cart__user=self.request.user)
        return queryset
