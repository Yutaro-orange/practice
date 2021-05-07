package dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import bean.Product;

public class CartDAO {


	public int getSumPrice(List<String> nameList){


		int sumPrice = 0;
		String sql = "SELECT PRICE FROM PRODUCTS WHERE NAME =? ";

		if(nameList.size() > 1) {
			for(int i=0;i<nameList.size() -1 ;i++) {
				sql=sql+ "OR NAME = ?";

			}
		}


		List<Product> cartList =new ArrayList<Product>();


		Connection con = null;
		PreparedStatement pSsmt = null;
		ResultSet rs = null;

		try {
			con = ConnectionManager.getConnection();

			pSsmt = con.prepareStatement(sql);

			for(int i = 0;i<nameList.size();i++) {
				pSsmt.setString(i+1,nameList.get(i));
			}

			rs = pSsmt.executeQuery();


			while(rs.next()) {
			Product product = new Product();

//			String name = rs.getString("NAME");
			int price = rs.getInt("PRICE");
//			int stock = rs.getInt("STOCK");

//			product.setName(name);
			product.setPrice(price);
//			product.setStock(stock);

			cartList.add(product);

			}

			for(int i=0; i<cartList.size();i++) {
				sumPrice+=cartList.get(i).getPrice();
			}


			System.out.println(sumPrice);

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

		return sumPrice;
	}



	public void changeCount(List<String> productNameList) {
		String sql ="UPDATE PRODUCTS SET STOCK = "
				+ "(SELECT STOCK FROM PRODUCTS WHERE NAME = ?) -1 "
				+ "WHERE NAME = ?";

//		String sql2 ="SELECT STOCK FROM PRODUCTS WHERE NAME = '?'";

		Connection con = null;
		PreparedStatement pSsmt = null;
//		System.out.println("aaa");



		try {
			con = ConnectionManager.getConnection();
			for(int i =0;i<productNameList.size();i++) {
				pSsmt = con.prepareStatement(sql);

				pSsmt.setString(1, productNameList.get(i));
				pSsmt.setString(2, productNameList.get(i));
				int r = pSsmt.executeUpdate();



//				pSsmt = con.prepareStatement(sql2);
//				pSsmt.setString(1, productNameList.get(i));

			}

		}catch(Exception ignore){

		}finally {
			if(pSsmt!=null) {
				try {
					pSsmt.close();
				}catch(Exception ignore) {
					//例外をキャッチしても何もしないことを明示的に宣言
				}
			}
		}
	}
}