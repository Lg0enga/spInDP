package com.darespider.darespider;

import android.app.Activity;
import android.app.Fragment;
import android.app.FragmentManager;
import android.app.FragmentTransaction;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.annotation.Nullable;
import android.support.design.widget.Snackbar;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageButton;
import android.widget.ProgressBar;
import android.widget.TextView;

import com.bumptech.glide.Glide;
import com.darespider.darespider.LineGraphFragment;
import com.darespider.darespider.R;
import com.darespider.darespider.VideoFragment;

import java.util.Timer;
import java.util.TimerTask;

import com.darespider.darespider.model.Spider;

/**
 * Created by Allard on 25-5-2016.
 */
public class MainFragment extends Fragment {
    private ProgressBar mBATTERIJ;

    private ImageButton mLFL;
    private ImageButton mLML;
    private ImageButton mLRL;
    private ImageButton mBODY;
    private ImageButton mLFR;
    private ImageButton mLMR;
    private ImageButton mLRR;
    private ImageButton mSTROOM;
    private ImageButton mKRACHT;
    private ImageButton mSTAND;
    private ImageButton mKOPPEL;
    private ImageButton mTEMPERATUUR;

    private TextView mBATTERIJPERCENTAGE;
    private TextView mHELLING;
    private TextView mPOOT;
    private TextView mCOXASTROOM;
    private TextView mCOXAKRACHT;
    private TextView mCOXASTAND;
    private TextView mCOXAKOPPEL;
    private TextView mCOXATEMPERATUUR;
    private TextView mFEMURSTROOM;
    private TextView mFEMURKRACHT;
    private TextView mFEMURSTAND;
    private TextView mFEMURKOPPEL;
    private TextView mFEMURTEMPERATUUR;
    private TextView mTIBIASTROOM;
    private TextView mTIBIAKRACHT;
    private TextView mTIBIASTAND;
    private TextView mTIBIAKOPPEL;
    private TextView mTIBIATEMPERATUUR;

    OnMainFragmentListener mCallback;

    public interface OnMainFragmentListener{
        void setAttribute(int attribute);
        void setSelectedLeg(int selectedLeg);
        int getSelectedLeg();
        Spider getSpider();
    }

