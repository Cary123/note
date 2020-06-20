# <center>Ubuntu basic command</center>
## Basic  command
### 1.ls 
- list all directory and files
- ls -a: hidden files
- ls -l: details properties
### 2.cd
- cd ~ : Go to home
- cd ~/bin: Go to bin [details](https://www.cnblogs.com/yudar/p/5809219.html)
      /bin/    用以存储二进制可执行命令文件。

      /sbin/    许多系统命令的存储位置，/usr/sbin/中也包括了许多命令。

      /root/    超级用户，即根用户的主目录。

      /home/    普通用户的默认目录，在该目录下，每个用户拥有一个以用户名命名的文件夹。

      /boot/    存放Ubuntu内核和系统启动文件。

      /boot/grub/        Grub引导器相关的文件

      /mnt/     通常包括系统引导后被挂载的文件系统的挂载点。

      /dev/    存储设备文件，包括计算机的所有外部设备，如硬盘、是、键盘、鼠标等。

      /etc/    存放文件管理配置文件和目录（系统文件和大部分应用程序的全局配置文件）。

            /etc/init.d/        SystemV风格的启动脚本

            /etc/rcX.d/        SystenV启动脚本的链接，定义运行级别

            /etc/network/        网络配置文件

            /etc/X11        图形界面配置文件

      /lib/    存储各种程序所需要的共享库文件。

      /lost+found/    一般为空，当非法关机时，会存放一些零散的文件。

      /var/    用于存放很多不断变化的文件，例如日志文件等。

      /usr/    包括与系统用户直接有关的文件和目录

            /usr/bin/        基于用户命令的可执行文件(应用程序)

            /usr/sbin/        管理员应用程序

            /usr/include        编译应用程序所需要的头文件

            /usr/lib/        应用程序库文件（常用的动态链接库和软件包的配置文件）

            /usr/share/        应用程序资源文件

            /usr/src/        应用程序源代码

            /usr/doc        存放文档的目录

            /usr/man        存放帮助文档的目录

            /usr/local/soft/        用户程序

            /usr/local/bin        本地增加的命令

            /usr/local/lib        本地增加的库根文件系统

            /usr/X11R6        图形界面系统(存放x windows的目录)

      /media/    存放Ubuntu系统自动挂载的设备文件。

      /proc/    这是一个虚拟目录，它是内存的映射，包括系统信息和进程信息。

      /tmp/    存储系统和用户的临时信息。

      /initrd/    用来加载启动时临时挂载的initrd.img映像文件，以及载入所要的设备模块目录。

      /opt/    作为可选文件和程序的存放目录，否则将无法引导计算机进入操作系统。

      /srv/    存储系统提供的服务数据。

      /sys/    系统设备和文件层次结构，并向用户程序提供详细的内核数据信息。
### 3. chmod
- x-1 w-2 r-4
- r-read w-write x-execute
- U-User G-Group O-Other
- chmod 777 filename : update rwx for u/g/o role

### 4. file create/delete/move/rename
- touch a.txt : create file a.txt
- mkdir folder : create folder
- rm a.txt : delete a.txt
- rmdir folder : delete folder
- mv : oldname newname (Rename or Move)
