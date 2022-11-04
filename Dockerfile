FROM golang:alpine3.16 AS builder
WORKDIR /app
COPY go.mod go.sum *.go ./
RUN go mod download && go build -o server.cgo

FROM alpine:latest  
ENV PORT=3000
WORKDIR /server/
RUN apk --no-cache add ca-certificates dumb-init
COPY --from=builder /app/server.cgo ./
EXPOSE 3000
HEALTHCHECK CMD wget -q --spider  http://localhost:3000/health || exit 1
ENTRYPOINT [ "dumb-init" ]
CMD ["./server.cgo"] 
