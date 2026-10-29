# Crawlora RedNote API client for Java

The official Java client for Crawlora's hosted RedNote API. It exposes 4 endpoints covering public explore feeds, note details, comments, and search suggestions. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-rednote</artifactId>
  <version>0.1.0</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=rednote-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=rednote-java-console) to get an API key.

```java
import net.crawlora.rednote.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.explore(Map.of());
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported RedNote API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-rednote/blob/main/docs/usage.md) also lists parameters and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/rednote/explore` | `rednote-explore` | Anonymous Rednote explore/channel feed |
| `GET` | `/rednote/note` | `rednote-note` | Anonymous Rednote note detail |
| `GET` | `/rednote/note-comments` | `rednote-note-comments` | Anonymous Rednote note comments |
| `GET` | `/rednote/search-suggest` | `rednote-search-suggest` | Anonymous Rednote search suggestions |

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=rednote-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-rednote)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=rednote-java-api-docs)
