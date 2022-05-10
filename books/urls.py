from rest_framework.routers import DefaultRouter

from books.views import AuthorViewSet

router = DefaultRouter()
router.register('author', AuthorViewSet, basename='author')

urlpatterns = router.urls
