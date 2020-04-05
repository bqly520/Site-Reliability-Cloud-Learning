# Networking

## Sections

* [TCP vs UDP](#tcp-vs-udp)
* [HTTP Status Codes](#http-status-codes)

### TCP vs UDP

**TCP**: *Transmission Control Protocol (TCP)* is a connection-oriented protocol that computers use to communicate over the internet. It is one of the main protocols in TCP/IP networks. For example:
>*Secure Shell (SSH)* or *File Transfer Protocol (FTP, picture messaging)* are examples of services that use TCP protocol because TCP **guarantees** delivery of data and that packets will be delivered in the order they were sent.

**UDP**: *User Datagram Protocol (UDP)* is a connectionless protocol that works just like TCP but assumes that error-checking and recovery services are not required. Instead, UDP continuously sends datagrams to the recipient whether they receive them or not.
>*Streaming videos* or *Online games* are best suited for UDP protocol because these applications or services requires speed and efficiency.

### HTTP Status Codes

- `1xx`: *Informational*, the request has been received and the process is continuing
- `2xx`: *Success*, the action was successfully received, understood, and accepted
    - `200`: OK, the request is OK
- `3xx`: *Redirection*, further action must be taken in order to complete the request
    - `302`: Found, the requested page has moved temporarily to a new url 
- `4xx`: *Client Error*, the request contains incorrect syntax or cannot be fulfilled, usually user error when making HTTP requests
    - `400`: Bad Request, syntax could not be understood
    - `401`: Unauthorized, request not fulfilled due to lack of authorization(needs a username or password)
    - `403`: Forbidden, request is understood but not fulfilled
    - `404`: Not Found, server cannot find the requested page
    - `408`: Request Timeout, request took longer than the server was prepared to wait
- `5xx`: *Server Error*, the server failed to fulfill an apparently valid request
    - `500`: Internal Server Error, the request was not completed because the server met an unexpected condition
    - `503`: Service Unavailable, the server is temporarily overloading or down, unable to temporarily handle requests
    - `504`: Gateway Timeout, gateway has timedout