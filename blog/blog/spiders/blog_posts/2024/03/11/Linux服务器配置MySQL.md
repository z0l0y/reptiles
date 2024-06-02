# 配置MySQL

## 在 Linux 上配置 MySQL 的过程如下：(注意一定要在第一次进去的时候就设置好root用户的密码，要不然后期找临时密码，再修改比较的麻烦)

  1. 安装 MySQL 服务器：

在终端中运行以下命令以安装 MySQL 服务器：

    
        1  
    2  
    

|

    
        sudo apt update  
    sudo apt install mysql-server  
      
  
---|---  
  
安装过程中会提示你设置 MySQL root 用户的密码，请确保设置一个安全且易记的密码。

  2. 配置 MySQL 服务器：

安装完成后，MySQL 服务器会自动启动，并且会在系统的服务列表中注册为 `mysql`。你可以使用以下命令来管理 MySQL 服务器：

     * 启动 MySQL 服务器：`sudo systemctl start mysql`
     * 停止 MySQL 服务器：`sudo systemctl stop mysql`
     * 重启 MySQL 服务器：`sudo systemctl restart mysql`
  3. #### 连接到 MySQL 服务器：

使用以下命令连接到 MySQL 服务器：

    
        1  
    

|

    
        mysql -u root -p  
      
  
---|---  
  
系统会提示你输入 MySQL root 用户的密码。输入密码后，你将进入 MySQL 服务器的命令行界面。

  4. 在 MySQL 中创建新用户和数据库：

在 MySQL 命令行界面中，你可以使用 SQL 语句来创建新用户和数据库。以下是一些常用的命令示例：

     * 创建新用户：
        
                1  
        2  
        

|

        
                CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';  
        请将 `'username'`、`'password'` 和 `'database_name'` 替换为你希望使用的实际值。  
          
  
---|---  
     * 授予用户访问权限：
        
                1  
        2  
        

|

        
                GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'localhost';或  
        grant all privileges on *.* to 'root'@'%' identified by 'password';flush privileges;  
          
  
---|---  
     * 创建新数据库：
        
                1  
        

|

        
                CREATE DATABASE database_name;  
          
  
---|---  
     * 刷新权限：
        
                1  
        

|

        
                FLUSH PRIVILEGES;//让权限立即生效    
          
  
---|---  
  
**修改my.cnf配置文件**

这个是mysql的配置文件，如果你无标题文章找不到在哪里的话，可以输入`find /* -name my.cnf `找到

通过vim编辑该文件，找到`bind-address = 127.0.0.1`这一句，然后在前面加个#号注释掉，保存退出

**重启服务（这点非常重要，不重启就不能实现远程访问数据库）**

    
        1  
    

|

    
        service mysql restart  
      
  
---|---  
  
**在本地远程连接**

在终端输入：

    
        1  
    

|

    
        mysql -h 服务器ip地址 -P 3306 -u root -p  
      
  
---|---  
  
然后输入密码即可。

  5. 退出 MySQL 命令行界面：

在 MySQL 命令行界面中，使用 `exit` 命令退出。

现在你已经成功配置了 MySQL 服务器，并可以通过连接到 MySQL 命令行界面来管理数据库和用户。

## 那我该怎么远程连接到数据库？

要远程连接到数据库，你需要确保以下几点：

  1. 数据库服务器已经启动并正在监听正确的端口。默认情况下，MySQL 数据库使用的是端口 3306。确保数据库服务器正在监听该端口。
  2. 数据库服务器的防火墙允许远程连接。如果你的数据库服务器上有防火墙，确保防火墙规则允许来自远程客户端的连接请求通过指定的端口。这通常需要在防火墙配置中打开端口 3306。
  3. 数据库服务器上的数据库用户已经配置允许远程连接。默认情况下，MySQL 数据库中的 root 用户只允许本地连接。如果你想通过远程连接使用 root 用户，你需要在数据库中修改 root 用户的权限，允许远程连接。

