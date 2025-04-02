#!/bin/sh

touch subdomain.txt

echo $1 >> subdomain.txt

echo "-------Running Subfinder--------"

subfinder -silent -d $1 > subdomain.txt

echo "-------Running Scilla--------"

scilla subdomain -oj output -target $1 1>/dev/null && cat output.json | jq .subdomain[] >> subdomain.txt

echo "-------Running Subdog--------"

echo $1 | subdog -silent -tools all >> subdomain.txt

echo "-------Running Ksubdomain--------"

echo $1 | ksubdomain e --stdin --silent >> subdomain.txt

echo "-------Running Amass--------"

amass enum -passive -d $1 >> subdomain.txt

cat subdomain.txt
