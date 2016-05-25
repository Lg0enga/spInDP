package com.darespider.darespider;

import android.os.Bundle;
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

import com.darespider.darespider.model.Spider;

import java.util.Timer;
import java.util.TimerTask;

/**
 * Created by Allard on 20-5-2016.
 */
public class TestActivity extends AppCompatActivity {


    private TextView mTest;


    class UpdateData extends TimerTask {
        public void run() {
            runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    updateData(MainActivity.mSPIDER);
                }
            });
        }
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.test);


        mTest = (TextView) findViewById(R.id.test);

        Timer timer = new Timer();
        timer.schedule(new UpdateData(), 0, 1000);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        MainActivity.selectedLeg = -1;
    }

    public final void updateData(Spider spider){
        switch (MainActivity.selectedLeg) {
            case 0:
                mTest.setText(Double.toString(spider.getLegs().get(0).getServos().get(0).getVoltage()));
                break;
        }
    }
}