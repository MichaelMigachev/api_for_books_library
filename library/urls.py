from rest_framework.routers import DefaultRouter

from library.views import (
    BookViewSet,
    AuthorViewSet,
    GenreViewSet,
    RentalViewSet
)

from library.apps import LibraryConfig


app_name = LibraryConfig.name


router = DefaultRouter()
router.register(r"books", BookViewSet, basename="books")
router.register(r"authors", AuthorViewSet, basename="authors")
router.register(r"genres", GenreViewSet, basename="genres")
router.register(r"rent", RentalViewSet, basename="rent")

urlpatterns = []
urlpatterns += router.urls
