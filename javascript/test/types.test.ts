import { RednoteClient } from "../src/index.js";

const client = new RednoteClient({ apiKey: "test-key" });
void client.searchSuggest({"keyword": "sample"});
void client.request("rednote-search-suggest", {"keyword": "sample"});
const streamResponse: Promise<Response> = client.request("rednote-search-suggest", {"keyword": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("rednote-search-suggest", {"keyword": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.searchSuggest({"keyword": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("rednote-search-suggest", {"keyword": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("rednote-search-suggest", {"keyword": "sample"}, { responseType: "text" });
void rawText;


void client.explore();
void client.request("rednote-explore");
// @ts-expect-error The selected operation requires its documented params.
void client.searchSuggest();
