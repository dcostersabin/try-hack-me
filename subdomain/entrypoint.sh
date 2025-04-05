#!/bin/sh

DOMAIN=$(echo ${1} |  sed -r 's/\./_/g' )

mc alias set s3server $SERVER_URL $ACCESS_KEY $SECRET_KEY

mc admin info s3server

touch subdomain.txt

echo $1 >> subdomain.txt

echo "Running [Subfinder]..."

subfinder -silent -d $1 > subdomain.txt

echo "Running [Scilla]..."

scilla subdomain -oj output -target $1 1>/dev/null && cat output.json | jq .subdomain[] >> subdomain.txt

echo "Running [Subdog]..."

echo $1 | subdog -silent -tools all >> subdomain.txt

echo "Running [Ksubdomain]..."

echo $1 | ksubdomain e --stdin --silent >> subdomain.txt

echo "Running [Amass]..."

amass enum -active -d $1 >> subdomain.txt

cat subdomain.txt |  grep -oE '([a-zA-Z0-9-]+\.)+[a-zA-Z]+' | sort | uniq > filtered.txt

mc put ./filtered.txt s3server/subdomains/$DOMAIN/subdomains.txt

cat filtered.txt
