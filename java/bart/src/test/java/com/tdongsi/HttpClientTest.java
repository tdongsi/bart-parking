package com.tdongsi;

import static org.junit.Assert.*;

import java.io.IOException;

import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.fluent.Request;
import org.junit.Test;

public class HttpClientTest {
	
	private static String API_ENDPOINT = "http://api.icndb.com/jokes/random";

	@Test
	public void test_fluentApi() throws ClientProtocolException, IOException {
		String see = Request.Get(API_ENDPOINT).execute().returnContent().asString();
		assertFalse(see.isEmpty());
		System.out.println(see);
	}

}
