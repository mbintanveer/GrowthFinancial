
import pytest
from django.urls import reverse
from django.test import Client

client=Client()

@pytest.mark.django_db
def test_Vendors_Landing(client):
   response = client.get("/Vendors/")
   assert response.status_code == 200
    
# def test_Vendors_View(client):
#     response = reverse("Vendors/Vendors_View/")
#     assert response.status_code ==200
