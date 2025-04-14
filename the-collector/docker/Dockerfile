FROM rust:1.86 AS builder

RUN apt-get update  && apt-get install musl-tools -y

RUN rustup target add x86_64-unknown-linux-musl

WORKDIR /app

COPY . .

RUN cargo build --release --target x86_64-unknown-linux-musl

FROM alpine:latest  AS runner

RUN apk update 

RUN apk add wget  

RUN wget https://dl.min.io/client/mc/release/linux-amd64/mc 

RUN mv /mc /bin/ 

RUN chmod +x /bin/mc 

COPY ./docker/entrypoint.sh .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

COPY --from=builder /app/target/x86_64-unknown-linux-musl/release/the-collector /bin/the-collector


