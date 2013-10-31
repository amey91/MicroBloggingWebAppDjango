package edu.cmu.cs.webapps.reflection;
import java.lang.reflect.*;

public class Main {


	public static void main(String[] args) throws Exception {
		// TODO Use reflection to access fields in the Person class
		Person p = new Person("personA",25);
		System.out.println(p.getClass());
		System.out.println(p);
		Person b= new Person("personB",35);
		//p.getClass().getDeclaredField("name") = b.getClass().getDeclaredField("name");
		Field field = p.getClass().getDeclaredField("name");
		field.setAccessible(true);

		String getThisValue = (String)field.get(p);


		System.out.print(getThisValue);

		//f="helloPersonA";
		//f.setAccessible(true);


	}

}