    @Override
    public void onAttach(Activity activity) {
        super.onAttach(activity);

        try {
            mCallback = (OnMainFragmentListener) activity;
        } catch (ClassCastException e) {
            throw new ClassCastException(activity.toString()
                    + " must implement OnMainFragmentListener");
        }

    }

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.main_fragment, container, false);

        mBATTERIJ = (ProgressBar) view.findViewById(R.id.batterij);

        mLFL = (ImageButton) view.findViewById(R.id.lfl);
        mLML = (ImageButton) view.findViewById(R.id.lml);
        mLRL = (ImageButton) view.findViewById(R.id.lrl);
        mBODY = (ImageButton) view.findViewById(R.id.body);
        mLFR = (ImageButton) view.findViewById(R.id.lfr);
        mLMR = (ImageButton) view.findViewById(R.id.lmr);
        mLRR = (ImageButton) view.findViewById(R.id.lrr);
        mSTROOM = (ImageButton) view.findViewById(R.id.stroom);
        mKRACHT = (ImageButton) view.findViewById(R.id.kracht);
        mSTAND = (ImageButton) view.findViewById(R.id.stand);
        mKOPPEL = (ImageButton) view.findViewById(R.id.koppel);
        mTEMPERATUUR = (ImageButton) view.findViewById(R.id.temperatuur);

        mBATTERIJPERCENTAGE = (TextView) view.findViewById(R.id.batterijPercentage);
        mHELLING = (TextView) view.findViewById(R.id.hellingNummer);
        mPOOT = (TextView) view.findViewById(R.id.poot);
        mCOXASTROOM = (TextView) view.findViewById(R.id.coxaStroom);
        mCOXAKRACHT = (TextView) view.findViewById(R.id.coxaKracht);
        mCOXASTAND = (TextView) view.findViewById(R.id.coxaStand);
        mCOXAKOPPEL = (TextView) view.findViewById(R.id.coxaKoppel);
        mCOXATEMPERATUUR = (TextView) view.findViewById(R.id.coxaTemperatuur);
        mFEMURSTROOM = (TextView) view.findViewById(R.id.femurStroom);
        mFEMURKRACHT = (TextView) view.findViewById(R.id.femurKracht);
        mFEMURSTAND = (TextView) view.findViewById(R.id.femurStand);
        mFEMURKOPPEL = (TextView) view.findViewById(R.id.femurKoppel);
        mFEMURTEMPERATUUR = (TextView) view.findViewById(R.id.femurTemperatuur);
        mTIBIASTROOM = (TextView) view.findViewById(R.id.tibiaStroom);
        mTIBIAKRACHT = (TextView) view.findViewById(R.id.tibiaKracht);
        mTIBIASTAND = (TextView) view.findViewById(R.id.tibiaStand);
        mTIBIAKOPPEL = (TextView) view.findViewById(R.id.tibiaKoppel);
        mTIBIATEMPERATUUR = (TextView) view.findViewById(R.id.tibiaTemperatuur);

        Glide.with(this).load(R.drawable.lfl).into(mLFL);
        Glide.with(this).load(R.drawable.lml).into(mLML);
        Glide.with(this).load(R.drawable.lrl).into(mLRL);
        Glide.with(this).load(R.drawable.body).into(mBODY);
        Glide.with(this).load(R.drawable.lfr).into(mLFR);
        Glide.with(this).load(R.drawable.lmr).into(mLMR);
        Glide.with(this).load(R.drawable.lrr).into(mLRR);

        mLFL.setOnClickListener(new ButtonHandler());
        mLML.setOnClickListener(new ButtonHandler());
        mLRL.setOnClickListener(new ButtonHandler());
        mBODY.setOnClickListener(new ButtonHandler());
        mLFR.setOnClickListener(new ButtonHandler());
        mLMR.setOnClickListener(new ButtonHandler());
        mLRR.setOnClickListener(new ButtonHandler());
        mSTROOM.setOnClickListener(new ButtonHandler());
        mKRACHT.setOnClickListener(new ButtonHandler());
        mSTAND.setOnClickListener(new ButtonHandler());
        mKOPPEL.setOnClickListener(new ButtonHandler());
        mTEMPERATUUR.setOnClickListener(new ButtonHandler());

        setHasOptionsMenu(true);

        Timer timer = new Timer();
        timer.schedule(new TimerTask() {
            @Override
            public void run() {
                if(isVisible()) {

                    getActivity().runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            if (mCallback.getSpider() != null) {
                                updateText(mCallback.getSpider());
                                mBATTERIJ.setProgress(mCallback.getSpider().getBatteryPercentage());
                                mBATTERIJPERCENTAGE.setText(Integer.toString(mCallback.getSpider().getBatteryPercentage()) + "%");
                                mHELLING.setText(Double.toString(mCallback.getSpider().getSpiderAngle()) + (char) 0x00B0);
                            }
                        }
                    });
                }
            }
        }, 0, 1000);
        return view;
    }
    public class ButtonHandler implements View.OnClickListener {

        @Override
        public void onClick(View v) {
            LineGraphFragment lineGraphFragment = new LineGraphFragment();
            FragmentManager fragmentManager = getFragmentManager();
            FragmentTransaction fragmentTransaction = fragmentManager.beginTransaction();
            switch (v.getId()) {
                case R.id.stroom:
                    if(mCallback.getSelectedLeg() != -1){
                        fragmentTransaction.add(R.id.fragment_container, lineGraphFragment);
                        fragmentTransaction.addToBackStack(null);
                        fragmentTransaction.commit();
                        mCallback.setAttribute(0);
                    }else{
                        Snackbar stroomSnackbar = Snackbar.make(v, "kracht", Snackbar.LENGTH_SHORT);
                        stroomSnackbar.show();
                    }
                    break;
                case R.id.kracht:
                    if(mCallback.getSelectedLeg() != -1){
                        fragmentTransaction.add(R.id.fragment_container, lineGraphFragment);
                        fragmentTransaction.addToBackStack(null);
                        fragmentTransaction.commit();
                        mCallback.setAttribute(1);
                    }else{
                        Snackbar krachtSnackbar = Snackbar.make(v, "kracht", Snackbar.LENGTH_SHORT);
                        krachtSnackbar.show();
                    }
                    break;
                case R.id.stand:
                    if(mCallback.getSelectedLeg() != -1){
                        fragmentTransaction.add(R.id.fragment_container, lineGraphFragment);
                        fragmentTransaction.addToBackStack(null);
                        fragmentTransaction.commit();
                        mCallback.setAttribute(2);
                    }else {
                        Snackbar standSnackbar = Snackbar.make(v, "stand", Snackbar.LENGTH_SHORT);
                        standSnackbar.show();
                    }
                    break;
                case R.id.koppel:
                    if(mCallback.getSelectedLeg() != -1){
                        fragmentTransaction.add(R.id.fragment_container, lineGraphFragment);
                        fragmentTransaction.addToBackStack(null);
                        fragmentTransaction.commit();
                        mCallback.setAttribute(3);
                    }else {
                        Snackbar koppelSnackbar = Snackbar.make(v, "koppel", Snackbar.LENGTH_SHORT);
                        koppelSnackbar.show();
                    }
                    break;
                case R.id.temperatuur:
                    if(mCallback.getSelectedLeg() != -1){
                        fragmentTransaction.add(R.id.fragment_container, lineGraphFragment);
                        fragmentTransaction.addToBackStack(null);
                        fragmentTransaction.commit();
                        mCallback.setAttribute(4);
                    }else {
                        Snackbar temperatuurSnackbar = Snackbar.make(v, "temperatuur", Snackbar.LENGTH_SHORT);
                        temperatuurSnackbar.show();
                    }
                    break;
                case R.id.lfl:
                    mCallback.setSelectedLeg(0);
                    mPOOT.setText("Linker VoorPoot");
                    updateText(mCallback.getSpider());
                    break;
                case R.id.lml:
                    mCallback.setSelectedLeg(1);
                    mPOOT.setText("Linker Middenpoot");
                    updateText(mCallback.getSpider());
                    break;
                case R.id.lrl:
                    mCallback.setSelectedLeg(2);
                    mPOOT.setText("Linker Achterpoot");
                    updateText(mCallback.getSpider());
                    break;
                case R.id.lfr:
                    mCallback.setSelectedLeg(3);
                    mPOOT.setText("Rechter Voorpoot");
                    updateText(mCallback.getSpider());
                    break;
                case R.id.lmr:
                    mCallback.setSelectedLeg(4);
                    mPOOT.setText("Rechter Middenpoot");
                    updateText(mCallback.getSpider());
                    break;
                case R.id.lrr:
                    mCallback.setSelectedLeg(5);
                    mPOOT.setText("Rechter Achterpoot");
                    updateText(mCallback.getSpider());
                    break;
            }
        }
    }

    private void updateText(Spider spider) {
        if(spider != null) {
            if (mCallback.getSelectedLeg() != -1) {
                mCOXASTROOM.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(0).getVoltage()));
                mCOXAKRACHT.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(0).getForce()));
                mCOXASTAND.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(0).getPosition()));
                mCOXAKOPPEL.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(0).getTorque()));
                mCOXATEMPERATUUR.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(0).getTemperature()));
                mFEMURSTROOM.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(1).getVoltage()));
                mFEMURKRACHT.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(1).getForce()));
                mFEMURSTAND.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(1).getPosition()));
                mFEMURKOPPEL.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(1).getTorque()));
                mFEMURTEMPERATUUR.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(1).getTemperature()));
                mTIBIASTROOM.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(2).getVoltage()));
                mTIBIAKRACHT.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(2).getForce()));
                mTIBIASTAND.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(2).getPosition()));
                mTIBIAKOPPEL.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(2).getTorque()));
                mTIBIATEMPERATUUR.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(2).getTemperature()));
            }
        }
    }

    @Override
    public void onCreateOptionsMenu(Menu menu, MenuInflater inflater){
        inflater.inflate(R.menu.main_fragment_menu, menu);
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item){
        switch (item.getItemId()){
            case R.id.video:
                VideoFragment videoFragment = new VideoFragment();
                FragmentManager fragmentManager = getFragmentManager();
                FragmentTransaction fragmentTransaction = fragmentManager.beginTransaction();
                fragmentTransaction.add(R.id.fragment_container, videoFragment);
                fragmentTransaction.addToBackStack(null);
                fragmentTransaction.commit();
                return true;
            default:
                return super.onOptionsItemSelected(item);
        }
    }
//    @Override
//    public boolean onCreateOptionsMenu(Menu menu) {
//        MenuInflater inflater = getActivity().getMenuInflater();
//        inflater.inflate(R.menu.main_fragment_menu, menu);
//        return true;
//    }
//
//    @Override
//    public boolean onOptionsItemSelected(MenuItem item) {
//        switch (item.getItemId()) {
//            case R.id.video:
//
//                return true;
//            default:
//                return super.onOptionsItemSelected(item);
//        }
//    }

}