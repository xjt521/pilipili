2019-7-26 xjt at shenzhen
piliweb解压后有两个文件
一个pilipili为工程文件，一个pilienv为所使用的虚拟环境
admin后台数据库管理，登录127.0.0.1/8000/admin
账号admin 密码0000


"""2019-7-29更新 xjt at shenzhen"""
1实现登录功能，登录时需要输入实时的图形化验证码。
2实现注册功能，注册时自动发送邮件至注册邮箱，并且需要在点击邮箱中确认链接后才可登录。
3为了实现邮箱注册功能，在OdinaryUser表中增加了code属性，代表每个用户独有的哈希吗，用来实现邮箱确认，注意python manage.py  makemigrations和python manage.py  migrate更新数据库
4前端非常丑陋，但核心功能基本已经实现，用模板补上即可，补模板时不要修改变量，防止运行出错。
5管理员登录admin 0000，在注册时由于没有部署至服务器，所以必须先运行本地服务器。
6为了方便debug没有使用二级路由，可以修改根目录下的urls和各个APP的urls，达成松耦合。
7不再上传环境，但有了reqiurements文件，直接使用它pip install所需环境即可。

PS：setting配置中的数据库名称和密码注意改成自己的