package com.darespider.darespider;

import android.app.Activity;
import android.app.Fragment;
import android.content.Context;
import android.content.pm.ActivityInfo;
import android.os.Bundle;
import android.support.v7.app.AlertDialog;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.content.res.Resources;
import android.graphics.Color;
import android.graphics.Typeface;
import android.os.Bundle;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.view.ViewGroup;
import android.widget.RelativeLayout;

import com.bumptech.glide.load.engine.Resource;
import com.darespider.darespider.R;
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

import com.darespider.darespider.model.Spider;

/**
 * Created by Allard on 26-5-2016.
 */
public class LineGraphFragment extends Fragment{

    OnLineGraphFragmentListener mCallback;
    boolean alert = true;


//    int entryNumber = 0;
//    ArrayList<Entry> mCoxa = new ArrayList<>();
//    ArrayList<Entry> mFemur = new ArrayList<>();
//    ArrayList<Entry> mTibia = new ArrayList<>();
//    LineData coxaData = new LineData();
//    LineData femurData = new LineData();
//    LineData tibiaData = new LineData();
//    ArrayList<String> xVals = new ArrayList<>();
    //LineDataSet coxaSet = new LineDataSet(mCoxa, "Coxa");
    // LineDataSet femurSet = new LineDataSet(mFemur, "Femur");
    //LineDataSet tibiaSet = new LineDataSet(mTibia, "Tibia");


    private LineChart mChart;
    public int number;

    /*
    The functions from the mainActivity that the fragment uses
     */
    public interface OnLineGraphFragmentListener {
        int getAttribute();
        int getSelectedLeg();
        int getIterator();
        ArrayList<Integer> getIteratorList();
        ArrayList<Spider> getSpiderList();
        boolean getInternet();
    }

    public void onAttach(Activity activity) {
        super.onAttach(activity);

        try {
            mCallback = (OnLineGraphFragmentListener) activity;
        } catch (ClassCastException e) {
            throw new ClassCastException(activity.toString()
                    + " must implement OnLineGraphFragmentListener");
        }

    }

