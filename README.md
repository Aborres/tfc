![Logo](http://i63.tinypic.com/16aa1km.png) 
# TFC

Tiny FTP Client is an easy to use command line ftp conexion tool.

TFC allows you to control every aspect of an FTP server from your command line.


### Commands:

1. init
2. push
3. pull
4. config
5. dir
6. purgue 

| Commands | Arg             | Action                                                     |
|----------|:---------------:|-----------------------------------------------------------:|
| init     |                 | Creates a ftp client on current folder                     |
|          | -f              | Creates a ftp client erasing possible previous clients     |
|          | -e              | Erases a ftp client on current folder                      |
|          | -c (arg) (arg)  | Clones a ftp client from one folder to another             |
|----------|-----------------|------------------------------------------------------------|
| push     |                 | Uploads default folder (Default Root)                      |
|          | -f  (arg)       | Uploads an especific file or folder                        |
|          | -e  (arg)       | Uploads default folder erasing previous files              |
|          | -ef (arg)       | Uploads an especific file or folder erasing previous files |
|----------|-----------------|------------------------------------------------------------|
| pull     |                 | Downloads all content from server                          |
|          | -f (arg)        | Downloads an especific folder from server                  |
|----------|-----------------|------------------------------------------------------------|
| config   |                 | Shows and sets all configuration info                      |
|          | -u (arg)        | Sets Default user for FTP conexion                         |
|          | -s (arg)        | Sets Default server for FTP conexion                       |
|          | -p (arg)        | Sets Default port for FTP conexion                         |
|          | -ps (arg)       | Sets Default password for FTP conexion                     |
|          | -uf (arg)       | Sets Default upload folder for FTP conexion                |
|          | -df (arg)       | Sets Default download folder for FTP conexion              |
|          | -w (arg)        | Shows welcome to TFC system :)                             |
|          | -i (arg)        | Shows info about the system                                |
|          | -timeout (arg)  | Sets Default time for password timeout                     |
|----------|-----------------|------------------------------------------------------------|
| dir      |                 | Shows content in FTP server                                |
|          | -mkdir (arg)    | Creates a folder in arg route                              |
|          | -ls (arg)       | Lists content of arg folder                                |
|          | -e (arg)        | Erases arg file                                            |
|          | -ef (arg)       | Erases arg folder and all it's content                     |
|----------|-----------------|------------------------------------------------------------|
| purgue   |                 | WARNING: Erases information in Server/Local/DB             |
|          | -l              | Erases all local content in this folder                    |
|          | -s              | Erases all content from ftp server                         |
|          | -db             | Purgues file database                                      |
|----------|:---------------:|-----------------------------------------------------------:|

###Getting Started:

tfc init

tfc config -u (USER)

tfc config -s (SERVER)

tfc config -p (PORT)

tfc config -ps (PASSWORD)

tfc push -f (file/folder)

tfc pull -f (file/folder)

###Example:

tfc init 

tfc config -u USER -s SERVER -p PORT

tfc push -f foo.txt

tfc pull -f foo.txt

tfc (command) -h for more info

tfc (command) -h (Arg) for more specific info
