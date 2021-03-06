# 第13周：自动化运维技术实训（下）

### 课程

通过本章的学习了解自动化运维基础知识和 Docker 容器。

实战部份包括：

- 自动化安装
- 监控报警
- 自动部署
- 批量运维等。



Docker 部份，将学习到 Docker 的镜像、容器、数据卷、dockerfile 等等实用功能。



---

### 作业

#### 问题描述

**作业一、 实现监控中心基础功能** 

1. 设计数据库表结构 

   ```
   主机表 字段 ：标签    ip    cpu    内存    硬盘 
   用户表 字段 ：用户名  密码 
   ```

2. 实现登录功能 
3. 登录成功后，可以添加主机 
4. 点击一条主机，可以查看到主机当前CPU、内存等资源占⽤用情况 
5. 点击编辑功能，可以修改主机信息，如 ip、签标等 
6. 项目界面参考见附件 

**作业二、 使用Docker搭建分布式爬虫**



#### 解题提示

1. 数据库设计和 Web 开发相关知识，参考 Web 开发模块 
2. 主机信息获取，可使用 psutil 模块 
3. CPU 使用率图表可使用百度图表



#### 批改标准

一、实现监控中心基础功能 

1. 数据库设计 5分 
2. 界面制作 5分 
3. Web开发 10分 
4. 自动登录远程主机 30分 
5. 获取远程主机 CPU、内存、硬盘等信息 30分 

二、使用 Docker 搭建分布式爬⾍ 

1. 实现功能 20分



