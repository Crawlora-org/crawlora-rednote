import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class RednoteClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-rednote-js/0.1.0" });
    this["explore"] = (...args) => this.request("rednote-explore", ...args);
    this["note"] = (...args) => this.request("rednote-note", ...args);
    this["noteComments"] = (...args) => this.request("rednote-note-comments", ...args);
    this["searchSuggest"] = (...args) => this.request("rednote-search-suggest", ...args);
  }
}

export { RednoteClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default RednoteClient;
