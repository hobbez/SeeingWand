#! /bin/sh

echo "Setting up Seeing Wand..."

ln -s /home/pi/SeeingWand/SeeingWand.sh /etc/init.d/SeeingWand.sh
update-rc.d SeeingWand.sh defaults
/etc/init.d/SeeingWand.sh start

ln -s /home/pi/SeeingWand/SeeingWand-onoff.sh /etc/init.d/SeeingWand-onoff.sh
update-rc.d SeeingWand-onoff.sh defaults
/etc/init.d/SeeingWand-onoff.sh start

echo "All done. Enjoy!"

exit 0