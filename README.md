![Logo](http://i63.tinypic.com/16aa1km.png) 
# TFC (ALPHA)

Tiny FTP Client is an easy to use command line ftp conexion tool.

TFC allows to control every aspect of an FTP server from your command line.


### Commands:

1. push
2. pull
3. erase
4. connect
5. close
6. dir
7. clear

| Commands | Arg       | Action                                                     |
|----------|:---------:|-----------------------------------------------------------:|
| push     |           | Uploads default folder                                     |
|          | -f  (arg) | Uploads an especific file or folder                        |
|          | -e  (arg) | Uploads default folder erasing previous files              |
|          | -ef (arg) | Uploads an especific file or folder erasing previous files |
|----------|-----------|------------------------------------------------------------|
| pull     |           | Downloads all content                                      |
|          | -f (arg)  | Downloads an especific folder                              |
|----------|-----------|------------------------------------------------------------|
| config   |           | Shows all configuration info                               |
|          | -u (arg)  | Sets Default user for FTP conexion                         |
|          | -s (arg)  | Sets Default server for FTP conexion                       |
|          | -p (arg)  | Sets Default port for FTP conexion                         |
|          | -ps (arg) | Sets Default password for FTP conexion                     |
|          | -uf (arg) | Sets Default upload folder for FTP conexion                |
|          | -df (arg) | Sets Default download folder for FTP conexion              |
|          | -h (arg)  | Shows help about this command                              |
|          | -w (arg)  | Shows welcome to TFC system :)                             |
|          | -i (arg)  | Shows info about the system                                |

### How to use:

Install binary version (Work In progress)

Or

Copy has much times has you want the raw Python client in every folder you want to work with

###Getting Started:

tfc config -u (USER)
tfc config -s (SERVER)
tfc config -p (PASSWORD)

Defaults folders are optional options only for easy use.

(tfc.py in raw Python versions)

Or

Edit config/config.ini to change full configuration