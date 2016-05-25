package com.darespider.darespider;

import com.darespider.darespider.model.Spider;

import android.content.res.Resources;
import android.graphics.Color;
import android.graphics.Typeface;
import android.os.Bundle;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.view.ViewGroup;
import android.widget.RelativeLayout;
import com.github.mikephil.charting.charts.LineChart;
import com.github.mikephil.charting.components.Legend;
import com.github.mikephil.charting.components.XAxis;
import com.github.mikephil.charting.components.YAxis;
import com.github.mikephil.charting.data.Entry;
import com.github.mikephil.charting.data.LineData;
import com.github.mikephil.charting.data.LineDataSet;
import com.github.mikephil.charting.interfaces.datasets.ILineDataSet;
import com.github.mikephil.charting.utils.ColorTemplate;

import java.util.ArrayList;
import java.util.Timer;
import java.util.TimerTask;

/**
 * Created by Allard on 20-5-2016.
 */
public class LineGraph extends AppCompatActivity {

    private int iterator;
    ArrayList<Entry> coxa = new ArrayList<>();
    ArrayList<Entry> femur = new ArrayList<>();
    ArrayList<Entry> tibia = new ArrayList<>();
    ArrayList<ILineDataSet> dataSets = new ArrayList<>();
    ArrayList<String> xVals = new ArrayList<>();

    private LineChart mChart;
    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.line_graph);

        mChart = (LineChart) findViewById(R.id.chart1);
        addEntry();
        switch (MainActivity.attribute){
            case 0:
                mChart.setDescription("Stroom");
                break;
            case 1:
                mChart.setDescription("Kracht");
                break;
            case 2:
                mChart.setDescription("Stand");
                break;
            case 3:
                mChart.setDescription("Koppel");
                break;
            case 4:
                mChart.setDescription("Temperatuur");
                break;
            default:
                mChart.setDescription("");
        }
        mChart.setDescriptionColor(ContextCompat.getColor(getBaseContext(),R.color.dareDevil));
        mChart.setDescriptionTypeface(Typeface.SERIF);
        mChart.setDescriptionTextSize(16f);
        mChart.setNoDataTextDescription("Geen data om weer te geven");
        mChart.setBackgroundColor(Color.LTGRAY);

        mChart.setDrawGridBackground(false);
        mChart.setTouchEnabled(true);
        mChart.setDragEnabled(true);
        mChart.setScaleEnabled(true);
        mChart.setPinchZoom(true);

        Legend l = mChart.getLegend();
        l.setForm(Legend.LegendForm.LINE);
        l.setTextColor(Color.WHITE);

        XAxis xl = mChart.getXAxis();
        xl.setPosition(XAxis.XAxisPosition.BOTTOM);
        xl.setTextSize(10f);
        xl.setTextColor(ContextCompat.getColor(getBaseContext(),R.color.dareDevil));
        xl.setDrawAxisLine(true);
        xl.setDrawGridLines(false);
        xl.setAxisMaxValue(100f);

        //xl.setLabelsToSkip(5);

        //xl.setAvoidFirstLastClipping(true);

        YAxis yl = mChart.getAxisLeft();
        yl.setTextColor(ContextCompat.getColor(getBaseContext(),R.color.dareDevil));
        xl.setTextSize(10f);
        yl.setAxisMaxValue(20f);
        yl.setDrawGridLines(true);
        yl.setSpaceBottom(0f);
        yl.setDrawZeroLine(true);;

        YAxis yl2 = mChart.getAxisRight();
        yl2.setEnabled(false);



        LineDataSet coxaSet = new LineDataSet(coxa, "Coxa");
        coxaSet.setAxisDependency(YAxis.AxisDependency.LEFT);
        dataSets.add(coxaSet);

        LineData data = new LineData(xVals, dataSets);
        mChart.setData(data);

        mChart.invalidate();
    }

//    public void addEntry(){
//
//        Timer timer = new Timer();
//        timer.schedule(new TimerTask() {
//            @Override
//            public void run() {
//                Entry coxaEntry = new Entry((float) MainActivity.spiderArrayList.get(MainActivity.iterator).getLegs().get(MainActivity.selectedLeg).getServos().get(0).getVoltage(), MainActivity.iterator);
//                coxa.add(coxaEntry);
//            }
//        }, 5000);
//    }

    public void addEntry(){
        while (true){
            Entry coxaEntry = new Entry((float) MainActivity.spiderArrayList.get(MainActivity.iterator).getLegs().get(MainActivity.selectedLeg).getServos().get(0).getVoltage(), MainActivity.iterator);
            coxa.add(coxaEntry);
        }
    }

//    public void addEntry() {
//
//        LineData data = mChart.getData();
//
//        if(data != null){
//            ILineDataSet set = data.getDataSetByIndex(0);
//
//            if(set == null){
//                set = createSet();
//                data.addDataSet(set);
//            }
//        }
//    }


//    private void addEntry() {
//
//        LineData data = mChart.getData();
//
//        if (data != null) {
//
//            ILineDataSet set = data.getDataSetByIndex(0);
//            // set.addEntry(...); // can be called as well
//
//            if (set == null) {
//                set = createSet();
//                data.addDataSet(set);
//            }
//
//            // add a new x-value first
//            for(int i = 0; i <= 10; i++) {
//                data.addXValue("");
//                data.addEntry(new Entry(((float)MainActivity.spiderArrayList.get(i).getLegs().get(MainActivity.selectedLeg).getServos().get(0).getVoltage()), set.getEntryCount()),0);
//            }
//
//
//
//            // let the chart know it's data has changed
//            mChart.notifyDataSetChanged();
//
//            // limit the number of visible entries
//            mChart.setVisibleXRangeMaximum(120);
//            // mChart.setVisibleYRange(30, AxisDependency.LEFT);
//
//            // move to the latest entry
//            mChart.moveViewToX(data.getXValCount() - 11);
//
//            // this automatically refreshes the chart (calls invalidate())
//            // mChart.moveViewTo(data.getXValCount()-7, 55f,
//            // AxisDependency.LEFT);
//        }
//    }
//    private LineDataSet createSet() {
//
//        Timer timer = new Timer();
//        LineDataSet set = new LineDataSet(null, "coxa");
//
//    }

//    private void feedMultiple() {
//
//        new Thread(new Runnable() {
//
//            @Override
//            public void run() {
//                for(int i = 0; i < 500; i++) {
//
//                    runOnUiThread(new Runnable() {
//
//                        @Override
//                        public void run() {
//                            addEntry();
//                        }
//                    });
//
//                    try {
//                        Thread.sleep(35);
//                    } catch (InterruptedException e) {
//                        // TODO Auto-generated catch block
//                        e.printStackTrace();
//                    }
//                }
//            }
//        }).start();
//    }
    @Override
    protected void onDestroy() {
        super.onDestroy();
        MainActivity.selectedLeg = -1;
        MainActivity.attribute = - 1;
    }
}
