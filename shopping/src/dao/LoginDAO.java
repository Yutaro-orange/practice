package dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import bean.User;

public class LoginDAO {

	public List<User> getLoginInformation(String a,String b){

		String sql = "SELECT * FROM USER1 WHERE ID =? AND PASSWORD = ?";
		List<User> userList =new ArrayList<User>();

		User user = new User();

		Connection con = null;
		PreparedStatement pSsmt = null;
		ResultSet rs = null;

		try {
			con = ConnectionManager.getConnection();
			//入力されたIDとパスワードを代入(サーブレットクラスでUSERインスタンスを生成)

			pSsmt = con.prepareStatement(sql);
			//入力されたIDとパスワードを取得
			pSsmt.setString(1,a);
			pSsmt.setString(2,b);
			rs = pSsmt.executeQuery();

			while(rs.next()) {



			String userId = rs.getString("ID");
			String userPassword = rs.getString("PASSWORD");

			user.setId(userId);
			user.setPassword(userPassword);

			userList.add(user);


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

		return userList;
	}
}
