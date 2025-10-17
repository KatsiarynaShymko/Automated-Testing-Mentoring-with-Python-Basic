"""Container for fixtures and hooks"""
import pytest
from app import ECommerceApp

def pytest_runtest_setup(item):
    """Pytest hook which runs before each test"""
    print(f"\nPreparation before test launch: {item.name}")

@pytest.fixture
def created_app():
    """Create an instance of ECommerceApp"""
    return ECommerceApp()

@pytest.fixture
def register_user(created_app):
    """Register user in app"""
    created_app.register_user("Alena", "test123")
    return created_app
