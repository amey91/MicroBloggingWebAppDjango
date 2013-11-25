package edu.cmu.cs.webapps.framework.actions;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import edu.cmu.cs.webapps.framework.Action;

public class HappyBirthday implements Action {
	String name;
	int age;

	public String get(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		return "birthday.jsp";
	}

	public String post(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		System.err.println("name and age should be set properly when this method is called.");
		System.err.println("Wishing (" + name + "," + age + ") a happy birthday");
		return "birthday.jsp";
	}
}
