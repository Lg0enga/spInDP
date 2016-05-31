package com.darespider.darespider;

import android.app.FragmentManager;
import android.app.FragmentTransaction;
import android.content.Intent;
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
    private int mAttribute = -1;
    private int mSelecedLeg =-1;
    private Spider mSpider;
    private ArrayList<Spider> spiderList = new ArrayList<>();
    private int mIterator = -1;
    private int mSeconds = -1;
    private ArrayList<Integer> mIteratorList = new ArrayList<>();
    private ArrayList<Integer> mSecondsList = new ArrayList<>();

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
                    spiderList = new ArrayList<>();
                if (mSpider != null) {
                    spiderList.add(mSpider);
                    mIterator++;
                    mSeconds++;
                    mIteratorList.add(mIterator);
                    mSecondsList.add(mSeconds);
                }
            }
        },0, 1000);
    }
    private void getData() {
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://10.42.0.76")
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        SpiderService spiderService = retrofit.create(SpiderService.class);
        spiderService.getData().enqueue(new Callback<Spider>() {
            @Override
            public void onResponse(Call<Spider> call, Response<Spider> response) {
                Spider spider = response.body();

                MainActivity.this.mSpider = spider;
            }

            @Override
            public void onFailure(Call<Spider> call, Throwable t) {

            }
        });

    }

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

    //public void setIterator(int iterator) {mIterator = iterator;}

    @Override
    public int getIterator() {
        return mIterator;
    }

    @Override
    public int getSeconds() {
        return mSeconds;
    }

    //public void setSeconds(int seconds) {mSeconds = seconds;}

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

    public ArrayList<Integer> getSecondsList(){
        return mSecondsList;
    }

}