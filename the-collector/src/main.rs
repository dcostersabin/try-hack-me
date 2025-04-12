mod collector;
mod s3;

use collector::IpCollector;

#[tokio::main]
async fn main() {
    let mut ip_collecotr = IpCollector::new();

    for ip in ip_collecotr.get_all_ips().await.unwrap() {
        println!("{:?}", ip);
    }
}
