# Crawlora RedNote JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `4`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rednote | `rednote.explore` | `rednote-explore` | `GET /rednote/explore` | `channel_id` (query string) | `ApiKeyAuth` | `RednoteExploreResponse` |  |
| rednote | `rednote.note` | `rednote-note` | `GET /rednote/note` | `url` (query string)<br>`note_id` (query string) | `ApiKeyAuth` | `RednoteNoteResponse` |  |
| rednote | `rednote.noteComments` | `rednote-note-comments` | `GET /rednote/note-comments` | `url` (query string)<br>`note_id` (query string)<br>`cursor` (query string) | `ApiKeyAuth` | `RednoteNoteCommentsResponse` |  |
| rednote | `rednote.searchSuggest` | `rednote-search-suggest` | `GET /rednote/search-suggest` | `keyword` (query string required) | `ApiKeyAuth` | `RednoteSearchSuggestResponse` |  |
