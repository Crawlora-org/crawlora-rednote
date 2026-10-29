import { RednoteClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new RednoteClient({ apiKey });

  const explore = await client.explore({  });
  console.log("explore", explore);
  const searchSuggest = await client.searchSuggest({ keyword: "coffee" });
  console.log("searchSuggest", searchSuggest);
