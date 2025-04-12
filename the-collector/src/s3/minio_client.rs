use std::env;

use minio_rsc::{
    client::{Bucket, ListObjectsArgs},
    provider::StaticProvider,
    Minio,
};
use reqwest::Client;

pub struct MinioClient {
    endpoint: String,
    bucket_name: String,
    access_key: String,
    secret_key: String,
    secure: bool,
    verify: bool,
}

impl MinioClient {
    pub fn new(secure: bool, verify: bool, bucket_name: String) -> Self {
        Self {
            endpoint: env::var("SERVER_URL")
                .unwrap()
                .replace("https://", "")
                .replace("http://", ""),
            access_key: env::var("ACCESS_KEY").unwrap(),
            secret_key: env::var("SECRET_KEY").unwrap(),
            secure,
            verify,
            bucket_name,
        }
    }

    pub fn client(&mut self) -> Result<Minio, Box<dyn std::error::Error>> {
        let provider = StaticProvider::new(self.access_key.clone(), self.secret_key.clone(), None);
        let client = Client::builder()
            .danger_accept_invalid_certs(!self.verify)
            .build()?;

        return Ok(Minio::builder()
            .endpoint(self.endpoint.clone())
            .provider(provider)
            .client(client)
            .secure(self.secure)
            .build()?);
    }

    pub fn bucket(&mut self) -> Result<Bucket, Box<dyn std::error::Error>> {
        return Ok(self.client()?.bucket(self.bucket_name.clone()));
    }

    pub async fn get_all_keys(&mut self) -> Result<Vec<String>, Box<dyn std::error::Error>> {
        let mut keys: Vec<String> = Vec::new();
        let bucket = self.bucket()?;

        let args = ListObjectsArgs::default().max_keys(1000);

        let objects = bucket.list_objects(args).await?;

        for obj in objects.contents {
            keys.push(obj.key.to_string());
        }

        let mut token = objects.next_continuation_token;

        loop {
            if token == "" {
                break;
            }

            let args = ListObjectsArgs::default()
                .max_keys(1000)
                .continuation_token(token.clone());

            let objects = bucket.list_objects(args.clone()).await.unwrap();

            token = objects.next_continuation_token;

            for object in objects.contents {
                keys.push(object.key.to_string());
            }
        }

        return Ok(keys);
    }

    pub async fn get_object(&mut self, key: String) -> Result<String, Box<dyn std::error::Error>> {
        return Ok(self.bucket()?.get_object(key).await?.text().await.unwrap());
    }
}
