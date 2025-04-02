FROM alpine:latest AS go-builder

RUN apk update  && apk upgrade 

RUN apk add go libpcap-dev 

RUN go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest 

RUN go install -v github.com/edoardottt/scilla/cmd/scilla@latest 

RUN go install github.com/rix4uni/subdog@latest 

RUN go install -v github.com/owasp-amass/amass/v4/...@master 

RUN go install -v github.com/boy-hack/ksubdomain/cmd/ksubdomain@latest 

RUN go install -v github.com/projectdiscovery/notify/cmd/notify@latest 

FROM alpine:latest AS runner

RUN apk add libpcap-dev jq sed 

COPY --from=go-builder /root/go/bin/subfinder /bin/

COPY --from=go-builder /root/go/bin/scilla /bin/

COPY --from=go-builder /root/go/bin/subdog /bin/

COPY --from=go-builder /root/go/bin/amass /bin/

COPY --from=go-builder /root/go/bin/ksubdomain /bin/

COPY ./entrypoint.sh .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

