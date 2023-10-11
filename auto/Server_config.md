## 服务器配置

### JDK配置

1. 先批量卸载jkd

- `rpm -qa | grep jdk | xargs rpm -e --nodeps`
- `rpm -qa | grep java | xargs rpm -e --nodeps`

2. 安装JDK11

- `yum install -y java-11-openjdk java-11-openjdk-devel`
- 如果显示的是/usr/bin/java请执行下面命令
- `ls -lr /usr/bin/java`
- `ls -lrt /etc/alternatives/java`

3. 配置JDK环境变量

- 通过yum方式安装默认安装在/usr/lib/jvm文件下
- 修改JAVA_HOME为/usr/lib/jvm/java-11-openjdk-11.0.12.0.7-0.el7_9.x86_64
- 编辑/etc/profile文件
- `vi /etc/profile`
- 按" i "键进行编辑，设置环境变量，ESC退出编辑，" :wq "保存内容
- #Java Environment
- `export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-11.0.12.0.7-0.el7_9.x86_64
  export JRE_HOME=$JAVA_HOME/jre
  export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/jre/lib/tools.jar:$JRE_HOME/lib:$CLASSPATH
  export PATH=$JAVA_HOME/bin:$PATH`

- 使环境变量生效 `source /etc/profile`

### Python配置

### Jenkins配置



