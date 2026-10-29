# Crawlora RedNote Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `4`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rednote | `rednote.explore` | `rednote-explore` | `GET /rednote/explore` | `channel_id` (query String) | `ApiKeyAuth` | `RednoteExploreResponse` |  |
| rednote | `rednote.note` | `rednote-note` | `GET /rednote/note` | `url` (query String)<br>`note_id` (query String) | `ApiKeyAuth` | `RednoteNoteResponse` |  |
| rednote | `rednote.note_comments` | `rednote-note-comments` | `GET /rednote/note-comments` | `url` (query String)<br>`note_id` (query String)<br>`cursor` (query String) | `ApiKeyAuth` | `RednoteNoteCommentsResponse` |  |
| rednote | `rednote.search_suggest` | `rednote-search-suggest` | `GET /rednote/search-suggest` | `keyword` (query String required) | `ApiKeyAuth` | `RednoteSearchSuggestResponse` |  |
