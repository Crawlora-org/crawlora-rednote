# Crawlora RedNote API client for PHP (`crawlora/rednote`)

This PHP package calls Crawlora's hosted RedNote API at `https://api.crawlora.net/api/v1`. It exposes 4 endpoints covering public explore feeds, note details, comments, and search suggestions. It does not call or scrape RedNote directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/rednote
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=rednote-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=rednote-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Rednote\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("rednote-explore", []);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 4 API operations.

## Supported RedNote API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-rednote/blob/main/docs/usage.md) includes parameter and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/rednote/explore` | `rednote-explore` | Anonymous Rednote explore/channel feed |
| `GET` | `/rednote/note` | `rednote-note` | Anonymous Rednote note detail |
| `GET` | `/rednote/note-comments` | `rednote-note-comments` | Anonymous Rednote note comments |
| `GET` | `/rednote/search-suggest` | `rednote-search-suggest` | Anonymous Rednote search suggestions |

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=rednote-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=rednote-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-rednote). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-rednote/blob/main/docs/usage.md).
