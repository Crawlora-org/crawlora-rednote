# Crawlora RedNote API client for Ruby (`crawlora-rednote`)

This Ruby gem calls Crawlora's hosted RedNote API at `https://api.crawlora.net/api/v1`. It exposes 4 endpoints covering public explore feeds, note details, comments, and search suggestions; it does not call or scrape RedNote directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-rednote"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=rednote-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=rednote-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/rednote"

client = Crawlora::Rednote::Client.new
result = client.request("rednote-explore", JSON.parse("{}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 4 API operations.

```ruby
client = Crawlora::Rednote::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported RedNote API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-rednote/blob/main/docs/usage.md) includes parameter and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/rednote/explore` | `rednote-explore` | Anonymous Rednote explore/channel feed |
| `GET` | `/rednote/note` | `rednote-note` | Anonymous Rednote note detail |
| `GET` | `/rednote/note-comments` | `rednote-note-comments` | Anonymous Rednote note comments |
| `GET` | `/rednote/search-suggest` | `rednote-search-suggest` | Anonymous Rednote search suggestions |

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=rednote-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=rednote-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-rednote) for account setup, the API operation reference, and release history.
