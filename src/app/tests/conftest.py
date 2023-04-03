# pylint: skip-file
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# this is to include backend dir in sys.path so that we can import from db,main.py

from fastapi.testclient import TestClient
from fastapi import FastAPI
import pytest
from typing import Generator
from typing import Any
# from config.Utils import load_routes
from main import api



# def start_application():
#    app = FastAPI()
    # Register routes by Controller
#    for route in load_routes():
#        app.include_router(route)
#    return app


@pytest.fixture(scope="function")
def app() -> Generator[FastAPI, Any, None]:
#    _app = start_application()
    yield api


@pytest.fixture(scope="function")
def client(
    app: FastAPI
) -> Generator[TestClient, Any, None]:
    with TestClient(app) as client:
        yield client