package servlet;

import java.io.IOException;
import java.util.List;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import dao.CartDAO;

/**
 * Servlet implementation class KessaiServlet
 */
@WebServlet("/KessaiServlet")
public class KessaiServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

    /**
     * @see HttpServlet#HttpServlet()
     */
    public KessaiServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub

		ServletContext application = this.getServletContext();


		CartDAO cDao = new CartDAO();

		//実装の仕方要検討
		@SuppressWarnings("unchecked")
		List <String> parchasedProducts = (List <String>)application.getAttribute("inCartList");


		cDao.changeCount(parchasedProducts);

		RequestDispatcher dispatcher =
				request.getRequestDispatcher("/kessai.jsp");
		dispatcher.forward(request,response);

	}

}
