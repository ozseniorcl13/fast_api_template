from fastapi import status
from fastapi.testclient import TestClient

def test_create_profile(client: TestClient):
    data = {
        "name":"new_test",
        "createdBy":"new_test",
        "description":"new_test",
        "projectManager":"new_manager",
    }
    data_response = {
        "name":"new_test",
        "createdBy":"new_test",
        "description":"new_test",
        "onwer":"new_test",
        "projectManager":"new_manager",
        "status":"new_active"
    }
    
    response = client.post('/profile', json=data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == data_response