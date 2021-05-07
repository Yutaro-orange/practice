package dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import bean.Product;

public class ProductDAO {


	public List<Product> getProducts(){

		String sql = "SELECT * FROM PRODUCTS";
		List<Product> productList =new ArrayList<Product>();


		Connection con = null;
		PreparedStatement pSsmt = null;
		ResultSet rs = null;

		try {
			con = ConnectionManager.getConnection();

			pSsmt = con.prepareStatement(sql);
			rs = pSsmt.executeQuery();

			while(rs.next()) {
			Product product = new Product();

			String name = rs.getString("NAME");
			int price = rs.getInt("PRICE");
			int stock = rs.getInt("STOCK");

			product.setName(name);
			product.setPrice(price);
			product.setStock(stock);

			productList.add(product);

			}

		}catch(SQLException e) {
			e.printStackTrace();
		}finally {
			if(rs!=null) {
				try {
					rs.close();
				}catch(Exception ignore) {

				}
			}
			if(pSsmt!=null) {
				try {
					pSsmt.close();
				}catch(Exception ignore) {
					//例外をキャッチしても何もしないことを明示的に宣言
				}
			}
		}

		return productList;
	}
}
