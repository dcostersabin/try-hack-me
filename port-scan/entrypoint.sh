#!/bin/sh

DOMAIN=$(echo ${1} |  sed -r 's/\./_/g' )

mc alias set s3server $SERVER_URL $ACCESS_KEY $SECRET_KEY

mc admin info s3server

mc get s3server/subdomains/$DOMAIN/resp.txt /tmp/resp.txt

ips=$(grep -E -o "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)" /tmp/resp.txt)

echo "Running [Nmap] For ${1} ..."

nmap  $1 -p- -sC -v -oN "/tmp/port_${DOMAIN}" -Pn

mc put "/tmp/port_${DOMAIN}" "s3server/portstore/${DOMAIN}/port-scan/port_${DOMAIN}"

echo "Uploading Results Of [Nmap] For ${1} ..."

for ip in $ips; do
	echo "Running [Nmap] For ${1} ${ip} ..."
	nmap  $1 -p- -sC -v -oN "/tmp/port_${ip}" -Pn
	echo "Uploading Results Of [Nmap] For ${1} ${ip} ..."
	mc put "/tmp/port_${ip}" "s3server/portstore/${DOMAIN}/port-scan/port_${ip}"
done



