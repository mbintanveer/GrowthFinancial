
import pytest
from django.test import Client

client=Client()

@pytest.mark.django_db
def test_Receivings_Landing(client):
   response = client.get("/Vendors/")
   assert response.status_code == 200
    
