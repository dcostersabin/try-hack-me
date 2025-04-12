use crate::s3::MinioClient;
use regex::Regex;
use std::collections::HashSet;
pub struct IpCollector {}

impl IpCollector {
    pub fn new() -> Self {
        Self {}
    }

    pub async fn get_all_ips(&mut self) -> Result<HashSet<String>, Box<dyn std::error::Error>> {
        let mut ips: HashSet<String> = HashSet::new();

        let mut minio = MinioClient::new(true, false, "domains".to_string());
        let keys = minio.get_all_keys().await.unwrap();

        for key in keys {
            if key.contains("resp.txt") {
                let re = Regex::new(r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)").unwrap();

                let text = minio.get_object(key).await.unwrap();
                for cap in re.captures_iter(&text) {
                    ips.insert(cap[0].to_string());
                }
            }
        }

        return Ok(ips);
    }
}
