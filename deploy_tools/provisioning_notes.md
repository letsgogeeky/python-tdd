## Required Packages:

* nginx
* Python 3.7
* virtualenv + pip
* Git

eg, on Ubuntu:

```bash
    sudo add-apt-repository ppa:fkrull/deadsnakes
    sudo apt-get install nginx git python37 python3.7-venv
```

## Nginx Virtual host config

* see nginx.template.conf
* replace SITENAME with your own domain name
* Replace SYSTEMUSER with the OS user name

## Systemd service

* see gunicorn-systemd.template.service
* replace SITENAME with your domain name

## Folder structure

Assume we have a user account at /home/username

```
/home/username
└── sites
    └── SITENAME
        |-- database
        |-- source
        |-- static
        |-- virtualenv
```
