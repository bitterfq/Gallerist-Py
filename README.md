# Gallerist

Discord bot built with Tokio and Serenity in Rust to display the object of the day from the **SAINT LOUIS ART MUSEUM**

ref : <https://www.slam.org/explore-the-collection/object-of-the-day/>

``` Rs

Workflow

1. bot to listen for command
2. deploy webscrapper to ref site
    2.1 Download image locally
    2.2 Formulate the description and metadata details regarding the object
3. and return the object of the day *with details* (optional)

```

## Important Refrences + Notes

1. Serenity examples useful ref: <https://github.com/serenity-rs/serenity/tree/current/examples>

2. Tokio::spawn used for async on message event.

3. Need to implement std::env to take token from terminal

4. Notes on commands ref: <https://betterprogramming.pub/writing-a-discord-bot-in-rust-2d0e50869f64>

5. Add comments

6. Web scrapper, ref: <https://kadekillary.work/post/webscraping-rust/>

7. To select the h tags, ref: <https://docs.rs/scraper/0.12.0/scraper/>

8. Tutorial to download images, ref: <https://www.youtube.com/watch?v=m_agcM_ds1c>

9. Cookbook to download images off the internet and store in temp file, ref: <https://rust-lang-nursery.github.io/rust-cookbook/web/clients/download.html>
