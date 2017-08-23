# docker-with-flask-run-0.12


Since flask==0.12 introduces a new way to run your app via

```
export FLASK_APP=run.py
flask run
```

Just an example when running it with docker


To run:
`
docker-compose up --build
`


Example output:

```zsh
docker-compose up --build
Building web
Step 1/7 : FROM python:3.6-alpine
 ---> a6beab4fa70b
Step 2/7 : WORKDIR /web
 ---> Using cache
 ---> 4561f5fd9ffa
Step 3/7 : RUN mkdir -p /web
 ---> Using cache
 ---> 3488b84ec177
Step 4/7 : ADD requirements.txt /web/
 ---> Using cache
 ---> 933808133fb9
Step 5/7 : RUN pip install -r requirements.txt
 ---> Using cache
 ---> 0f4ae9343a94
Step 6/7 : ADD . /web
 ---> Using cache
 ---> 348f6f62911f
Step 7/7 : ENV FLASK_APP ./web/run.py
 ---> Using cache
 ---> 5e9abca5b4cc
Successfully built 5e9abca5b4cc
Successfully tagged webapp_web:latest
Recreating webapp_web_1 ...
Starting webapp_redis_1 ...
Recreating webapp_web_1
Recreating webapp_web_1 ... done
Attaching to webapp_redis_1, webapp_web_1
redis_1  | 1:C 23 Aug 02:20:10.204 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
redis_1  | 1:C 23 Aug 02:20:10.204 # Redis version=4.0.1, bits=64, commit=00000000, modified=0, pid=1, just started
redis_1  | 1:C 23 Aug 02:20:10.204 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
redis_1  | 1:M 23 Aug 02:20:10.205 * Running mode=standalone, port=6379.
redis_1  | 1:M 23 Aug 02:20:10.205 # WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
redis_1  | 1:M 23 Aug 02:20:10.205 # Server initialized
redis_1  | 1:M 23 Aug 02:20:10.205 # WARNING you have Transparent Huge Pages (THP) support enabled in your kernel. This will create latency and memory usage issues with Redis. To fix this issue run the command 'echo never > /sys/kernel/mm/transparent_hugepage/enabled' as root, and add it to your /etc/rc.local in order to retain the setting after a reboot. Redis must be restarted after THP is disabled.
redis_1  | 1:M 23 Aug 02:20:10.205 * DB loaded from disk: 0.000 seconds
redis_1  | 1:M 23 Aug 02:20:10.205 * Ready to accept connections
web_1    |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```
