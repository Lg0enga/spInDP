package com.darespider.darespider;

import android.app.Activity;
import android.app.Fragment;
import android.content.Context;
import android.content.pm.ActivityInfo;
import android.os.Bundle;
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

    public interface OnLineGraphFragmentListener {
        int getAttribute();

        int getSelectedLeg();

        int getIterator();

        int getSeconds();

        ArrayList<Integer> getIteratorList();

        ArrayList<Integer> getSecondsList();

        ArrayList<Spider> getSpiderList();
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

    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.line_graph_fragment, container, false);

        mChart = (LineChart) view.findViewById(R.id.chart1);

        switch (mCallback.getAttribute()) {
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
        ;

        YAxis yl2 = mChart.getAxisRight();
        yl2.setEnabled(false);


        for(int i = 0; i < mCallback.getIterator(); i++){
            addEntry(i);
        }
        addSecondData();
        return view;
    }

    private void addEntry(int i){
        if(i > -1) {
            LineData data = mChart.getData();

            if (data != null) {
                ILineDataSet coxaSet = data.getDataSetByIndex(0);
                ILineDataSet femurSet = data.getDataSetByIndex(1);
                ILineDataSet tibiaSet = data.getDataSetByIndex(2);
                if (coxaSet == null) {
                    coxaSet = createSet("Coxa");
                    data.addDataSet(coxaSet);
                }
                if (femurSet == null) {
                    femurSet = createSet("Femur");
                    data.addDataSet(femurSet);
                }
                if (tibiaSet == null) {
                    tibiaSet = createSet("Tibia");
                    data.addDataSet(tibiaSet);
                }
                Entry entry1;
                Entry entry2;
                Entry entry3;
                data.addXValue(Integer.toString(mCallback.getSecondsList().get(i)));
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
                }
                mChart.notifyDataSetChanged();
                mChart.invalidate();
            }
        }
    }
    //    private void addFirstData(){
//        new Thread(new Runnable() {
//
//            @Override
//            public void run() {
//                for(number = 0; number < mCallback.getIteratorList().size(); number++) {
//
//                    if(getActivity() == null)
//                        return;
//                    getActivity().runOnUiThread(new Runnable() {
//
//                        @Override
//                        public void run() {
//                            addEntry(number);
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
                            addEntry(number);
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
    private LineDataSet createSet(String name) {
        LineDataSet set = new LineDataSet(null, name);
        set.setAxisDependency(YAxis.AxisDependency.LEFT);
        set.setColor(ColorTemplate.getHoloBlue());
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
