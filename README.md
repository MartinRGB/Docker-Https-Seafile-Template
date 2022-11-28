# Docker-HTTPS-ZFile-Template

1. create ur own CA(optinal) & save to ./proxy/certs

    ```mkcert seafile.local.com localhost 127.0.0.1 172.22.0.20 ::1```

    Install the local CA in the system trust store.

    ```mkcert -install```

2. add these to host(optional) && change `./proxy/conf/nginx.conf` 's `server_name`

    ```server_name seafile.local.com localhost 127.0.0.1 172.22.0.20;```

3. change `./proxy/conf/nginx.conf` 's `proxy_pass` to ur physical ip & port(same port in `docker-compose.yml`)

    ```proxy_pass http://172.22.0.20:8443/;```

4. setup
    ```docker-compose up```

5. 本地存储 -> 文件路径 `/root/zfile/data`

reference -> https://www.howtoforge.com/how-to-create-locally-trusted-ssl-certificates-with-mkcert-on-ubuntu/
   
