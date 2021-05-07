

<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import ="java.util.ArrayList,java.util.List,bean.Product" %>
<%
List<Product> pList = (List<Product>) application.getAttribute("pList");
List<Product> inCartList = new ArrayList<Product>();
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>商品一覧</title>
</head>
<body>

<table id="products">
<tr>
<td>NAME</td>
<td>PRICE</td>
<td>STOCK</td>
</tr>

<% for(int i=0;i<pList.size();i++){ %>
<tr id ="cart">
<td id= "productName(<%=i%>)"><input type = "checkbox" name = "cart<%=i%>" value="cart" ><%= pList.get(i).getName() %></td>
<td><%= pList.get(i).getPrice() %></td>
<td><%= pList.get(i).getStock() %></td>
</tr>
<% } %>
<script>


function addCart(){

	var array = [];

	<% for (int i = 0 ; i < pList.size() ; i++) {%>

		var productName<%=i%> = document.getElementById("productName(<%=i%>)").textContent;
		if(cart<%=i%>.checked){
		array.push(productName<%=i%>);
		}

	<%}%>



	var tbl = document.getElementById("products");

	var target = document.getElementById("cartForm");

   target.value = array;

}
</script>


</table>
<button type = "submit"  name="kessai" onclick ="addCart()" >aaaa</button>


<form action ="/shopping/PaymentServlet" method ="POST">
<input type ="text" id = "cartForm" name ="inCartProducts" readonly="readonly">
<button type = "submit">決済</button>
</form>
<a href = "/shopping/ProductServlet">aaa</a>
</body>
</html>