    /*
     Creates the view for the LineChart
     */
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.line_graph_fragment, container, false);

        mChart = (LineChart) view.findViewById(R.id.chart1);

        switch (mCallback.getAttribute()) {
            case 0:
                mChart.setDescription("Voltage");
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
        mChart.setDescriptionColor(R.color.dareDevil);
        mChart.setDescriptionTypeface(Typeface.SERIF);
        mChart.setDescriptionTextSize(16f);
        mChart.setNoDataTextDescription("Geen data om weer te geven");
        mChart.setBackgroundColor(Color.LTGRAY);

        mChart.setDrawGridBackground(false);
        mChart.setTouchEnabled(true);
        mChart.setDragEnabled(true);
        mChart.setScaleEnabled(true);
        mChart.setPinchZoom(true);

        LineData data = new LineData();
        data.setValueTextColor(Color.WHITE);

        mChart.setData(data);

        Legend l = mChart.getLegend();
        l.setForm(Legend.LegendForm.LINE);
        l.setTextColor(Color.WHITE);

        XAxis xl = mChart.getXAxis();
        xl.setPosition(XAxis.XAxisPosition.BOTTOM);
        xl.setTextSize(10f);
        xl.setTextColor(R.color.dareDevil);
        xl.setDrawAxisLine(true);
        xl.setDrawGridLines(false);

        //xl.setLabelsToSkip(5);

        //xl.setAvoidFirstLastClipping(true);

        YAxis yl = mChart.getAxisLeft();
        yl.setTextColor(R.color.dareDevil);
        xl.setTextSize(10f);
        yl.setDrawGridLines(true);
        yl.setSpaceBottom(0f);
        yl.setDrawZeroLine(true);
        yl.setGranularity(5);

        YAxis yl2 = mChart.getAxisRight();
        yl2.setEnabled(false);


        for(int i = 0; i < mCallback.getIterator(); i++){
            addEntry(i);
        }
        addSecondData();


        return view;
    }

    /**
     * Adds an entry to the LineData.
     * The iterator determines how many times the chart will update.
     * @param i the iterator
     */
    private void addEntry(int i){
 //       try{
            if(i > -1) {
                LineData data = mChart.getData();
                if (data != null) {
                    ILineDataSet coxaOrVoltageOrBatterySet = data.getDataSetByIndex(0);
                    ILineDataSet femurOrForceOrSlopeXSet = data.getDataSetByIndex(1);
                    ILineDataSet tibiaOrPositionOrSlopeYSet = data.getDataSetByIndex(2);
                    ILineDataSet torqueSet = data.getDataSetByIndex(3);
                    ILineDataSet temperatureSet = data.getDataSetByIndex(4);
                    if (coxaOrVoltageOrBatterySet == null) {
                        if(mCallback.getAttribute() > 4 && mCallback.getAttribute() != 8){
                            coxaOrVoltageOrBatterySet = createSet("Voltage", ColorTemplate.JOYFUL_COLORS[0]);
                        }
                        else if(mCallback.getAttribute() == 8){
                            coxaOrVoltageOrBatterySet = createSet("Batterij", ColorTemplate.JOYFUL_COLORS[0]);
                        }
                        else{
                            coxaOrVoltageOrBatterySet = createSet("Coxa", ColorTemplate.JOYFUL_COLORS[0]);
                        }
                        data.addDataSet(coxaOrVoltageOrBatterySet);
                    }
                    if (femurOrForceOrSlopeXSet == null) {
                        if(mCallback.getAttribute() > 4 && mCallback.getAttribute() != 8){
                            femurOrForceOrSlopeXSet = createSet("Kracht", ColorTemplate.JOYFUL_COLORS[1]);
                        }
                        else if(mCallback.getAttribute() == 8){
                            femurOrForceOrSlopeXSet = createSet("Helling X", ColorTemplate.JOYFUL_COLORS[1]);
                        }
                        else{
                            femurOrForceOrSlopeXSet = createSet("Femur", ColorTemplate.JOYFUL_COLORS[1]);
                        }
                        data.addDataSet(femurOrForceOrSlopeXSet);
                    }
                    if (tibiaOrPositionOrSlopeYSet == null) {
                        if(mCallback.getAttribute() > 4 && mCallback.getAttribute() != 8){
                            tibiaOrPositionOrSlopeYSet = createSet("Stand", ColorTemplate.JOYFUL_COLORS[2]);
                        }
                        else if(mCallback.getAttribute() == 8){
                            tibiaOrPositionOrSlopeYSet = createSet("Helling Y", ColorTemplate.JOYFUL_COLORS[2]);
                        }
                        else{
                            tibiaOrPositionOrSlopeYSet = createSet("Tibia", ColorTemplate.JOYFUL_COLORS[2]);
                        }
                        data.addDataSet(tibiaOrPositionOrSlopeYSet);
                    }
                    if(torqueSet == null){
                        torqueSet = createSet("Koppel", ColorTemplate.JOYFUL_COLORS[3]);
                        data.addDataSet(torqueSet);
                    }
                    if(temperatureSet == null){
                        temperatureSet = createSet("Temperatuur", ColorTemplate.JOYFUL_COLORS[4]);
                        data.addDataSet(temperatureSet);
                    }
                    Entry entry1;
                    Entry entry2;
                    Entry entry3;
                    Entry entry4;
                    Entry entry5;
                    data.addXValue(Integer.toString(mCallback.getIteratorList().get(i)));

                    switch (mCallback.getAttribute()){
                        case 0:
                            entry1 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(0).getVoltage(), i);
                            entry2 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(1).getVoltage(), i);
                            entry3 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(2).getVoltage(), i);
                            data.addEntry(entry1, 0);
                            data.addEntry(entry2, 1);
                            data.addEntry(entry3, 2);
                            break;
                        case 1:
                            entry1 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(0).getForce(), i);
                            entry2 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(1).getForce(), i);
                            entry3 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(2).getForce(), i);
                            data.addEntry(entry1, 0);
                            data.addEntry(entry2, 1);
                            data.addEntry(entry3, 2);
                            break;
                        case 2:
                            entry1 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(0).getPosition(), i);
                            entry2 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(1).getPosition(), i);
                            entry3 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(2).getPosition(), i);
                            data.addEntry(entry1, 0);
                            data.addEntry(entry2, 1);
                            data.addEntry(entry3, 2);
                            break;
                        case 3:
                            entry1 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(0).getTorque(), i);
                            entry2 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(1).getTorque(), i);
                            entry3 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(2).getTorque(), i);
                            data.addEntry(entry1, 0);
                            data.addEntry(entry2, 1);
                            data.addEntry(entry3, 2);
                            break;
                        case 4:
                            entry1 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(0).getTemperature(), i);
                            entry2 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(1).getTemperature(), i);
                            entry3 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(2).getTemperature(), i);
                            data.addEntry(entry1, 0);
                            data.addEntry(entry2, 1);
                            data.addEntry(entry3, 2);
                            break;
                        case 5:
                            entry1 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(0).getVoltage(), i);
                            entry2 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(0).getForce(), i);
                            entry3 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(0).getPosition(), i);
                            entry4 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(0).getTorque(), i);
                            entry5 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(0).getTemperature(), i);
                            data.addEntry(entry1, 0);
                            data.addEntry(entry2, 1);
                            data.addEntry(entry3, 2);
                            data.addEntry(entry4, 3);
                            data.addEntry(entry5, 4);
                            break;
                        case 6:
                            entry1 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(1).getVoltage(), i);
                            entry2 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(1).getForce(), i);
                            entry3 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(1).getPosition(), i);
                            entry4 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(1).getTorque(), i);
                            entry5 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(1).getTemperature(), i);
                            data.addEntry(entry1, 0);
                            data.addEntry(entry2, 1);
                            data.addEntry(entry3, 2);
                            data.addEntry(entry4, 3);
                            data.addEntry(entry5, 4);
                            break;
                        case 7:
                            entry1 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(2).getVoltage(), i);
                            entry2 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(2).getForce(), i);
                            entry3 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(2).getPosition(), i);
                            entry4 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(2).getTorque(), i);
                            entry5 = new Entry((float) mCallback.getSpiderList().get(i).getLegs().get(mCallback.getSelectedLeg()).getServos().get(2).getTemperature(), i);
                            data.addEntry(entry1, 0);
                            data.addEntry(entry2, 1);
                            data.addEntry(entry3, 2);
                            data.addEntry(entry4, 3);
                            data.addEntry(entry5, 4);
                            break;
                        case 8:
                            entry1 = new Entry((float) mCallback.getSpiderList().get(i).getBatteryPercentage(), i);
                            entry2 = new Entry((float) mCallback.getSpiderList().get(i).getSpiderAngleX(), i);
                            entry3 = new Entry((float) mCallback.getSpiderList().get(i).getSpiderAngleY(), i);
                            data.addEntry(entry1, 0);
                            data.addEntry(entry2, 1);
                            data.addEntry(entry3, 2);
                            break;
                    }
                    mChart.notifyDataSetChanged();
                    mChart.setVisibleXRangeMaximum(10);
                    mChart.moveViewToX(data.getXValCount() - 11);
                    mChart.invalidate();
                }
            }
        //}catch(IndexOutOfBoundsException e){
