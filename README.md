# RedNote clients for Crawlora

Official Crawlora client packages for the hosted RedNote API. Access 4 API endpoints covering public explore feeds, note details, comments, and search suggestions from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape RedNote locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by RedNote or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/rednote`](javascript/README.md)
- Python: [`crawlora-rednote`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-rednote`](go.mod)
- Ruby: [`crawlora-rednote`](ruby/README.md)
- Java: [`net.crawlora:crawlora-rednote:0.1.0`](java/README.md)
- PHP: [`crawlora/rednote`](php/README.md)
- Rust: [`crawlora-rednote`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=rednote-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=rednote-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=rednote-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 4 selected public RedNote API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/rednote/explore` | `rednote-explore` | Anonymous Rednote explore/channel feed |
| `GET` | `/rednote/note` | `rednote-note` | Anonymous Rednote note detail |
| `GET` | `/rednote/note-comments` | `rednote-note-comments` | Anonymous Rednote note comments |
| `GET` | `/rednote/search-suggest` | `rednote-search-suggest` | Anonymous Rednote search suggestions |

## License

MIT. See [LICENSE](LICENSE).