在你的情况下，如果你想通过 SSH 连接到数据库服务器，你可以按照以下步骤进行：

  1. 使用 SSH 连接到远程服务器：运行 `ssh root@192.168.88.131` 命令，连接到远程服务器。
  2. 在远程服务器上，确保数据库已经启动并监听端口 3306。
  3. 确认数据库服务器的防火墙规则允许来自你的客户端的连接请求通过端口 3306。你可能需要配置防火墙规则以允许这样的连接。
  4. 确保你在数据库服务器上创建了允许远程连接的数据库用户。如果你想使用 root 用户进行远程连接，你需要修改 root 用户的权限以允许远程连接。
  5. 使用 MySQL 客户端工具，比如 `mysql` 命令行工具，连接到远程数据库服务器。例如，运行 `mysql -u username -h 192.168.88.131 -p` 命令，其中 `username` 是你在数据库服务器上创建的允许远程连接的用户名。

这样，你就可以通过 SSH
连接到远程服务器，并使用适当的数据库客户端工具连接到数据库服务器进行远程数据库访问。请确保在进行远程连接时遵循安全最佳实践，并采取适当的安全措施来保护数据库和服务器的安全性。

## 关于localhost

在 MySQL 中，`localhost` 是一个特殊的主机名，表示本地主机，即 MySQL 服务器所在的计算机。但是，你可以将 `'localhost'`
替换为其他主机名或 IP 地址，以允许远程主机连接到 MySQL 服务器。

以下是一些常见的选项：

  1. 允许所有主机连接：

如果你希望允许任何主机连接到 MySQL 服务器，请使用 `%` 作为主机名，如下所示：

    
        1  
    

|

    
        CREATE USER 'myuser'@'%' IDENTIFIED BY 'mypassword';  
      
  
---|---  
  
这将为用户 `'myuser'` 创建一个允许从任何主机连接的帐户。

  2. 允许指定的 IP 地址连接：

如果你只想允许特定的 IP 地址连接到 MySQL 服务器，请将 `'localhost'` 替换为该 IP 地址，如下所示：

    
        1  
    

|

    
        CREATE USER 'myuser'@'192.168.0.100' IDENTIFIED BY 'mypassword';  
      
  
---|---  
  
这将为用户 `'myuser'` 创建一个允许从 IP 地址为 `192.168.0.100` 的主机连接的帐户。

请根据你的需求选择适当的主机名或 IP 地址，并相应地设置 MySQL 用户。请记住，为了安全起见，最好仅允许需要访问的主机连接到 MySQL
服务器，并使用强密码保护用户帐户。

## 为什么会ERROR 1396

错误消息 “ERROR 1396 (HY000): Operation CREATE USER failed for ‘root‘@’localhost’”
意味着创建用户 ‘root‘@’localhost’ 失败。

在 MySQL 中，‘root‘@’localhost’ 是默认的超级用户账户，并且在安装 MySQL 时已经存在。由于安全原因，MySQL 不允许通过
CREATE USER 命令创建一个已经存在的用户。

如果你需要更改 ‘root‘@’localhost’ 用户的密码，可以使用以下命令：

    
    
    1  
    

|

    
    
    ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';  
      
  
---|---  
  
请将 `'new_password'` 替换为你希望设置的新密码。这将更改 ‘root‘@’localhost’ 用户的密码为新密码。

请注意，只有具有适当权限的用户才能执行 ALTER USER 命令。如果你没有足够的权限，你可能需要使用具有适当权限的用户账户来执行此操作。

另外，请确保设置强密码来保护 ‘root‘@’localhost’ 用户账户，以确保 MySQL 服务器的安全性。

## 远程访问数据库

要连接到远程数据库，你需要采取以下步骤：

  1. 确保远程数据库服务器可访问：

确保远程数据库服务器处于运行状态，并且网络上可以访问该服务器。你需要知道远程数据库服务器的 IP 地址或主机名。

  2. 允许远程连接到数据库服务器：

默认情况下，MySQL 服务器不允许远程连接。你需要在 MySQL 服务器的配置文件中进行相应的设置，以允许远程连接。配置文件通常是 `my.cnf` 或
`my.ini`，注意是在etc的mysql目录下找。

