#!/bin/bash

start_scan(){
	docker run --rm -e MC_INSECURE=true -e SERVER_URL=$SERVER_URL -e ACCESS_KEY=$ACCESS_KEY -e SECRET_KEY=$SECRET_KEY ghcr.io/dcostersabin/thm_port_scanner:latest $1
}

export -f start_scan

TARGET_DOMAINS=$(mc ls s3server/subdomains --json | jq .key | sed 's/"//g' | sed 's/\///g' | sort | uniq)

SCANNED=$(mc ls s3server/portstore --json | jq .key | sed 's/"//g' | sed 's/\///g' | sort | uniq)

for DOMAIN in $TARGET_DOMAINS;do

	if [[ ${SCANNED[@]} =~ $DOMAIN ]]
	then
		echo "Skipping Scan For '$DOMAIN'"
	else
		start_scan $(echo $DOMAIN | sed 's/_/\./g')
	fi
done
