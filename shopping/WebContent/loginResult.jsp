<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import = "bean.User,java.util.List"
%>
<% List<User> userList = (List<User>)session.getAttribute("userList"); %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>ログイン結果</title>
</head>
<body>
<% if(userList.size()!=0) { %>
	<p>ログインに成功しました。</p>
	<a href ="/shopping/ProductServlet">商品検索画面へ</a>
<% }else{ %>
	<p>ログインに失敗しました。</p>
	<a href = "/shopping/Main">トップへ</a>
<% } %>
</body>
</html>