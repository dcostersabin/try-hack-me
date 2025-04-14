#!/bin/sh

mc alias set s3server $SERVER_URL $ACCESS_KEY $SECRET_KEY

mc admin info s3server

echo "Fetching Subdomains..."

the-collector subdomain --list > /tmp/subdomains.txt

echo "Fetching Ips..."

the-collector ip --list > /tmp/ips.txt

echo "Uploading Results ..."

mc put /tmp/subdomains.txt s3server/the-collector/subdomains.txt

mc put /tmp/ips.txt s3server/the-collector/ips.txt
