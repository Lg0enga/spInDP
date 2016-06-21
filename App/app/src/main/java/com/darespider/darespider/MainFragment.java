package com.darespider.darespider;

import android.app.Activity;
import android.app.Fragment;
import android.app.FragmentManager;
import android.app.FragmentTransaction;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.support.annotation.Nullable;
import android.support.design.widget.Snackbar;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.ProgressBar;
import android.widget.TextView;

import com.bumptech.glide.Glide;
import com.darespider.darespider.LineGraphFragment;
import com.darespider.darespider.R;
import com.darespider.darespider.VideoFragment;

import java.util.ArrayList;
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

    private Button mCoxa;
    private Button mFemur;
    private Button mTibia;

    private TextView mBATTERIJPERCENTAGE;
    private TextView mHELLINGX;
    private TextView mHELLINGY;
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
    boolean alert = true;
    OnMainFragmentListener mCallback;

    /*
    The functions from MainAcitivity that the fragment uses
     */
    public interface OnMainFragmentListener{
        void setAttribute(int attribute);
        void setSelectedLeg(int selectedLeg);
        int getSelectedLeg();
        Spider getSpider();
        boolean getInternet();
        ArrayList<Spider> getSpiderList();
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

    /*
    Creates the view for the main fragment
     */
    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, final ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.main_fragment, container, false);

        mBATTERIJ = (ProgressBar) view.findViewById(R.id.battery);

        mLFL = (ImageButton) view.findViewById(R.id.lfl);
        mLML = (ImageButton) view.findViewById(R.id.lml);
        mLRL = (ImageButton) view.findViewById(R.id.lrl);
        mBODY = (ImageButton) view.findViewById(R.id.body);
        mLFR = (ImageButton) view.findViewById(R.id.lfr);
        mLMR = (ImageButton) view.findViewById(R.id.lmr);
        mLRR = (ImageButton) view.findViewById(R.id.lrr);
        mSTROOM = (ImageButton) view.findViewById(R.id.voltage);
        mKRACHT = (ImageButton) view.findViewById(R.id.power);
        mSTAND = (ImageButton) view.findViewById(R.id.position);
        mKOPPEL = (ImageButton) view.findViewById(R.id.torque);
        mTEMPERATUUR = (ImageButton) view.findViewById(R.id.temperature);

        mCoxa = (Button) view.findViewById(R.id.coxa);
        mFemur = (Button) view.findViewById(R.id.femur);
        mTibia = (Button) view.findViewById(R.id.tibia);

        mBATTERIJPERCENTAGE = (TextView) view.findViewById(R.id.batteryPercentage);
        mHELLINGX = (TextView) view.findViewById(R.id.angleX);
        mHELLINGY = (TextView) view.findViewById(R.id.angleY);
        mPOOT = (TextView) view.findViewById(R.id.leg);
        mCOXASTROOM = (TextView) view.findViewById(R.id.coxaVoltage);
        mCOXAKRACHT = (TextView) view.findViewById(R.id.coxaPower);
        mCOXASTAND = (TextView) view.findViewById(R.id.coxaPosition);
        mCOXAKOPPEL = (TextView) view.findViewById(R.id.coxaTorque);
        mCOXATEMPERATUUR = (TextView) view.findViewById(R.id.coxaTemperature);
        mFEMURSTROOM = (TextView) view.findViewById(R.id.femurVoltage);
        mFEMURKRACHT = (TextView) view.findViewById(R.id.femurPower);
        mFEMURSTAND = (TextView) view.findViewById(R.id.femurPosition);
        mFEMURKOPPEL = (TextView) view.findViewById(R.id.femurTorque);
        mFEMURTEMPERATUUR = (TextView) view.findViewById(R.id.femurTemperature);
        mTIBIASTROOM = (TextView) view.findViewById(R.id.tibiaVoltage);
        mTIBIAKRACHT = (TextView) view.findViewById(R.id.tibiaPower);
        mTIBIASTAND = (TextView) view.findViewById(R.id.tibiaPosition);
        mTIBIAKOPPEL = (TextView) view.findViewById(R.id.tibiaTorque);
        mTIBIATEMPERATUUR = (TextView) view.findViewById(R.id.tibiaTemperature);

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
        mCoxa.setOnClickListener(new ButtonHandler());
        mFemur.setOnClickListener(new ButtonHandler());
        mTibia.setOnClickListener(new ButtonHandler());

        setHasOptionsMenu(true);

        Timer timer = new Timer();
        timer.schedule(new TimerTask() {
            @Override
            public void run() {
                if(isVisible()) {

                    getActivity().runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            if(!mCallback.getInternet()){ // if there's no internet creates an AlertDialog
                                while(alert){
                                    AlertDialog.Builder builder = new AlertDialog.Builder(getActivity());
                                    builder.setTitle(R.string.noConnection);
                                    builder.setMessage(R.string.restart);
                                    builder.setNegativeButton(R.string.okay, null);
                                    AlertDialog alertDialog = builder.create();
                                    alertDialog.show();
                                    alert = false;
                                }
                            }

                            if (mCallback.getSpider() != null) {
                                updateText(mCallback.getSpider());
                                mBATTERIJ.setProgress(mCallback.getSpider().getBatteryPercentage());
                                mBATTERIJPERCENTAGE.setText(Integer.toString(mCallback.getSpider().getBatteryPercentage()) + "%");
                                mHELLINGX.setText("X:" + Double.toString(mCallback.getSpider().getSpiderAngleX()) + (char) 0x00B0);
                                mHELLINGY.setText("Y:" + Double.toString(mCallback.getSpider().getSpiderAngleY()) + (char) 0x00B0);
                            }
                        }
                    });
                }
            }
        }, 0, 1000);
        return view;
    }
    public class ButtonHandler implements View.OnClickListener {

        /**
         * The onClickHandler
         * @param v the view
         */
        @Override
        public void onClick(View v) {
            LineGraphFragment lineGraphFragment = new LineGraphFragment();
            FragmentManager fragmentManager = getFragmentManager();
            FragmentTransaction fragmentTransaction = fragmentManager.beginTransaction();
            switch (v.getId()) {
                case R.id.voltage:
                    if(mCallback.getSelectedLeg() == -1 || mCallback.getSpiderList().size() == 0){
                        Snackbar stroomSnackbar = Snackbar.make(v, R.string.voltage, Snackbar.LENGTH_SHORT);
                        stroomSnackbar.show();
                    }else{
                        fragmentTransaction.add(R.id.fragment_container, lineGraphFragment);
                        fragmentTransaction.addToBackStack(null);
                        fragmentTransaction.commit();
                        mCallback.setAttribute(0);
                    }
                    break;
                case R.id.power:
                    if(mCallback.getSelectedLeg() == -1 || mCallback.getSpiderList().size() == 0){
                        Snackbar krachtSnackbar = Snackbar.make(v, R.string.power, Snackbar.LENGTH_SHORT);
                        krachtSnackbar.show();
                    }else{
                        fragmentTransaction.add(R.id.fragment_container, lineGraphFragment);
                        fragmentTransaction.addToBackStack(null);
                        fragmentTransaction.commit();
                        mCallback.setAttribute(1);
                    }
                    break;
                case R.id.position:
                    if(mCallback.getSelectedLeg() == -1 || mCallback.getSpiderList().size() == 0){
                        Snackbar standSnackbar = Snackbar.make(v, R.string.position, Snackbar.LENGTH_SHORT);
                        standSnackbar.show();
                    }else {
                        fragmentTransaction.add(R.id.fragment_container, lineGraphFragment);
                        fragmentTransaction.addToBackStack(null);
                        fragmentTransaction.commit();
                        mCallback.setAttribute(2);
                    }
                    break;
                case R.id.torque:
                    if(mCallback.getSelectedLeg() == -1 || mCallback.getSpiderList().size() == 0){
                        Snackbar koppelSnackbar = Snackbar.make(v, R.string.torque, Snackbar.LENGTH_SHORT);
                        koppelSnackbar.show();
                    }else {
                        fragmentTransaction.add(R.id.fragment_container, lineGraphFragment);
                        fragmentTransaction.addToBackStack(null);
                        fragmentTransaction.commit();
                        mCallback.setAttribute(3);
                    }
                    break;
                case R.id.temperature:
                    if(mCallback.getSelectedLeg() == -1 || mCallback.getSpiderList().size() == 0){
                        Snackbar temperatuurSnackbar = Snackbar.make(v, R.string.temperature, Snackbar.LENGTH_SHORT);
                        temperatuurSnackbar.show();
                    }else {
                        fragmentTransaction.add(R.id.fragment_container, lineGraphFragment);
                        fragmentTransaction.addToBackStack(null);
                        fragmentTransaction.commit();
                        mCallback.setAttribute(4);
                    }
                    break;
                case R.id.coxa:
                    if(mCallback.getSelectedLeg() == -1) {
                        Snackbar coxaSnackbar = Snackbar.make(v, R.string.selectLeg, Snackbar.LENGTH_SHORT);
                        coxaSnackbar.show();
                    }
                    else if(mCallback.getSelectedLeg() == -1 || mCallback.getSpiderList().size() == 0){
                        Snackbar coxaSnackbar = Snackbar.make(v, R.string.noConnection, Snackbar.LENGTH_SHORT);
                        coxaSnackbar.show();
                    }else{
                        fragmentTransaction.add(R.id.fragment_container, lineGraphFragment);
                        fragmentTransaction.addToBackStack(null);
                        fragmentTransaction.commit();
                        mCallback.setAttribute(5);
                    }
                    break;
                case R.id.femur:
                    if(mCallback.getSelectedLeg() == -1) {
                        Snackbar femurSnackbar = Snackbar.make(v, R.string.selectLeg, Snackbar.LENGTH_SHORT);
                        femurSnackbar.show();
                    }
                    else if(mCallback.getSpiderList().size() == 0){
                        Snackbar femurSnackbar = Snackbar.make(v, R.string.noConnection, Snackbar.LENGTH_SHORT);
                        femurSnackbar.show();
                    }else{
                        fragmentTransaction.add(R.id.fragment_container, lineGraphFragment);
                        fragmentTransaction.addToBackStack(null);
                        fragmentTransaction.commit();
                        mCallback.setAttribute(6);
                    }
                    break;
                case R.id.tibia:
                    if(mCallback.getSelectedLeg() == -1) {
                        Snackbar coxaSnackbar = Snackbar.make(v, R.string.selectLeg, Snackbar.LENGTH_SHORT);
                        coxaSnackbar.show();
                    }
                    else if(mCallback.getSelectedLeg() == -1 || mCallback.getSpiderList().size() == 0){
                        Snackbar tibiaSnackbar = Snackbar.make(v, R.string.noConnection, Snackbar.LENGTH_SHORT);
                        tibiaSnackbar.show();
                    }else{
                        fragmentTransaction.add(R.id.fragment_container, lineGraphFragment);
                        fragmentTransaction.addToBackStack(null);
                        fragmentTransaction.commit();
                        mCallback.setAttribute(7);
                    }
                    break;
                case R.id.body:
                    if(mCallback.getSpiderList().size() != 0){
                        fragmentTransaction.add(R.id.fragment_container, lineGraphFragment);
                        fragmentTransaction.addToBackStack(null);
                        fragmentTransaction.commit();
                        mCallback.setAttribute(8);
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

    /**
     * Takes a spider and sets the text in the textfield to the appopriate data
     * @param spider the spider model
     */
    private void updateText(Spider spider) {
        if(spider != null) {
            if (mCallback.getSelectedLeg() != -1) {
                mCOXASTROOM.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(0).getVoltage()) + " [V]" );
                mCOXAKRACHT.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(0).getForce()) + " [N]");
                mCOXASTAND.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(0).getPosition()) + " [" + (char) 0x00B0 + "]");
                mCOXAKOPPEL.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(0).getTorque()) + " [Nm]");
                mCOXATEMPERATUUR.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(0).getTemperature()) + " [" +(char) 0x00B0 + " C]");
                mFEMURSTROOM.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(1).getVoltage()) + " [V]");
                mFEMURKRACHT.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(1).getForce()) + " [N]");
                mFEMURSTAND.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(1).getPosition()) + " [" + (char) 0x00B0 + "]");
                mFEMURKOPPEL.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(1).getTorque()) + " [Nm]");
                mFEMURTEMPERATUUR.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(1).getTemperature()) + " [" + (char) 0x00B0 + " C]");
                mTIBIASTROOM.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(2).getVoltage()) + " [V]");
                mTIBIAKRACHT.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(2).getForce()) + " [N]");
                mTIBIASTAND.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(2).getPosition()) + " [" + (char) 0x00B0 + "]");
                mTIBIAKOPPEL.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(2).getTorque()) + " [Nm]");
                mTIBIATEMPERATUUR.setText(Double.toString(spider.getLegs().get(mCallback.getSelectedLeg()).getServos().get(2).getTemperature()) + " [" + (char) 0x00B0 + " C]");
            }
        }
    }

    /*
    Creates the Menu
    */
    @Override
    public void onCreateOptionsMenu(Menu menu, MenuInflater inflater){
        inflater.inflate(R.menu.main_fragment_menu, menu);
    }

    /*
    Does something when an item in the menu gets selected
     */
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
}