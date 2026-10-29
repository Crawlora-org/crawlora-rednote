from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelRednoteSuggestResponseDoc = TypedDict('ModelRednoteSuggestResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRednoteSuggestResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRednoteSuggestResponse = TypedDict('ModelRednoteSuggestResponse', {
    'count': NotRequired[int],
    'items': NotRequired[list[ModelRednoteSuggestItem]],
    'keyword': NotRequired[str],
    'search_cpl_id': NotRequired[str],
    'word_request_id': NotRequired[str],
}, total=False)

ModelRednoteSuggestItem = TypedDict('ModelRednoteSuggestItem', {
    'highlight_flags': NotRequired[list[bool]],
    'search_type': NotRequired[str],
    'text': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelRednoteCommentsResponseDoc = TypedDict('ModelRednoteCommentsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRednoteCommentsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRednoteCommentsResponse = TypedDict('ModelRednoteCommentsResponse', {
    'count': NotRequired[int],
    'cursor': NotRequired[str],
    'has_more': NotRequired[bool],
    'items': NotRequired[list[ModelRednoteComment]],
    'note_id': NotRequired[str],
}, total=False)

ModelRednoteComment = TypedDict('ModelRednoteComment', {
    'author': NotRequired[ModelRednoteCommentAuthor],
    'comment_id': NotRequired[str],
    'content': NotRequired[str],
    'created_at': NotRequired[int],
    'ip_location': NotRequired[str],
    'like_count': NotRequired[int],
    'sub_comment_count': NotRequired[int],
    'sub_comments': NotRequired[list[ModelRednoteComment]],
}, total=False)

ModelRednoteCommentAuthor = TypedDict('ModelRednoteCommentAuthor', {
    'avatar_url': NotRequired[str],
    'nickname': NotRequired[str],
    'user_id': NotRequired[str],
}, total=False)

ModelRednoteNoteResponseDoc = TypedDict('ModelRednoteNoteResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRednoteNoteResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRednoteNoteResponse = TypedDict('ModelRednoteNoteResponse', {
    'author': NotRequired[ModelRednoteNoteAuthor],
    'description': NotRequired[str],
    'image_urls': NotRequired[list[str]],
    'note_id': NotRequired[str],
    'published_at': NotRequired[str],
    'stats': NotRequired[ModelRednoteNoteStats],
    'tags': NotRequired[list[ModelRednoteNoteTag]],
    'title': NotRequired[str],
    'type': NotRequired[str],
    'url': NotRequired[str],
    'video_duration_seconds': NotRequired[float],
    'video_url': NotRequired[str],
}, total=False)

ModelRednoteNoteTag = TypedDict('ModelRednoteNoteTag', {
    'id': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelRednoteNoteStats = TypedDict('ModelRednoteNoteStats', {
    'collected_count': NotRequired[int],
    'comment_count': NotRequired[int],
    'liked_count': NotRequired[int],
    'share_count': NotRequired[int],
}, total=False)

ModelRednoteNoteAuthor = TypedDict('ModelRednoteNoteAuthor', {
    'avatar_url': NotRequired[str],
    'nickname': NotRequired[str],
    'user_id': NotRequired[str],
}, total=False)

ModelRednoteExploreResponseDoc = TypedDict('ModelRednoteExploreResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRednoteExploreResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRednoteExploreResponse = TypedDict('ModelRednoteExploreResponse', {
    'channel_id': NotRequired[str],
    'channels': NotRequired[list[ModelRednoteChannel]],
    'count': NotRequired[int],
    'items': NotRequired[list[ModelRednoteExploreCard]],
}, total=False)

ModelRednoteExploreCard = TypedDict('ModelRednoteExploreCard', {
    'author': NotRequired[ModelRednoteNoteAuthor],
    'cover_url': NotRequired[str],
    'liked_count': NotRequired[int],
    'note_id': NotRequired[str],
    'note_url': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[str],
    'xsec_token': NotRequired[str],
}, total=False)

ModelRednoteChannel = TypedDict('ModelRednoteChannel', {
    'id': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

RednoteExploreResponse = ModelRednoteExploreResponseDoc
RednoteExploreParams = TypedDict('RednoteExploreParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'channel_id': NotRequired[str],
}, total=False)

RednoteNoteResponse = ModelRednoteNoteResponseDoc
RednoteNoteParams = TypedDict('RednoteNoteParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'url': NotRequired[str],
    'note_id': NotRequired[str],
}, total=False)

RednoteNoteCommentsResponse = ModelRednoteCommentsResponseDoc
RednoteNoteCommentsParams = TypedDict('RednoteNoteCommentsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'url': NotRequired[str],
    'note_id': NotRequired[str],
    'cursor': NotRequired[str],
}, total=False)

