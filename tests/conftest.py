from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture
def client():
    # Arrange
    original_activities = deepcopy(app_module.activities)

    # Act
    with TestClient(app_module.app) as test_client:
        yield test_client

    # Assert
    app_module.activities.clear()
    app_module.activities.update(deepcopy(original_activities))
