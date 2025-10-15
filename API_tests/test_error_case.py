"""Tests for https://http.cat/status/"""

import pytest
import requests
from bs4 import BeautifulSoup

URL = "https://http.cat/status/"


@pytest.fixture
def response():
    """Fixture to get HTTP response."""
    return requests.get(URL, timeout=10)


def test_status_code(response):
    """Test that status code is 403."""
    expected_status_code = 403
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
    """Test that h1 contains '403 Forbidden'."""
    expected_h1 = "403 Forbidden"
    soup = BeautifulSoup(response.text, "html.parser")
    h1 = soup.find("h1").text
    assert (h1 == expected_h1), f"h1 from {URL} is not {expected_h1}"
