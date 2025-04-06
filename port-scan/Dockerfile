FROM alpine:latest AS runner

RUN apk update 

RUN apk add nmap nmap-scripts jq sed  wget 

RUN wget https://dl.min.io/client/mc/release/linux-amd64/mc 

RUN mv /mc /bin/ 

RUN chmod +x /bin/mc 

COPY ./entrypoint.sh .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]