//            while(alert){
//                AlertDialog.Builder builder = new AlertDialog.Builder(getActivity());
//                builder.setTitle(R.string.noInternet);
//                builder.setMessage(R.string.noInternet);
//                builder.setNegativeButton(R.string.okay, null);
//                AlertDialog alertDialog = builder.create();
//                alertDialog.show();
//                alert = false;
//            }
//            mChart.setData(null);
        //}

    }

    /**
     * Adds an entry to the LineDataSet every second
     */
    private void addSecondData(){
        new Thread(new Runnable() {

            @Override
            public void run() {
                for(number = mCallback.getIteratorList().size() - 1; number <10000; number++) {

                    if(getActivity() == null)
                        return;
                    getActivity().runOnUiThread(new Runnable() {

                        @Override
                        public void run() {
                            if(mCallback.getInternet()){
                                addEntry(number);
                            }
                            else{
                                int test = 9;
                            }

                        }
                    });

                    try {
                        Thread.sleep(1000);
                    } catch (InterruptedException e) {
                        // TODO Auto-generated catch block
                        e.printStackTrace();
                    }
                }
            }
        }).start();
    }

    /**
     * Returns a LineDataSet which the LineChart can use
     * @param name the name of the data set
     * @param color the color the data set is given
     * @return the LineDataSet
     */

    private LineDataSet createSet(String name, int color) {
        LineDataSet set = new LineDataSet(null, name);
        set.setAxisDependency(YAxis.AxisDependency.LEFT);
        set.setColor(color);
        set.setCircleColor(Color.WHITE);
        set.setLineWidth(2f);
        set.setCircleRadius(4f);
        set.setFillAlpha(65);
        set.setFillColor(ColorTemplate.getHoloBlue());
        set.setHighLightColor(Color.rgb(244, 117, 117));
        set.setValueTextColor(Color.WHITE);
        set.setValueTextSize(9f);
        set.setDrawValues(false);
        return set;
    }
}
