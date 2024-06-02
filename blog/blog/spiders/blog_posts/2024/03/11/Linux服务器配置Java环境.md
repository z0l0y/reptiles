# 关于Linux服务器上Java的一些问题

## 怎么配置Java环境（千万注意是在profile里面去配置，要不然会错）

  1. 下载 Java JDK：首先，你需要从官方网站下载适用于你的 Linux 发行版的 Java JDK（Java Development Kit）。你可以访问 Oracle 官方网站（[https://www.oracle.com/java/technologies/javase-jdk11-downloads.html）或者](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html%EF%BC%89%E6%88%96%E8%80%85) OpenJDK 官方网站（[https://openjdk.java.net/install/）来获取适合你的发行版的](https://openjdk.java.net/install/%EF%BC%89%E6%9D%A5%E8%8E%B7%E5%8F%96%E9%80%82%E5%90%88%E4%BD%A0%E7%9A%84%E5%8F%91%E8%A1%8C%E7%89%88%E7%9A%84) JDK。

  2. 安装 Java JDK：下载完成后，打开终端，并使用以下命令安装 JDK。根据你的发行版和下载的 JDK 类型，命令可能会有所不同。

     * 对于 Ubuntu / Debian：
        
                1  
        2  
        

|

        
                sudo apt update  
        sudo apt install openjdk-11-jdk  
          
  
---|---  
     * 对于 CentOS / RHEL：
        
                1  
        2  
        

|

        
                sudo yum update  
        sudo yum install java-11-openjdk-devel  
          
  
---|---  
     * 对于其他发行版，你可以按照相应的包管理器和命令进行安装。

  3. 配置环境变量：安装完成后，你需要配置服务器的环境变量，以便系统能够找到 Java 的安装路径。在终端中执行以下命令，打开环境变量配置文件：
    
        1  
    

|

    
        sudo vim /etc/profile  
      
  
---|---  
  
注意注意：

千万不要在environment里面配置，要不然会出问题的。

ps1:

对于大多数 Linux 发行版，系统会自动加载某些全局环境变量配置文件，而无需手动配置。这些配置文件包含系统范围的环境变量设置，可以在用户登录时自动加载。

常见的全局环境变量配置文件包括：

     * `/etc/environment`：这个文件是一个全局的环境变量配置文件，其中定义的变量对所有用户和系统服务都可见。
     * `/etc/profile`：这个文件是一个全局的 shell 配置文件，其中可以包含设置环境变量的语句。
     * `/etc/profile.d/` 目录：该目录包含一系列以 `.sh` 结尾的脚本文件，这些文件中可以设置特定的环境变量。

当你登录到 Linux 系统时，系统会自动加载这些配置文件，并将其中定义的环境变量设置为全局可用的。

需要注意的是，如果你希望在特定用户或特定会话下设置环境变量，可以通过修改用户的 `.bashrc` 或 `.bash_profile`
文件来实现。这些文件位于用户的主目录下，可以在登录时加载用户自定义的环境变量设置。

总之，对于全局环境变量配置，Linux
系统会自动加载预定义的配置文件，无需手动配置。但如果你需要针对特定用户或会话进行环境变量设置，可以修改相应的用户配置文件。

ps2:

在某些 Linux 发行版中，如 Ubuntu，可能没有默认的 `/etc/environment`
文件。这是因为不同的发行版可能采用不同的方式来管理环境变量。

在缺少 `/etc/environment` 文件的情况下，你可以手动创建它。请使用超级用户权限（root）执行以下步骤：

    1. 打开终端，并使用文本编辑器（如 `vim` 或 `nano`）创建 `/etc/profile`文件：
        
                1  
        

|

        
                sudo vi /etc/profile  
          
  
---|---  
    2. 在打开的文件中，按照以下格式添加你的环境变量：
        
                1  
        

|

        
                VARIABLE_NAME="variable_value"  
          
  
---|---  
  
例如：

        
                1  
        2  
        3  
        4  
        

|

        
                export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-11.0.3.7-0.el7_6.aarch64  
        export JRE_HOME=$JAVA_HOME/jre  
        export CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH  
        export PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH  
          
  
---|---  
  
注意，等号两边不要有空格，且值需要使用双引号引起来。

    3. 保存并关闭文件。

    4. 重新登录或重新加载环境变量配置，以使新的环境变量生效。

或者，你可以在当前终端中执行以下命令，立即加载新的环境变量配置：

        
                1  
        

|

        
                source /etc/profile  
          
  
---|---  
  4. 在打开的文件中，添加以下行：

对了，注意一下在vim里面可以用快捷键来复制，ctrl+shift+v即可

    
        1  
    2  
    3  
    4  
    

|

    
        export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-11.0.3.7-0.el7_6.aarch64  
    export JRE_HOME=$JAVA_HOME/jre  
    export CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH  
    export PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH  
      
  
---|---  
  5. 使环境变量生效：执行以下命令以使环境变量生效：
    
        1  
    

|

    
        source /etc/profile  
      
  
---|---  
  6. 验证 Java 安装：执行以下命令验证 Java 是否已成功安装：
    
        1  
    

|

    
        java -version  
      
  
---|---  
  
如果一切顺利，你将看到 Java 的版本信息。

现在，你已经在 Linux 服务器上成功配置了 Java 环境。你可以使用 Java 来运行和管理你的 Java 应用程序。

## 怎么切换Java版本

在 Linux 上切换 Java 的版本，可以使用 `update-alternatives` 命令来管理系统中的多个 Java 安装版本。下面是切换
Java 版本的一般步骤：

  1. 查看可用的 Java 版本：执行以下命令，列出系统中已安装的 Java 版本以及其优先级：
    
        1  
    

|

    
        sudo update-alternatives --config java  
      
  
---|---  
  
这将显示类似以下内容的选项列表：

    
        1  
    2  
    3  
    4  
    5  
    6  
    7  
    8  
    9  
    10  
    

|

    
        有 2 个候选项可用于替换 java (提供 /usr/bin/java)。  
      
      选择       路径                                   优先级  状态  
    ------------------------------------------------------------  
      
    * 0            /usr/lib/jvm/java-11-openjdk-amd64/bin/java   1111      自动模式  
      1            /usr/lib/jvm/java-11-openjdk-amd64/bin/java   1111      手动模式  
      2            /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java   1081      手动模式  
      
    按下 <enter> 保持当前选择[*]或者键入选择的编号：  
      
  
---|---  
  
`*` 符号表示当前选择的 Java 版本。

  2. 选择要使用的 Java 版本：根据列表中的选项，键入对应 Java 版本的编号并按 Enter，或者直接按 Enter 保持当前选择不变。

  3. 验证 Java 版本：执行以下命令，验证已切换到的 Java 版本：
    
        1  
    

|

    
        java -version  
      
  
---|---  
  
这将显示当前正在使用的 Java 版本的信息。

通过上述步骤，你可以在 Linux 上切换系统中可用的 Java 版本，并使用 `update-alternatives` 命令来配置默认的 Java
版本。

## 怎么找到Java的安装路径

你可以通过以下方式来找到你的 Java 安装路径：

  1. 使用 `which` 命令：在终端中执行以下命令，可以查看系统当前默认的 Java 可执行文件的路径：
    
        1  
    

|

    
        which java  
      
  
---|---  
  
这将输出 Java 可执行文件的完整路径，如 `/usr/bin/java`。

  2. 使用 `readlink` 命令：如果你想获取 Java 可执行文件的符号链接的真实路径，可以执行以下命令：
    
        1  
    

|

    
        readlink -f $(which java)  
      
  
---|---  
  
这将输出 Java 可执行文件的真实路径，如 `/usr/lib/jvm/java-11-openjdk-amd64/bin/java`。

  3. 使用 `update-alternatives` 命令：在某些 Linux 发行版中，你可以使用 `update-alternatives` 命令来管理系统中的多个 Java 安装版本。执行以下命令，可以查看当前配置的 Java 选项及其路径：
    
        1  
    

|

    
        update-alternatives --display java  
      
  
---|---  
  
这将显示 Java 的可选配置项列表，包括各个选项的路径。

以上方法中的任何一种都可以帮助你找到 Java 的安装路径。根据你的系统和安装方式，Java 的路径可能会有所不同。

## JAVA_HOME是什么

`JAVA_HOME` 是指定 Java Development Kit (JDK) 的根目录路径。JDK 是用于开发和构建 Java
应用程序的软件包，包括 Java 编译器 (`javac`)、Java 虚拟机 (`java`)、Java 类库和其他开发工具。

通过设置 `JAVA_HOME` 环境变量，你可以指定 JDK 的安装路径，以便系统和应用程序能够找到所需的 Java
运行时环境和开发工具。`JAVA_HOME` 变量应该指向 JDK 安装目录的根路径，其中包含 `bin`、`lib`、`include` 等子目录。

例如，如果你的 JDK 安装路径是 `C:\Program Files\Java\jdk1.8.0_271`（在 Windows 上），那么你可以将
`JAVA_HOME` 设置为 `C:\Program Files\Java\jdk1.8.0_271`。

在设置了正确的 `JAVA_HOME` 后，应用程序和开发工具可以使用该环境变量来定位所需的 Java 运行时环境和工具，例如编译 Java 代码、运行
Java 程序等。

## 怎么查看JAVA_HOME在哪里

要查看 `JAVA_HOME` 环境变量的值和定义位置，可以按照以下步骤进行：

  1. 打开终端。

  2. 运行以下命令来查看 `JAVA_HOME` 环境变量的值：
    
        1  
    

|

    
        echo $JAVA_HOME  
      
  
---|---  
  
这将在终端中显示 `JAVA_HOME` 环境变量的值。如果它已设置，你将看到 Java 的安装路径。

  3. 如果没有显示 `JAVA_HOME` 环境变量的值，说明它可能没有设置。在这种情况下，你可以尝试以下方法来查找定义位置：

     * **查看系统级环境变量文件** ：某些 Linux 发行版会将环境变量设置存储在 `/etc/environment` 文件中。你可以使用文本编辑器打开该文件，并查找是否在其中定义了 `JAVA_HOME` 环境变量。

     * **查看用户级环境变量文件** ：用户级环境变量文件通常是用户主目录下的 `.bashrc` 或 `.bash_profile`。你可以使用文本编辑器打开适用于当前用户的环境变量文件，并搜索是否有关于 `JAVA_HOME` 的定义。

     * **查看特定的 Shell 配置文件** ：如果你在使用特定的 Shell（如 `zsh` 或 `fish`），可以查看该 Shell 的配置文件，例如 `.zshrc` 或 `config.fish`，以寻找 `JAVA_HOME` 的定义。

     * **尝试其他方法** ：如果以上方法都没有找到 `JAVA_HOME` 的定义，你可以尝试运行 `grep` 命令来搜索系统中的所有文件，以查找 `JAVA_HOME` 关键字。例如：
        
                1  
        

|

        
                grep -rnw '/' -e "JAVA_HOME"  
          
  
---|---  
  
这将在整个文件系统中递归搜索包含 `JAVA_HOME` 的文件，并显示匹配的行及其所在文件的路径。

通过上述步骤，你应该能够找到 `JAVA_HOME` 环境变量的值和定义位置。请注意，如果你使用的是 Windows
操作系统，查找环境变量的方法会有所不同。

## 关于环境配置的etc目录

`/etc` 是 Linux 系统中的一个特殊目录，用于存储系统的配置文件。它是 “etcetera”（等等）的缩写，表示其中包含了各种各样的配置文件。

在 `/etc` 目录下，你会找到许多与系统配置相关的文件和子目录。这些文件和目录通常需要超级用户（root）权限才能进行修改。以下是一些常见的
`/etc` 目录下的文件和目录：

  * `/etc/passwd`：包含系统上的用户账户信息。
  * `/etc/group`：包含系统上的用户组信息。
  * `/etc/hosts`：包含主机名与 IP 地址的映射。
  * `/etc/resolv.conf`：设置系统的 DNS 解析配置。
  * `/etc/fstab`：定义系统启动时挂载的文件系统。
  * `/etc/network/interfaces` 或 `/etc/sysconfig/network-scripts`：网络配置文件，用于设置网络接口。
  * `/etc/ssh/sshd_config`：SSH 服务器的配置文件。
  * `/etc/sudoers`：定义系统上的用户和用户组的 sudo 访问权限。
  * `/etc/environment`：全局环境变量的配置文件。

注意一下：

`/etc/environment` 不是一个目录，而是一个文件。

`/etc/environment` 是一个系统级别的环境变量文件，用于定义系统范围的环境变量。它是一个文本文件，通常不包含目录。

`/etc` 目录中的文件和目录通常由系统管理员进行管理和配置。它们是系统范围的配置文件，用于设置各种系统参数、服务和应用程序的行为。因此，对 `/etc`
目录的修改和配置需要谨慎，并且可能需要超级用户权限。

## 关于.bashrc和.bash_profile文件在哪里

![image-20240306192156882](https://z0l0y.github.io//2024/03/11/1/image-20240306192156882.png)

## 关于which软连接

![image-20240306203316460](https://z0l0y.github.io//2024/03/11/1/image-20240306203316460-1710152979673.png)

* * *

_文章作者:_ [zoloy](/about)

_文章链接:_ <http://example.com/2024/03/11/1/>

_版权声明:_ 本博客所有文章除特別声明外，均采用 [CC BY
4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 许可协议。转载请注明来源
[zoloy](/about) !

[ Linux ](/tags/Linux/) [ Java ](/tags/Java/)

赏

__

#### 你的赏识是我前进的动力

  * 支付宝
  * 微 信

![支付宝打赏二维码](https://z0l0y.github.io//medias/reward/alipay.jpg)

![微信打赏二维码](https://z0l0y.github.io//medias/reward/wechat.png)

