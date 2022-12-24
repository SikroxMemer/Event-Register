# Event-Register
>Flask : Python Library Example
In This Example You Will Find An Example Of Flask Libary Uses In This Case An Event Register<br>
>>The Following Libaries Are The Ones In Use In My Example :<br>

* **Flask**
* **Flask SQLalchemy**
* **PyMySQL**

>Installing Flask :<br>
```
pip install flask
```
>Installing Flask SQLalchemy :<br>

```
pip install flask-sqlalchemy
```
>Installing flask PyMySQL :<br>

```
pip install pymysql
```
>To Set Up Mysql in your app you need to have a user , password , database in Mysql For Example :
>
>>*To Make A User In MYSQL:*
```
CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password';
```
>>*The ```authentication_plugin``` Can Differ Between Diffrent Users So Make Sure You Find The Supported One*
>>*Next Make A Database :*
```
CREATE DATABASE my_data_base;
```
>>Finally:
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://youruser:yourpassword@localhost/yourdatabase'
```
<https://flask.palletsprojects.com/en/2.2.x/>
