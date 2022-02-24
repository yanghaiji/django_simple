## 安装django

> pip install django
>

## 启动项目

### 命令启动

> python manage.py runserver 127.0 .0 .1: 9999

### pycharm 启动

### [pycharm 配置项目运行方式](pycharm_run.md)

## 常用命令

- 创建包

> django-admin startproject project_name
>

- 创建app

## 创建模块

> python manage.py startapp sales
>

## 修改数据库

> 修改 settings.py DATABASES配置
>
> 执行 python manage.py migrate

- 自定义表

> 项目内的 models.py 用于存储数据库表的定义
> 在settings.py 内 INSTALLED_APPS 添加 'common.apps.CommonConfig'
> 初始化数据库
> python manage.py makemigrations common
> python manage.py migrate
>

## Django Admin 管理数据

### [Django Admin 管理系统的使用](DjangoAdmin.md)