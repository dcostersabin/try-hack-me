#!/bin/sh

DOMAIN=$(echo ${1} |  sed -r 's/\./_/g' )

mc alias set s3server $SERVER_URL $ACCESS_KEY $SECRET_KEY

mc admin info s3server

echo "Running [Nmap] For ${1} ${ip} ..."
nmap  $2 -p- -sC -v -oN "/tmp/port_${2}" -Pn
echo "Uploading Results Of [Nmap] For ${1} ${2} ..."
mc put "/tmp/port_${2}" "s3server/portstore/${DOMAIN}/port-scan/port_${2}"



