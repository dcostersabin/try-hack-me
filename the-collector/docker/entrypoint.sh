#!/bin/sh

mc alias set s3server $SERVER_URL $ACCESS_KEY $SECRET_KEY

mc admin info s3server

echo "Fetching Subdomains..."

the-collector subdomain --list > /tmp/subdomains.txt

echo "Fetching Ips..."

the-collector ip --list > /tmp/ip.txt

echo "Uploading Results ..."

mc put ./subdomains.txt s3server/the-collector/subdomains.txt

mc put ./ip.txt s3server/the-collector/ip.txt
