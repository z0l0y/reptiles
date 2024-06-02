# 编译部署的流程

## **1.写完后端代码，并且编译无误后，通过Maven来package项目，得到项目的jar包。**

## **2.在Ubuntu服务器上部署数据库MariaDB，并且创建DB用户，设置密码。**

## **3.安装jdk，配置好Java对应的环境，使jar包可以正常运行即可。**

##
**4.将本地的数据库进行dump，修改字符编码为utf8mb4_general_ci，得到data.sql文件，并上传到服务器，便于进行建表操作。进入MariaDB，建立数据库，将data.sql导入数据库，成功建表。**

##
**5.在服务器上创建backend的文件夹，将jar包上传到服务器，并且写start.sh和stop.sh脚本，定义日志文件路径，便于查看出现的问题**

## **6.部署成功**

* * *

_文章作者:_ [zoloy](/about)

_文章链接:_
<http://example.com/2024/03/11/%E7%BC%96%E8%AF%91%E9%83%A8%E7%BD%B2%E7%9A%84%E6%B5%81%E7%A8%8B/>

_版权声明:_ 本博客所有文章除特別声明外，均采用 [CC BY
4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 许可协议。转载请注明来源
[zoloy](/about) !

[ Java ](/tags/Java/) [ Maven ](/tags/Maven/) [ Ubuntu ](/tags/Ubuntu/) [
MariaDB ](/tags/MariaDB/) [ shell脚本 ](/tags/shell%E8%84%9A%E6%9C%AC/)

赏

__

#### 你的赏识是我前进的动力

  * 支付宝
  * 微 信

![支付宝打赏二维码](https://z0l0y.github.io//medias/reward/alipay.jpg)

![微信打赏二维码](https://z0l0y.github.io//medias/reward/wechat.png)

