from abc import ABC, abstractmethod
from fastapi import FastAPI, APIRouter

class BaseRouter(ABC):
    def __init__(self):
        self._sub_app = FastAPI()
        self._router = APIRouter()
        self._setup_routes()

    @abstractmethod
    def _setup_routes(self):
        raise NotImplementedError("Subclasses should implement this method")

    def get_sub_application(self):
        return self._sub_app
