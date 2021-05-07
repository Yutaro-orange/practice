package dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class ConnectionManager {


	private final static String DRIVER = "org.postgresql.Driver";
	private final static String JDBC_URL = "jdbc:postgresql://localhost:5432/postgres";
	private final static String USER_ID ="postgres";
	private final static String USER_PASS="aaaaa";

	public static Connection getConnection() throws SQLException {

		try {
			Class.forName(DRIVER);
		}catch(ClassNotFoundException e) {
			e.printStackTrace();
			throw new IllegalStateException("fail to class load : "
					+e.getMessage());
		}

		Connection con = DriverManager.getConnection(JDBC_URL,USER_ID,USER_PASS);

		return con;
	}

}
