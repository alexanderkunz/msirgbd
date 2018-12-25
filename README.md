# MSI-RGBD
Daemon for msi-rgb tool with web interface.
This tool is pretty simple and made for my own personal usage.

## Installing MSI-RGB
A manual installation of msi-rgb, the utility I'm using to set
the colors, is required.

Grab it at https://github.com/nagisa/msi-rgb and compile it.
After you're done, copy the executable to `/usr/local/sbin/msi-rgb`.
Since it requires special permissions, I'd suggest you set the s flag.

    $ cargo build --release
    $ sudo cp ./target/release/msi-rgb /usr/local/sbin/msi-rgb
    $ sudo chmod +s /usr/local/sbin/msi-rgb

## Requirements
Installable via PIP:
- bottle
- noise


    $ sudo pip install bottle noise 

## Run/Debug
For testing/debugging purposes you can run `msirgbd_start.py`.

For actually using it you're better of running the setup and
invoking `msirgbd` in your favorite shell directly

## Configuration
There's no config file or similar thing yet.
Just modify the scripts if you're not happy with what I'm using.

## Installation

    $ sudo python setup.py install

## Service
- Create folder ~/.config/msirgbd
- Create file /etc/systemd/system/msirgbd.service

```INI
[Unit]
Description=MSI-RGB Daemon
After=network.target

[Service]
Type=simple
Restart=always
RestartSec=1
User=[YOUR_USERNAME]
ExecStart=/usr/bin/msirgbd
WorkingDirectory=/home/[YOUR_USERNAME]/.config/msirgbd

[Install]
WantedBy=multi-user.target
```
