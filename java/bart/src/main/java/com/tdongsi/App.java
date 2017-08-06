package com.tdongsi;

import java.io.IOException;

import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
        
        String API_ENDPOINT = "http://api.icndb.com/jokes/random";
        CloseableHttpClient httpclient = HttpClients.createDefault();
        HttpGet httpget = new HttpGet(API_ENDPOINT);
        try {
			CloseableHttpResponse response = httpclient.execute(httpget);
		} catch (IOException e) {
			System.err.println("Cannot request " + API_ENDPOINT);
		}
        
    }
}
