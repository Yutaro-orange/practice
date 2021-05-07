<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import ="java.util.List,bean.Product" %>
<% List<String> inCartList = (List<String>) application.getAttribute("inCartList");%>
<% int sumPrice = (int)application.getAttribute("sumPrice");%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>決済</title>
</head>
<body>
<p>以下の商品を購入します。</p>
<form action = "/shopping/KessaiServlet" method ="POST">
	<% for(int i =0;i<inCartList.size();i++){ %>
	<input type = "text" readonly="readonly" name="cart<%=i %>" value =<%= inCartList.get(i) %>>
	<% } %>
	<p>小計：<%= sumPrice %></p>
	<button type ="submit">購入確定</button>
</form>
</body>
</html>