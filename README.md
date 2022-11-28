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

5. Link:

![1](https://user-images.githubusercontent.com/7036706/204402428-8578e9a3-9cf6-4c8d-84bf-8db1c83dd8a8.png)


   
