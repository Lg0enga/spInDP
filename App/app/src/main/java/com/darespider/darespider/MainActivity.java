package com.darespider.darespider;

import android.app.FragmentManager;
import android.app.FragmentTransaction;
import android.content.Intent;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;

import com.darespider.darespider.LineGraphFragment;
import com.darespider.darespider.MainFragment;
import com.darespider.darespider.R;
import com.darespider.darespider.VideoFragment;
import com.github.mikephil.charting.data.Entry;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Timer;
import java.util.TimerTask;

import com.darespider.darespider.api.SpiderService;
import com.darespider.darespider.model.Spider;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.GsonConverterFactory;
import retrofit2.Response;
import retrofit2.Retrofit;

public class MainActivity extends AppCompatActivity implements MainFragment.OnMainFragmentListener, VideoFragment.OnVideoFragmentListener, LineGraphFragment.OnLineGraphFragmentListener  {
    private int mAttribute = -1; //
    private int mSelecedLeg =-1; //gets set when one of the imagebuttons of the spider gets clicked
    private boolean mInternet = true; // a boolean that's true when there's internet
    private Spider mSpider; // the spider model
    private ArrayList<Spider> spiderList = new ArrayList<>(); //a List of the model spider that adds a new one every second
    private int mIterator = -1; //the iterator used in the iteratorList
    private ArrayList<Integer> mIteratorList = new ArrayList<>(); //a list of iterations that starts with 0 and adds 1 every second

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        getFragmentManager().beginTransaction()
                .add(R.id.fragment_container, new MainFragment())
                .commit();

        Timer timer = new Timer();
        timer.schedule(new TimerTask() {
            @Override
            public void run() {
                getData();
                if (spiderList == null)
                    spiderList = new ArrayList<>(); //if the spiderList is empty create a new one
                if (mSpider != null) {
                    spiderList.add(mSpider);
                    mIterator++;
                    mIteratorList.add(mIterator);
                }
            }
        },0, 1000);


    }

    /**
     * Sends a request to a webserver and retrieves the data from that server
     * Creates an interface and stores the data in multiple models
     */
    private void getData() {
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://172.24.1.1:5000")
                //.baseUrl("http://10.42.0.76")
                .addConverterFactory(GsonConverterFactory.create())
                .build();


        SpiderService spiderService = retrofit.create(SpiderService.class);
        spiderService.getData().enqueue(new Callback<Spider>() {
            /**
             * If the request can be send to the webserver, creates a spider model
             * @param call the request for the spider model
             * @param response the response that returns a spider model
             */
            @Override
            public void onResponse(Call<Spider> call, Response<Spider> response) {
                if (response.body() != null) {
                    Spider spider = response.body();
                    MainActivity.this.mSpider = spider;

                }else{
                    mInternet = false;
                }
            }

            @Override
            public void onFailure(Call<Spider> call, Throwable t) {
                mInternet = false;
            }
        });

    }

    /**
     * Goes back one fragment when the back button gets pressed
     */
    @Override
    public void onBackPressed() {
        if(getFragmentManager().getBackStackEntryCount() != 0){
            getFragmentManager().popBackStack();
        }else{
            super.onBackPressed();
        }
    }

    @Override
    public void setAttribute(int attribute) {
        mAttribute = attribute;
    }

    public int getAttribute(){
        return mAttribute;
    }

    @Override
    public int getIterator() {
        return mIterator;
    }

    @Override
    public ArrayList<Spider> getSpiderList() {
        return spiderList;
    }

    @Override
    public void setSelectedLeg(int selectedLeg) {
        mSelecedLeg = selectedLeg;
    }

    public int getSelectedLeg(){
        return mSelecedLeg;
    }

    @Override
    public Spider getSpider() {
        return mSpider;
    }

    public ArrayList<Integer> getIteratorList(){
        return mIteratorList;
    }

    public boolean getInternet() {return mInternet;}

}