use crate::s3::MinioClient;
pub struct Subdomains {}
use regex::Regex;

impl Subdomains {
    pub fn new() -> Self {
        Self {}
    }

    pub async fn get_all_ips(&mut self) -> Result<(), Box<dyn std::error::Error>> {
        let mut minio = MinioClient::new(true, false, "domains".to_string());
        let keys = minio.get_all_keys().await.unwrap();

        for key in keys {
            if key.contains("filtered.txt") {
                let text = minio.get_object(key).await.unwrap().replace("\r", "");

                let re =
                    Regex::new(r"([\w+]+://)?([\w\d-]+\.)*[\w-]+[\.:]\w+([/\?=&\#\.]?[\w-]+)*/?")
                        .unwrap();
                for domain in re.find_iter(&text) {
                    println!("{}", domain.as_str());
                }
            }
        }

        return Ok(());
    }
}
