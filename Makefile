
all:
	pytest

install:
	mkdir -p /usr/local/pi-client
	mkdir -p /var/log/pi-client
	cp -r . /usr/local/pi-client
	cp etc/init.d/pi-client /etc/init.d/pi-client
	chmod +x /usr/local/pi-client/bin/*
	chmod +x /etc/init.d/pi-client

uninstall:
	rm -fR /usr/local/pi-client
	rm -f /etc/init.d/pi-client

