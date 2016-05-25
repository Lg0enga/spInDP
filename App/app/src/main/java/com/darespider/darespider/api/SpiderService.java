package com.darespider.darespider.api;

import com.darespider.darespider.model.Spider;

import retrofit2.Call;
import retrofit2.http.GET;

/**
 * Created by Allard on 19-5-2016.
 */
public interface SpiderService {

    @GET("/")
    Call<Spider> getData();

}
