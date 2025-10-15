"""Tests for https://http.cat/status/503"""

import pytest
import requests
from bs4 import BeautifulSoup

URL = "https://http.cat/status/503"


@pytest.fixture
def response():
    """Fixture to get HTTP response."""
    return requests.get(URL, timeout=10)


def test_status_code(response):
    """Test that status code is 200."""
    expected_status_code = 200
    assert (
        response.status_code == expected_status_code
    ), f"Actual status code {response.status_code} is not {expected_status_code}"


def test_content_type_header(response):
    """Test that Content-Type header is text/html."""
    expected_content_type_header = "text/html"
    assert (
        response.headers["Content-Type"] == expected_content_type_header
    ), f"Content-Type header from {URL} is not {expected_content_type_header}"


def test_h1(response):
    """Test that h1 contains '503 Service Unavailable'."""
    expected_h1 = "503 Service Unavailable"
    soup = BeautifulSoup(response.text, "html.parser")
    h1 = soup.find("h1", class_="text-center my-12").text
    assert (h1 == expected_h1), f"h1 from {URL} is not {expected_h1}"
