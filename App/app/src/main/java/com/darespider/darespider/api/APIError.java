package com.darespider.darespider.api;

/**
 * Created by Allard on 1-6-2016.
 */
public class APIError {
    private int statusCode;
    private String message;

    public APIError() {
    }

    public int status() {
        return statusCode;
    }

    public String message() {
        return message;
    }
}

