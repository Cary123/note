# <center>My SQL Server 5.7.30 配置</center>

### 配置安装
* 下载MySQL Community Server 5.7.30 版本
* > https://dev.mysql.com/downloads/mysql/
* 解压
* 配置D:\software\mysql-5.7.30\bin到环境变量
* 在根目录D:\software\mysql-5.7.30新建一个my.ini文件，编辑内容如下：
    ```ini
    [client]
    port=3306
    default-character-set=utf8

    [mysql]
    default-character-set=utf8 

    [mysqld]
    skip-grant-tables
    port=3306
    character-set-server=utf8
    basedir=D:\\software\\mysql-5.7.30
    datadir=D:\\software\\mysql-5.7.30\\data
    sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES
    max_connections=200
    default-storage-engine=INNODB
    explicit_defaults_for_timestamp=1

    [WinMySQLAdmin]
    D:\\software\\mysql-5.7.30\\bin\\mysqld.exe
    ```
* cmd控制台切换到D:\software\mysql-5.7.30\bin目录，依次执行如下命令
    ``` powershell

    mysqld install
    安装mysql服务，任务管理器服务里面可以查看是否安装成功

    mysqld –-initialize   
    初始化data目录，5.7版本不含该目录，如果报错可以手动创建目录再执
    行命令

    net start mysql
    启动服务

    net stop mysql
    停止服务

    mysqld remove
    如果前面步骤执行完，启动服务报错，可以执行此命令移除服务再试
    ```

* 登录mysql
    ```
    mysql -u root -p
    空密码登录

    如果拒绝登录 ”Access denied for user ‘root’@’localhost’ (using password: YES)”

    net stop mysql （停止服务）

    mysqld –skip-grant-tables

    修改 root密码方式

    a. 使用mysqladmin语法：mysqladmin -u用户名 -p旧密码 password 新密码 
    例如：mysqladmin -u root -p 123 password 456；

    b.直接修改user表的用户口令： 
    use mysql;
    update user set authentication_string=password(“xxxxxx”) where user=“root”;      
    flush privileges;

    删除my.ini中
    skip-grant-tables
    重启服务

    ```

### 

