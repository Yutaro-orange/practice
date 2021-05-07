<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>ログイン</title>
</head>
<body>
<h1>ログイン画面</h1>
<form action = "/shopping/LoginServlet" method ="POST">
ID:<input type = "text" name = "ID"/>
パスワード:<input type = "password" name = "PASSWORD"/>
<button type = "submit">ログイン</button>
</form>
</body>
</html>