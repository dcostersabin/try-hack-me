use crate::s3::MinioClient;
pub struct Subdomains {}

impl Subdomains {
    pub fn new() -> Self {
        Self {}
    }

    pub async fn get_all_ips(&mut self) -> Result<(), Box<dyn std::error::Error>> {
        let mut minio = MinioClient::new(true, false, "domains".to_string());
        let keys = minio.get_all_keys().await.unwrap();

        for key in keys {
            if key.contains("filtered.txt") {
                let text = minio
                    .get_object(key)
                    .await
                    .unwrap()
                    .replace("\r", "")
                    .replace("\"", "");

                let lines = text.split("\n");

                for line in lines {
                    let col: Vec<&str> = line.split(" ").collect();
                    if col.len() > 0 {
                        let domain: Vec<&str> = col[0].split(".").collect();
                        if !col[0].contains("*")
                            && !col[0].contains("{")
                            && !col[0].contains("}")
                            && domain.len() > 1
                        {
                            println!("{}", col[0]);
                        }
                    }
                }
            }
        }

        return Ok(());
    }
}
