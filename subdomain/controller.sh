#!/bin/bash

start_scan(){
	docker run --rm -e MC_INSECURE=true -e SERVER_URL=$SERVER_URL -e ACCESS_KEY=$ACCESS_KEY -e SECRET_KEY=$SECRET_KEY ghcr.io/dcostersabin/thm_subdomain:latest $1
}

export -f start_scan

SCANNED=$(mc ls subdomains/subdomains --json | jq .key | sed 's/"//g' | sed 's/\///g' | sort | uniq)

DOMAINS=$(curl -s https://raw.githubusercontent.com/projectdiscovery/public-bugbounty-programs/refs/heads/main/chaos-bugbounty-list.json | jq '.programs | map(.domains[])[]' | sort | uniq | sed 's/"//g')

for DOMAIN in $DOMAINS;do

	if [[ ${SCANNED[@]} =~ $DOMAIN ]]
	then
		echo "Skipping Scan For '$DOMAIN'"
	else
		start_scan $DOMAIN
	fi
done


