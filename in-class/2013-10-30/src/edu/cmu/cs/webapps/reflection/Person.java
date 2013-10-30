package edu.cmu.cs.webapps.reflection;

public class Person {
    public String name;  // This is public for demonstration purposes
                         // only.  It is very poor design for the name
                         // to be public
    private int age;
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String toString() {
        return name + ", age " + age;
    }
    
}
