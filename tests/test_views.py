import pytest
from app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    with app as testing_client:
        yield testing_client


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"""<div class="screen">0</div>""" in response.data
