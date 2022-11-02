from django.urls import reverse
from companies.models import Company
import json
import pytest


companies_url = reverse("companies-list")
pytestmark = pytest.mark.django_db


# ------------------ Test Get Companies -----------------------
def test_zero_companies_should_return_empty_list(client) -> None:
    response = client.get(companies_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []


def test_one_company_should_succeed(client) -> None:
    test_company = Company.objects.create(name="Amazon")
    response = client.get(companies_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content.get("name") == test_company.name
    assert response_content.get("status") == "Hiring"
    assert response_content.get("application_link") == ""


# ------------------ Test Post Companies ---------------------------
def test_create_company_without_arguments_should_fail(client) -> None:
    response = client.post(companies_url)
    assert response.status_code == 400
    assert json.loads(response.content) == {"name": ["This field is required."]}


def test_create_existing_company_should_fail(client) -> None:
    Company.objects.create(name="Sony")
    response = client.post(companies_url, data={"name": "Sony"})
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "name": ["company with this name already exists."]
    }


def test_create_company_with_only_name_all_fields_should_default(client) -> None:
    response = client.post(companies_url, data={"name": "Test Company"})
    assert response.status_code == 201
    response_content = json.loads(response.content)


def test_create_company_with_layoffs_status_should_succeed(client) -> None:
    response = client.post(
        companies_url, data={"name": "Test Company", "status": "Layoffs"}
    )
    assert response.status_code == 201
    response_content = json.loads(response.content)
    assert response_content.get("status") == "Layoffs"


def test_create_company_with_wrong_status_should_fail(client) -> None:
    incorrect_status_name = "Froze"
    response = client.post(
        companies_url, data={"name": "Test Company", "status": incorrect_status_name}
    )
    assert response.status_code == 400
    assert incorrect_status_name in str(response.content)
