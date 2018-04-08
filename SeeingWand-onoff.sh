#! /bin/sh

### BEGIN INIT INFO
# Provides:          SeeingWand-onoff.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO

# If you want a command to always run, put it here

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting SeeingWand-onoff.py"
    /home/pi/z/SeeingWand-onoff.py &
    ;;
  stop)
    echo "Stopping SeeingWand-onoff.py"
    pkill -f /home/pi/z/SeeingWand-onoff.py
    ;;
  *)
    echo "Usage: /etc/init.d/SeeingWand-onoff.sh {start|stop}"
    exit 1
    ;;
esac

exit 0
