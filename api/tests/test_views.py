from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from api.views import ArticleViewSet
from entries.models import Entry


class ArticleViewSetTests(APITestCase):
    def test_get_list(self):
        url = reverse("article-list")
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_create_article(self):
        User = get_user_model()
        testuser = User.objects.create(username="testuser")
        client = APIClient()
        client.force_authenticate(user=testuser)
        url = reverse("article-list")
        data = {"title": "Great article", "content": "Content for article"}
        response = client.post(url, data=data, format="json")
        assert response.status_code == status.HTTP_201_CREATED


class EntryViewSetTests(APITestCase):
    def test_get_list(self):
        url = reverse("entry-list")
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_create_entry(self):
        User = get_user_model()
        testuser = User.objects.create(username="testuser")
        client = APIClient()
        client.force_authenticate(user=testuser)
        url = reverse("entry-list")
        data = {"title": "Some title", "content": "Some text here"}
        response = client.post(url, data=data, format="json")
        assert response.status_code == status.HTTP_201_CREATED


class CommentListCreateViewTests(APITestCase):
    def test_get_list(self):
        url = reverse("comment-list")
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
