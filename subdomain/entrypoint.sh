#!/bin/sh

DOMAIN=$(echo ${1} |  sed -r 's/\./_/g' )

mc alias set s3server $SERVER_URL $ACCESS_KEY $SECRET_KEY

mc admin info s3server

touch subdomain.txt

echo "-----[ SCAN STARTED (${1}) ]-----"

echo $1 >> subdomain.txt

echo $1 >> resp.txt

echo "Running [Subfinder]..."

subfinder -silent -d $1 | dnsx -silent >> subdomain.txt

echo "Running [Scilla]..."

scilla subdomain -oj output -target $1 && cat output.json | jq .subdomain[] >> subdomain.txt

echo "Running [Subdog]..."

echo $1 | subdog -silent -tools all >> subdomain.txt

echo "Running [Ksubdomain]..."

echo $1 | ksubdomain e --stdin --silent >> subdomain.txt


echo "Running [Amass]..."

amass enum -active -timeout 10 -d $1 >> amass.txt

cat amass.txt | grep -oE '([a-zA-Z0-9-]+\.)+[a-zA-Z]+' | sort | uniq >> subdomain.txt

cat subdomain.txt | sort | uniq > filtered.txt

echo "Running [DNSX]..."

cat filtered.txt | dnsx -silent -a -resp >> resp.txt


echo "Uploading Scanned Results"

mc put ./subdomain.txt s3server/subdomains/$DOMAIN/subdomain.txt

mc put ./filtered.txt s3server/subdomains/$DOMAIN/filtered.txt

mc put ./amass.txt s3server/subdomains/$DOMAIN/amass.txt

mc put ./resp.txt s3server/subdomains/$DOMAIN/resp.txt

cat filtered.txt
