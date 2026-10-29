"""Typed RedNote client for the Crawlora hosted API."""

from .platform import RednoteClient, AsyncRednoteClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = RednoteClient
AsyncClient = AsyncRednoteClient
__version__ = '0.1.0'
DISPLAY_NAME = 'RedNote'
PLATFORM = 'rednote'
CONTRACT_REVISION = 'sha256:0ff837b756f317110ad2ca6ef655d435cfadae208bc290b059b8c331a50fb015'

__all__ = [
    "RednoteClient", "AsyncRednoteClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
