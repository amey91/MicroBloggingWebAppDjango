package edu.cmu.cs.webapps.framework;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public interface Action {
	public String get(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException;
	public String post(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException;
}
