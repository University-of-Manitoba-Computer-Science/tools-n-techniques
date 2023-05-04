package com.example;

import org.json.JSONStringer;

/**
 * Hello world!
 *
 */
public class App {
    public static void main(String[] args) {
        JSONStringer stringer = new JSONStringer();
        System.out.println(stringer.object().key("Hello").value("world").endObject().toString());
    }
}
