import pytest
from bot_engine.utils.Dotenv import Dotenv

@pytest.fixture
def dotenv_instance():
    return Dotenv()

def test_get_existing_key(dotenv_instance):
    result = dotenv_instance.get("MONGODB")
    assert result is None  

def test_get_missing_key(dotenv_instance):
    result = dotenv_instance.get("NON_EXISTENT_KEY")
    assert result is None

def test_get_list(dotenv_instance):
    result = dotenv_instance.get("USER_IDS")
    assert result == [1,2,3,4,55,19]  

