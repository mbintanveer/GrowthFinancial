
import pytest
from django.urls import reverse
from django.test import Client

client=Client()

# @pytest.fixture()
# def admin_client(client, admin_user):
#     client.force_login(admin_user)
    # return client

# @pytest.mark.django_db
# def test_admin_page(admin_client):
#    response = admin_client.get("/Vendors/")
#    assert response.status_code == 200

@pytest.mark.django_db
def test_Vendors_Landing(client):
   response = client.get("/Vendors/")
   assert response.status_code == 200
    
# def test_Vendors_View(client):
#     response = reverse("Vendors/Vendors_View/")
#     assert response.status_code ==200
