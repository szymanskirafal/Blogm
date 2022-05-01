from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .views impor ArticleViewSet


class ArticleViewSetTests(APITestCase):
    def test_get_list_view(self:
        url = reverse(ArticleViewSet)
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
 
