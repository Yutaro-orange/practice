package servlet;

import java.io.IOException;
import java.util.Arrays;
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
 * Servlet implementation class PaymentServlet
 */
@WebServlet("/PaymentServlet")
public class PaymentServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

    /**
     * @see HttpServlet#HttpServlet()
     */
    public PaymentServlet() {
        super();
        // TODO Auto-generated constructor stub
    }
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

		ServletContext application = this.getServletContext();

		String inCartProduct = request.getParameter("inCartProducts");

		String[] productAry = inCartProduct.split(",");
		List<String> inCartList = Arrays.asList(productAry);

	//	ServletContext application = this.getServletContext();

		CartDAO cDao = new CartDAO();

		int sumPrice = cDao.getSumPrice(inCartList);

		application.setAttribute("inCartList", inCartList);
		application.setAttribute("sumPrice", sumPrice);



		RequestDispatcher dispatcher =
				request.getRequestDispatcher("/payment.jsp");
		dispatcher.forward(request,response);

		}
	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
		// TODO Auto-generated method stub



//		System.out.println(inCartProduct);


//		System.out.println(pList.get(0).getName());






}
