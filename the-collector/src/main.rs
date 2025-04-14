mod collector;
mod s3;
mod utils;

use clap::Parser;
use collector::{IpCollector, Subdomains};
use utils::{Cli, Commands};

#[tokio::main]
async fn main() {
    let cli = Cli::parse();

    match &cli.command {
        Some(Commands::Subdomain { list }) => {
            if *list {
                let mut subdomain = Subdomains::new();
                println!("{:?}", subdomain.get_all_ips().await.unwrap());
            }
        }
        Some(Commands::Ip { list }) => {
            if *list {
                let mut ips = IpCollector::new();
                println!("{:?}", ips.get_all_ips().await.unwrap());
            }
        }
        None => {}
    }
}