RednoteSearchSuggestResponse = ModelRednoteSuggestResponseDoc
RednoteSearchSuggestParams = TypedDict('RednoteSearchSuggestParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
}, total=False)

class RednoteGroup:
    @overload
    def explore(self, **params: Unpack[RednoteExploreStreamParams]) -> BinaryIO: ...
    @overload
    def explore(self, **params: Unpack[RednoteExploreTextResponseParams]) -> str: ...
    @overload
    def explore(self, **params: Unpack[RednoteExploreDefaultParams]) -> RednoteExploreResponse: ...
    @overload
    def note(self, **params: Unpack[RednoteNoteStreamParams]) -> BinaryIO: ...
    @overload
    def note(self, **params: Unpack[RednoteNoteTextResponseParams]) -> str: ...
    @overload
    def note(self, **params: Unpack[RednoteNoteDefaultParams]) -> RednoteNoteResponse: ...
    @overload
    def note_comments(self, **params: Unpack[RednoteNoteCommentsStreamParams]) -> BinaryIO: ...
    @overload
    def note_comments(self, **params: Unpack[RednoteNoteCommentsTextResponseParams]) -> str: ...
    @overload
    def note_comments(self, **params: Unpack[RednoteNoteCommentsDefaultParams]) -> RednoteNoteCommentsResponse: ...
    @overload
    def search_suggest(self, **params: Unpack[RednoteSearchSuggestStreamParams]) -> BinaryIO: ...
    @overload
    def search_suggest(self, **params: Unpack[RednoteSearchSuggestTextResponseParams]) -> str: ...
    @overload
    def search_suggest(self, **params: Unpack[RednoteSearchSuggestDefaultParams]) -> RednoteSearchSuggestResponse: ...

OperationId = Literal[
    'rednote-explore',
    'rednote-note',
    'rednote-note-comments',
    'rednote-search-suggest',
]

class CrawloraClient:
    rednote: RednoteGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['rednote-explore'],
        params: RednoteExploreParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RednoteExploreResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['rednote-note'],
        params: RednoteNoteParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RednoteNoteResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['rednote-note-comments'],
        params: RednoteNoteCommentsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RednoteNoteCommentsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['rednote-search-suggest'],
        params: RednoteSearchSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RednoteSearchSuggestResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['rednote-explore'],
        params: RednoteExploreParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RednoteExploreResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['rednote-note'],
        params: RednoteNoteParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RednoteNoteResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['rednote-note-comments'],
        params: RednoteNoteCommentsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RednoteNoteCommentsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['rednote-search-suggest'],
        params: RednoteSearchSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RednoteSearchSuggestResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class RednoteClient(CrawloraClient):
    def __enter__(self) -> RednoteClient: ...
    @overload
    def explore(self, **params: Unpack[RednoteExploreStreamParams]) -> BinaryIO: ...
    @overload
    def explore(self, **params: Unpack[RednoteExploreTextResponseParams]) -> str: ...
    @overload
    def explore(self, **params: Unpack[RednoteExploreDefaultParams]) -> RednoteExploreResponse: ...
    @overload
    def note(self, **params: Unpack[RednoteNoteStreamParams]) -> BinaryIO: ...
    @overload
    def note(self, **params: Unpack[RednoteNoteTextResponseParams]) -> str: ...
    @overload
    def note(self, **params: Unpack[RednoteNoteDefaultParams]) -> RednoteNoteResponse: ...
    @overload
    def note_comments(self, **params: Unpack[RednoteNoteCommentsStreamParams]) -> BinaryIO: ...
    @overload
    def note_comments(self, **params: Unpack[RednoteNoteCommentsTextResponseParams]) -> str: ...
    @overload
    def note_comments(self, **params: Unpack[RednoteNoteCommentsDefaultParams]) -> RednoteNoteCommentsResponse: ...
    @overload
    def search_suggest(self, **params: Unpack[RednoteSearchSuggestStreamParams]) -> BinaryIO: ...
    @overload
    def search_suggest(self, **params: Unpack[RednoteSearchSuggestTextResponseParams]) -> str: ...
    @overload
    def search_suggest(self, **params: Unpack[RednoteSearchSuggestDefaultParams]) -> RednoteSearchSuggestResponse: ...

class AsyncRednoteClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncRednoteClient: ...
    rednote: _AsyncRednoteGroup
    @overload
    async def explore(self, **params: Unpack[RednoteExploreStreamParams]) -> BinaryIO: ...
    @overload
    async def explore(self, **params: Unpack[RednoteExploreTextResponseParams]) -> str: ...
    @overload
    async def explore(self, **params: Unpack[RednoteExploreDefaultParams]) -> RednoteExploreResponse: ...
    @overload
    async def note(self, **params: Unpack[RednoteNoteStreamParams]) -> BinaryIO: ...
    @overload
    async def note(self, **params: Unpack[RednoteNoteTextResponseParams]) -> str: ...
    @overload
    async def note(self, **params: Unpack[RednoteNoteDefaultParams]) -> RednoteNoteResponse: ...
    @overload
    async def note_comments(self, **params: Unpack[RednoteNoteCommentsStreamParams]) -> BinaryIO: ...
    @overload
    async def note_comments(self, **params: Unpack[RednoteNoteCommentsTextResponseParams]) -> str: ...
    @overload
    async def note_comments(self, **params: Unpack[RednoteNoteCommentsDefaultParams]) -> RednoteNoteCommentsResponse: ...
    @overload
    async def search_suggest(self, **params: Unpack[RednoteSearchSuggestStreamParams]) -> BinaryIO: ...
    @overload
    async def search_suggest(self, **params: Unpack[RednoteSearchSuggestTextResponseParams]) -> str: ...
    @overload
    async def search_suggest(self, **params: Unpack[RednoteSearchSuggestDefaultParams]) -> RednoteSearchSuggestResponse: ...

class _AsyncRednoteGroup:
    @overload
    async def explore(self, **params: Unpack[RednoteExploreStreamParams]) -> BinaryIO: ...
    @overload
    async def explore(self, **params: Unpack[RednoteExploreTextResponseParams]) -> str: ...
    @overload
    async def explore(self, **params: Unpack[RednoteExploreDefaultParams]) -> RednoteExploreResponse: ...
    @overload
    async def note(self, **params: Unpack[RednoteNoteStreamParams]) -> BinaryIO: ...
    @overload
    async def note(self, **params: Unpack[RednoteNoteTextResponseParams]) -> str: ...
    @overload
    async def note(self, **params: Unpack[RednoteNoteDefaultParams]) -> RednoteNoteResponse: ...
    @overload
    async def note_comments(self, **params: Unpack[RednoteNoteCommentsStreamParams]) -> BinaryIO: ...
    @overload
    async def note_comments(self, **params: Unpack[RednoteNoteCommentsTextResponseParams]) -> str: ...
    @overload
    async def note_comments(self, **params: Unpack[RednoteNoteCommentsDefaultParams]) -> RednoteNoteCommentsResponse: ...
    @overload
    async def search_suggest(self, **params: Unpack[RednoteSearchSuggestStreamParams]) -> BinaryIO: ...
    @overload
    async def search_suggest(self, **params: Unpack[RednoteSearchSuggestTextResponseParams]) -> str: ...
    @overload
    async def search_suggest(self, **params: Unpack[RednoteSearchSuggestDefaultParams]) -> RednoteSearchSuggestResponse: ...

RednoteExploreDefaultParams = TypedDict('RednoteExploreDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'channel_id': NotRequired[str],
}, total=False)

RednoteExploreTextResponseParams = TypedDict('RednoteExploreTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'channel_id': NotRequired[str],
}, total=False)

RednoteExploreStreamParams = TypedDict('RednoteExploreStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'channel_id': NotRequired[str],
}, total=False)

RednoteNoteDefaultParams = TypedDict('RednoteNoteDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'url': NotRequired[str],
    'note_id': NotRequired[str],
}, total=False)

RednoteNoteTextResponseParams = TypedDict('RednoteNoteTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'url': NotRequired[str],
    'note_id': NotRequired[str],
}, total=False)

RednoteNoteStreamParams = TypedDict('RednoteNoteStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'url': NotRequired[str],
    'note_id': NotRequired[str],
}, total=False)

RednoteNoteCommentsDefaultParams = TypedDict('RednoteNoteCommentsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'url': NotRequired[str],
    'note_id': NotRequired[str],
    'cursor': NotRequired[str],
}, total=False)

RednoteNoteCommentsTextResponseParams = TypedDict('RednoteNoteCommentsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'url': NotRequired[str],
    'note_id': NotRequired[str],
    'cursor': NotRequired[str],
}, total=False)

RednoteNoteCommentsStreamParams = TypedDict('RednoteNoteCommentsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'url': NotRequired[str],
    'note_id': NotRequired[str],
    'cursor': NotRequired[str],
}, total=False)

RednoteSearchSuggestDefaultParams = TypedDict('RednoteSearchSuggestDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
}, total=False)

RednoteSearchSuggestTextResponseParams = TypedDict('RednoteSearchSuggestTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
}, total=False)

RednoteSearchSuggestStreamParams = TypedDict('RednoteSearchSuggestStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
}, total=False)
