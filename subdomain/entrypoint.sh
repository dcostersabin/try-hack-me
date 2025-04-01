#!/bin/sh

touch subdomain.txt

echo "-------Running Subfinder--------"

subfinder -silent -d $1 > subdomain.txt

echo "Found" && cat subdomain.txt | wc -l 

echo "-------Running Scilla--------"

scilla subdomain -oj output -target $1 1>/dev/null && cat output.json | jq .subdomain[] >> subdomain.txt

echo "Found" && cat subdomain.txt | wc -l 

echo "-------Running Subdog--------"

echo $1 | subdog -silent -tools all >> subdomain.txt

echo "Found" && cat subdomain.txt | wc -l 

echo "-------Running Ksubdomain--------"

echo $1 | ksubdomain e --stdin --silent >> subdomain.txt

echo "Found" && cat subdomain.txt | wc -l 

echo "-------Running Amass--------"

amass enum -active -d $1 -p 80,443,8080 >> subdomain.txt

echo "Found" && cat subdomain.txt | wc -l 

cat subdomain.txt
