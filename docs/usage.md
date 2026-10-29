# RedNote API endpoint reference and client usage

This reference lists all 4 public RedNote API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/rednote`, `crawlora-rednote`, and `crawlora-rednote` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape RedNote locally; Crawlora is independent from and not endorsed by RedNote or its owners.

The package tracks the public API contract revision `sha256:0ff837b756f317110ad2ca6ef655d435cfadae208bc290b059b8c331a50fb015` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `rednote`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `explore` | `explore` | `rednote.explore` | `GET /rednote/explore` | `channel_id` (query, optional) | Anonymous Rednote explore/channel feed |
| `note` | `note` | `rednote.note` | `GET /rednote/note` | `url` (query, optional), `note_id` (query, optional) | Anonymous Rednote note detail |
| `noteComments` | `note_comments` | `rednote.note_comments` | `GET /rednote/note-comments` | `url` (query, optional), `note_id` (query, optional), `cursor` (query, optional) | Anonymous Rednote note comments |
| `searchSuggest` | `search_suggest` | `rednote.search_suggest` | `GET /rednote/search-suggest` | `keyword` (query, required) | Anonymous Rednote search suggestions |

## Client forms

- JavaScript: import `RednoteClient` (also exported as `Client`) from `@crawlora-org/rednote`; use `new RednoteClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `RednoteClient` (also exported as `Client`) from `crawlora_rednote`; use `with RednoteClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncRednoteClient`, used with `async with` and `await`.
- Rust: add `crawlora-rednote` with Cargo; import `Client` and the generated operation parameter struct, then call `client.rednote.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-rednote/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
