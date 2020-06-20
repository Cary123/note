# <center>eclipse项目结构</center>

##  简介
* .settings 文件里面存放各种插件的配置文件
* .project是项目文件，项目的结构都在其中定义，比如lib的位置,src的位置,classes的位置
* .classpath的位置定义了你这个项目在编译时所使用的$CLASSPATH

[参考](https://www.cnblogs.com/shihaiming/p/5803957.html)

## 1. 文件：.project
.project是项目文件
```xml
<?xml version="1.0" encoding="UTF-8"?>
<projectDescription>
    <!-- name里的内容代表项目名字，对应了Eclipse项目的名称，不是Maven的finalName -->
    <name>demo</name>
    <!-- 项目的注释 -->
    <comment></comment>
    <!-- 引用的项目的名字 -->
    <projects>
    </projects>
    <!-- 有序的列表，定义了一系列的构建命令（buildCommand） -->
    <buildSpec>
        <buildCommand>
            <!-- 项目构建命令的名字 -->
            <name>org.eclipse.wst.jsdt.core.javascriptValidator</name>
            <!-- 构建命令初始化时需要传递的参数（一般看到的都是空的） -->
            <arguments>
            </arguments>
        </buildCommand>
        <buildCommand>
            <name>org.eclipse.jdt.core.javabuilder</name>
            <arguments>
            </arguments>
        </buildCommand>
        <buildCommand>
            <name>org.eclipse.wst.common.project.facet.core.builder</name>
            <arguments>
            </arguments>
        </buildCommand>
        <buildCommand>
            <name>org.eclipse.m2e.core.maven2Builder</name>
            <arguments>
            </arguments>
        </buildCommand>
    </buildSpec>
    <!-- 项目中用到的一些特性的列表 -->
    <natures>
        <!-- 每一个特性的的名字 -->
        <nature>org.eclipse.jem.workbench.JavaEMFNature</nature>
        <nature>org.eclipse.wst.common.modulecore.ModuleCoreNature</nature>
        <nature>org.eclipse.jdt.core.javanature</nature>
        <nature>org.eclipse.m2e.core.maven2Nature</nature>
        <nature>org.eclipse.wst.common.project.facet.core.nature</nature>
        <nature>org.eclipse.wst.jsdt.core.jsNature</nature>
    </natures>
</projectDescription>
```

###  Normal Maven
一个Maven项目要确保有如下的内容，如果没有，可以手工加上下面的BuildCommand和natures：
```xml
<projectDescription>
    <buildSpec>
        <buildCommand>
            <name>org.eclipse.m2e.core.maven2Builder</name>
            <arguments>
            </arguments>
        </buildCommand>
    </buildSpec>
    <natures>
        <nature>org.eclipse.m2e.core.maven2Nature</nature>
    </natures>
</projectDescription>
```

### Dynamic Web
把一个Java项目变为dynamic web项目
加入如下的buildSpec、nature元素即可：
```xml
<buildSpec>
    <buildCommand>
        <name>org.eclipse.wst.common.project.facet.core.builder</name>
        <arguments>
        </arguments>
    </buildCommand>
</buildSpec>
<natures>
    <nature>org.eclipse.wst.common.modulecore.ModuleCoreNature</nature>
    <nature>org.eclipse.wst.common.project.facet.core.nature</nature>
</natures>
```


## 2. 文件：.classpath
.classpath描述了一个Eclipse项目。

### 典型内容
```xml
<?xml version="1.0" encoding="UTF-8"?>
<classpath>
    <!-- 含义：src/main/java属于源码，编译后放到target/classes目录下 -->
    <classpathentry kind="src" output="target/classes" path="src/main/java">
        <attributes>
            <attribute name="optional" value="true"/>
            <attribute name="maven.pomderived" value="true"/>
        </attributes>
    </classpathentry>
    <classpathentry excluding="**" kind="src" output="target/classes" path="src/main/resources">
        <attributes>
            <!-- 代表了配置是从POM.xml里来的，受maven管理，非maven项目可以去掉这个 -->
            <attribute name="maven.pomderived" value="true"/>
        </attributes>
    </classpathentry>
    <!-- 这里的including代表了目录下所有.java文件才会被处理，其他文件一概忽略，不会出现在target/test-classes目录下 -->
    <classpathentry including="**/*.java" kind="src" output="target/test-classes" path="src/test/java">
        <attributes>
            <attribute name="optional" value="true"/>
            <attribute name="maven.pomderived" value="true"/>
        </attributes>
    </classpathentry>
    <classpathentry excluding="**" kind="src" output="target/test-classes" path="src/test/resources">
        <attributes>
            <attribute name="maven.pomderived" value="true"/>
        </attributes>
    </classpathentry>
    <!-- 这里代表使用标准的JavaSE-1.7 JDK，相比来说如果用default和直接写当前系统中安装的JDK是不推荐的 -->
    <classpathentry kind="con" path="org.eclipse.jdt.launching.JRE_CONTAINER/org.eclipse.jdt.internal.debug.ui.launcher.StandardVMType/JavaSE-1.7">
        <attributes>
            <attribute name="maven.pomderived" value="true"/>
        </attributes>
    </classpathentry>
    <!-- 代表了Maven中的dependencies也都放到classpath里 -->
    <classpathentry kind="con" path="org.eclipse.m2e.MAVEN2_CLASSPATH_CONTAINER">
        <attributes>
            <attribute name="maven.pomderived" value="true"/>
            <!-- web工程中把依赖的jar都放到输出的webapp里/WEB-INF/lib下面 -->
            <attribute name="org.eclipse.jst.component.dependency" value="/WEB-INF/lib"/>
        </attributes>
    </classpathentry>
    <!--  -->
    <classpathentry kind="con" path="org.eclipse.jst.server.core.container/org.eclipse.jst.server.tomcat.runtimeTarget/Apache-Tomcat v7.0">
        <attributes>
            <attribute name="owner.project.facets" value="jst.web"/>
        </attributes>
    </classpathentry>
    <!-- 统一的输出为target/classes -->
    <classpathentry kind="output" path="target/classes"/>
</classpath>
```
### 使用示例
项目有test/resources或test/java目录，但是不识别为classpath

酌情加入如下的classpathentry：
<classpathentry including="**/*.java" kind="src" output="target/test-classes" path="src/test/java" />
<classpathentry excluding="**" kind="src" output="target/test-classes" path="src/test/resources" />
项目是maven工程，但是构建路径貌似怎么也配置不对

Maven是约定优于配置（convention over configuration）的，但是.classpath是配置型的，一般不会出现这种情况，如果出现了，检查maven约定的类路径（比如src/main/java、org.eclipse.m2e.MAVEN2_CLASSPATH_CONTAINER）中是否有如下的元素：
```xml
<attributes>
    <attribute name="maven.pomderived" value="true"/>
</attributes>
```
Maven的依赖jar文件放不到/WEB-INF/lib里

确认或加入如下的配置：
```xml
<classpathentry kind="con" path="org.eclipse.m2e.MAVEN2_CLASSPATH_CONTAINER">
    <attributes>
        <attribute name="maven.pomderived" value="true"/>
        <attribute name="org.eclipse.jst.component.dependency" value="/WEB-INF/lib"/>
    </attributes>
</classpathentry>
```