![image-20240306210605982](https://z0l0y.github.io//2024/03/11/2/image-20240306210605982.png)

打开配置文件，并找到类似于以下行的配置：

    
        1  
    

|

    
        #bind-address = 127.0.0.1  
      
  
---|---  
  
将该行的注释 `#` 去掉，并将 `bind-address` 设置为 MySQL 服务器所在的 IP 地址：

    
        1  
    

|

    
        bind-address = your_server_ip  
      
  
---|---  
  
保存并关闭配置文件，然后重新启动 MySQL 服务器，使更改生效。

  3. 使用远程连接参数连接到数据库：

在命令行或脚本中，使用以下命令连接到远程数据库：

    
        1  
    

|

    
        mysql -h remote_server_ip -P port_number -u username -p  
      
  
---|---  
     * `remote_server_ip`：远程数据库服务器的 IP 地址或主机名。
     * `port_number`：MySQL 服务器的端口号。默认情况下，MySQL 使用 3306 端口。
     * `username`：连接到 MySQL 的用户名。
     * `-p`：提示输入密码。在命令中不指定密码，输入该命令后会要求输入密码。

例如，如果要使用用户名为 `myuser`，密码为 `mypassword` 连接到远程数据库服务器 `192.168.1.100`，使用默认的 3306
端口，命令如下：

    
        1  
    

|

    
        mysql -h 192.168.1.100 -P 3306 -u myuser -p  
      
  
---|---  
  
输入上述命令后，系统会提示输入密码。输入密码后，你将连接到远程数据库服务器。

确保你已经完成了上述步骤，并提供正确的远程数据库服务器的 IP 地址、端口号、用户名和密码。这样，你就可以通过远程连接访问数据库了。

## 关于ini文件

INI 文件是一种普遍用于存储配置数据的文件格式。INI 是 “Initialization” 的缩写，它最初用于 Windows 操作系统的配置文件。

INI
文件具有一种简单的键值对结构，由一系列的节（section）和键值对组成。每个键值对由一个键（key）和一个值（value）组成，它们通过等号（=）或冒号（:）进行分隔。节提供了对键值对进行逻辑分组的一种方式。

以下是一个简单的示例 INI 文件的结构：

    
    
    1  
    2  
    3  
    4  
    5  
    6  
    7  
    8  
    

|

    
    
    ; 这是注释  
    [section1]  
    key1 = value1  
    key2 = value2  
      
    [section2]  
    key3 = value3  
    key4 = value4  
      
  
---|---  
  
在上面的示例中，文件包含两个节（section1 和 section2）。每个节下面有一些键值对。注释以分号（;）开头，用于提供对配置的解释或说明。

INI 文件在多个应用程序和操作系统中被广泛使用，用于存储程序的配置选项、用户首选项和其他相关设置。它们通常是纯文本文件，可以使用文本编辑器进行编辑。

虽然 INI 文件最初是与 Windows 相关的，但现在它已经成为许多不同操作系统和编程语言的通用配置文件格式。

## mysqld是什么？

`mysqld` 是 MySQL 数据库服务器的守护进程或服务进程。

`mysqld` 是 MySQL 服务器的主要组件，负责处理客户端的连接请求、执行 SQL
查询、管理数据库和数据等操作。它是一个长时间运行的进程，通过监听网络端口或套接字接受来自客户端的连接，并提供对 MySQL 数据库的访问。

当你安装和启动 MySQL 数据库服务器时，实际上就是启动 `mysqld` 进程。具体启动 `mysqld`
进程的方式取决于你所使用的操作系统和安装方式。

在 Linux 或 macOS 系统上，你可以使用 `systemctl` 或 `service` 命令来管理 `mysqld`
进程的启动、停止和重启。例如：

    
    
    1  
    2  
    3  
    4  
    5  
    6  
    7  
    8  
    

|

    
    
    # 启动 MySQL 服务  
    sudo systemctl start mysqld  
      
    # 停止 MySQL 服务  
    sudo systemctl stop mysqld  
      
    # 重启 MySQL 服务  
    sudo systemctl restart mysqld  
      
  
---|---  
  
在 Windows 系统上，你可以通过服务管理界面或使用命令行来启动、停止和重启 `mysqld` 进程。

`mysqld` 进程的配置信息通常存储在 MySQL 的配置文件中，例如 `my.cnf` 或
`my.ini`。在配置文件中，你可以指定服务器的端口、数据存储路径、日志文件路径、内存设置等参数。这样，你可以根据需要对 `mysqld`
进程进行自定义配置。

总之，`mysqld` 是 MySQL 数据库服务器的守护进程或服务进程，负责处理客户端请求、执行数据库操作，并提供对 MySQL 数据库的访问

## 查看默认用户的密码

![image-20240306212449294](https://z0l0y.github.io//2024/03/11/2/image-20240306212449294.png)

![image-20240306212731913](https://z0l0y.github.io//2024/03/11/2/image-20240306212731913.png)

## 查看所有用户的信息

要查看当前 MySQL 数据库中有多少用户，你可以执行以下步骤：

  1. 使用合适的 MySQL 客户端连接到 MySQL 服务器。你可以在命令行上使用 `mysql` 命令，或者使用图形化工具如 phpMyAdmin 或 MySQL Workbench。

  2. 连接成功后，在 MySQL 客户端中执行以下 SQL 查询语句：
    
        1  
    

|

    
        SELECT user FROM mysql.user;  
      
  
---|---  
  
这将返回一个结果集，其中包含了所有在 MySQL 数据库中定义的用户列表。

如果你只想要返回用户的数量，可以使用 `COUNT(*)` 聚合函数：

    
        1  
    

|

    
        SELECT COUNT(*) AS user_count FROM mysql.user;  
      
  
---|---  
  
这将返回一个名为 `user_count` 的列，其中显示了用户的数量。

或者是

    
        1  
    

|

    
        select host,user from mysql.user;  
      
  
---|---  

## identified by报错

以上查询将返回 MySQL
数据库中所有用户的列表或用户数量。请注意，这些查询需要具有足够权限的用户才能执行。如果你无法执行这些查询，请确保你使用的用户具有足够的权限来查看用户列表。

MySQL版本8.0.21，在给新用户授权时，执行如下语句：

    
    
    1  
    2  
    

|

    
    
    grant all privileges on *.* to 'root'@'%' identified by '123456' with grant option;  
    1  
      
  
---|---  
  
报错如下：

    
    
    1  
    2  
    

|

    
    
    You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'identified by  'password' with grant option'  
    1  
      
  
---|---  
  
原因分析 ：高版本的MySQL把将创建账户和赋予权限分开了。

解决方法：分开执行。

    
    
    1  
    2  
    3  
    4  
    5  
    6  
    7  
    8  
    

|

    
    
    #创建账户  
    create user 'root'@'%' identified by '123456';  
      
    #赋予权限  
    grant all privileges on *.* to 'root'@'%' with grant option;  
      
    #刷新  
    flush privileges;  
      
  
---|---  
  
## 查看当前用户

    
    
    1  
    

|

    
    
    mysql> select current_user();  
      
  
---|---  
  
![img](https://z0l0y.github.io//2024/03/11/2/1151002-20170525190717763-60562880.png)

## [mysql远程连接只显示部分数据库问题 - 叶落之秋 - 博客园
(cnblogs.com)](https://www.cnblogs.com/gengsc/p/6905536.html)

## 查看用户权限

    
    
    1  
    

|

    
    
    mysql> show grants from current_user();  
      
  
---|---  
  
![img](https://z0l0y.github.io//2024/03/11/2/1151002-20170525190835091-1440680625.png)

我们再查看huohe用户对远程主机的授权。

![img](https://z0l0y.github.io//2024/03/11/2/1151002-20170725100148656-2029272290.png)

# 成功

* * *

_文章作者:_ [zoloy](/about)

_文章链接:_ <http://example.com/2024/03/11/2/>

_版权声明:_ 本博客所有文章除特別声明外，均采用 [CC BY
4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 许可协议。转载请注明来源
[zoloy](/about) !

[ Linux ](/tags/Linux/) [ MySQL ](/tags/MySQL/)

赏

__

#### 你的赏识是我前进的动力

  * 支付宝
  * 微 信

![支付宝打赏二维码](https://z0l0y.github.io//medias/reward/alipay.jpg)

![微信打赏二维码](https://z0l0y.github.io//medias/reward/wechat.png)

