# KAOS TV

This KAOS TV is a simple and analog way to share media content with the KAOS Berlin comunity. A lokal screen whitch is placed on the way to the kitchen shows the content. People can scan the QR code to get in touch with the Telegram chat boot. Simply put the media you want to share, a photo or videoto in the chat.

The Host Computer can be near to anything, in our case we use a older Intel NUC whitch consume up to 10W and runs Ubuntu 22.04LTS on it.

## Installation
First download and instal Miniconda, we use it with Python Version 3.10.
```
	bash Miniconda3-latest-Linux-x86_64.sh
	conda config --set auto_activate_base false
```
Then install this dependencis:
```	
	sudo apt-get install vlc -y
```

Create the conda enviroment 'kaos_tv' with envirinment.yaml file.
The Telegram Token is passed to the Programm over a env variable.
While deployment, conda do this for us, later the kaos_tv systemd service.
```
	conda env create -f environment.yml
	conda activate kaos_tv
	conda env config vars set TELEG_TOKEN=**the_token**
	conda install -c conda-forge libstdcxx-ng
```

## Autostart
### setup systemctl service
To start the KAOS TV directly after booting, we setup a systemctl servie for the User ktv. 
```
	cp kaos_tv.service /etc/systemd/system/
	chmod 744 start_ktv.sh
	chmod 664 /etc/systemd/system/kaos_tv.service

	systemctl --user daemon-reload
	systemctl --user enable kaos_tv.service 
```
### Proof your systemctl servcie
```
	systemctl --user status kaos_tv.service
	systemctl --user list-unit-files --type=service --state=enabled
	journalctl -u kaos_tv
```

## Logging
The logging is made with python logger. 
To see the live logging use:
```
	tail -f kaos_tv.log
```

	miniconda3/envs/kaos_tv/bin/python kaos_tv/main.py 
## Feature request


