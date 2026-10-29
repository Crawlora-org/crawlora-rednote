use crawlora_rednote::{Client, ModelRednoteExploreResponseDoc, RednoteExploreParams};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .rednote
        .explore(RednoteExploreParams {
            ..Default::default()
        })
        .await?;
    let data: ModelRednoteExploreResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
