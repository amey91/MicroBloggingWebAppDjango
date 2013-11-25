package edu.cmu.cs.webapps.framework;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import edu.cmu.cs.webapps.framework.actions.*;

@WebServlet("/actions/*")
public class Controller extends HttpServlet {
	private static final long serialVersionUID = 1L;
	
	private enum RequestType {GET, POST};	
	private static final Map<String,Class<Action>> urlToActionMap = 
			new HashMap<String,Class<Action>>();
	
	static {
		registerAction("/wish", HappyBirthday.class);
	}
	
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Controller() {
        super();
    }

    protected void doAll(HttpServletRequest request, HttpServletResponse response, RequestType type) throws ServletException, IOException {
    		String path = request.getPathInfo();
		if (!(urlToActionMap.containsKey(path))) {
			response.sendError(HttpServletResponse.SC_NOT_FOUND, path);
			return;
		}
		Class<Action> actionClass = urlToActionMap.get(path);
		
		Action action = initializeAction(actionClass, request);
		
		String jsp = null;
		switch (type) {
			case GET:
				jsp = action.get(request, response);
				break;
			case POST:
				jsp = action.post(request, response);
				break;
		}
		ServletContext context = getServletContext();
		RequestDispatcher d = context.getRequestDispatcher("/" + jsp);
		d.forward(request, response);
    }
    
    
	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doAll(request, response, RequestType.GET);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doAll(request, response, RequestType.POST);
	}

	public Action initializeAction(Class<Action> actionClass, HttpServletRequest request) {
		// TODO:  1. Use reflection to create an instance of the right Action.
		//        2. Set all the data fields of that instance based on parameter values.
		//           a) Figure out data fields in the instance, and their type.
		//           b) Convert parameter value to the right type.
		//           c) Make field accessible if necessary.
		//        3. Set request attribute name/value pairs based on parameter values.
		//           i.e.,  also do request.setAttribute("foo", bar); for each field foo in the Action.
		//        4. Return the Action.
		return null;
	}

	public static void registerAction(String url, Class actionClass) {
		if (url == null || actionClass == null) {
			throw new NullPointerException("Registered URL or action was null");
		}
		if (urlToActionMap.containsKey(url)) {
			throw new IllegalArgumentException("URL already registered: " + url);
		}
		// Should also check to confirm that actionClass represents an Action,
		// but instead we'll allow a run-time ClassCast exception when processing
		// the requests..
		urlToActionMap.put(url, actionClass);
	}
}
