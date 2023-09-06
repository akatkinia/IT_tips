#!/bin/bash

# description: Simple app
# Required-Start: $syslog $network
. /etc/default/app

case "$1" in
start)
  logger "$(date) service started"
  su user-app -c "java /usr/local/bin/app.jar -Xms1024m -Xmx1024m -Djava.security.egd=file:/dev/./urandom -Djava.awt.headless=true -Djava.io.tmpdir=/tmp -Dspring.config.name=application &"
  echo $!>/var/run/simpleapp.pid
  ;;
stop)
  logger "$(date) service stopped"
  kill `cat /var/run/simpleapp.pid`
  rm /var/run/simpleapp.pid
  ;;
restart)
  $0 stop
  $0 start
  ;;
status)
  if [ -e /var/run/simpleapp.pid ]; then
    echo simpleapp is running, pid=$(cat /var/run/simpleapp.pid)
  else
    echo simpleapp is NOT running
    exit 1
  fi
  ;;
*)
  echo "Usage: $0 (start|stop|status|restart)"
esac

exit 0

