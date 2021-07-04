import pytest

@pytest.mark.django_db
def test_Services_Landing(client):
   response = client.get("/Services/")
   assert response.status_code == 200
    
