package com.darespider.darespider;

import android.content.Intent;
import android.os.Handler;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.ImageButton;
import android.widget.ProgressBar;
import android.widget.TextView;

import java.util.ArrayList;
import java.lang.Double;
import java.util.Timer;
import java.util.TimerTask;

import com.bumptech.glide.Glide;

import com.darespider.darespider.api.SpiderService;
import com.darespider.darespider.model.Spider;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.GsonConverterFactory;
import retrofit2.Response;
import retrofit2.Retrofit;

public class MainActivity extends AppCompatActivity {


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

    private TestActivity mTestActivity;
    public static Spider mSPIDER = new Spider();

    public static int iterator = 0;
    public static int seconds = 0;
    public static ArrayList<Spider> spiderArrayList = new ArrayList<>();
    public static int attribute = -1;
    public static int selectedLeg = -1;
    class RefreshData extends TimerTask {
        public void run() {
            getData();

        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Timer timer = new Timer();
        Timer timer2 = new Timer();
        timer.schedule(new RefreshData(), 0, 1000);

        timer2.schedule(new TimerTask() {
            @Override
            public void run() {
                if (spiderArrayList == null)
                    spiderArrayList = new ArrayList<>();
                if (spiderArrayList.size() >= 10){
                    spiderArrayList.remove(0);
                }
                iterator++;
                seconds+=5;
                spiderArrayList.add(mSPIDER);
            }
        },0, 5000);



        mBATTERIJ = (ProgressBar) findViewById(R.id.batterij);

        mLFL = (ImageButton) findViewById(R.id.lfl);
        mLML = (ImageButton) findViewById(R.id.lml);
        mLRL = (ImageButton) findViewById(R.id.lrl);
        mBODY = (ImageButton) findViewById(R.id.body);
        mLFR = (ImageButton) findViewById(R.id.lfr);
        mLMR = (ImageButton) findViewById(R.id.lmr);
        mLRR = (ImageButton) findViewById(R.id.lrr);
        mSTROOM = (ImageButton) findViewById(R.id.stroom);
        mKRACHT = (ImageButton) findViewById(R.id.kracht);
        mSTAND = (ImageButton) findViewById(R.id.stand);
        mKOPPEL = (ImageButton) findViewById(R.id.koppel);
        mTEMPERATUUR = (ImageButton) findViewById(R.id.temperatuur);

        mBATTERIJPERCENTAGE = (TextView) findViewById(R.id.batterijPercentage);
        mHELLING = (TextView) findViewById(R.id.hellingNummer);
        mPOOT = (TextView) findViewById(R.id.poot);
        mCOXASTROOM = (TextView) findViewById(R.id.coxaStroom);
        mCOXAKRACHT = (TextView) findViewById(R.id.coxaKracht);
        mCOXASTAND = (TextView) findViewById(R.id.coxaStand);
        mCOXAKOPPEL = (TextView) findViewById(R.id.coxaKoppel);
        mCOXATEMPERATUUR = (TextView) findViewById(R.id.coxaTemperatuur);
        mFEMURSTROOM = (TextView) findViewById(R.id.femurStroom);
        mFEMURKRACHT = (TextView) findViewById(R.id.femurKracht);
        mFEMURSTAND = (TextView) findViewById(R.id.femurStand);
        mFEMURKOPPEL = (TextView) findViewById(R.id.femurKoppel);
        mFEMURTEMPERATUUR = (TextView) findViewById(R.id.femurTemperatuur);
        mTIBIASTROOM = (TextView) findViewById(R.id.tibiaStroom);
        mTIBIAKRACHT = (TextView) findViewById(R.id.tibiaKracht);
        mTIBIASTAND = (TextView) findViewById(R.id.tibiaStand);
        mTIBIAKOPPEL = (TextView) findViewById(R.id.tibiaKoppel);
        mTIBIATEMPERATUUR = (TextView) findViewById(R.id.tibiaTemperatuur);

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

        mTestActivity = new TestActivity();
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

                MainActivity.this.mSPIDER = spider;

                MainActivity.this.updateText(spider);
                MainActivity.this.mBATTERIJ.setProgress(spider.getBatteryPercentage());
                MainActivity.this.mBATTERIJPERCENTAGE.setText(Integer.toString(spider.getBatteryPercentage()) + "%");
                MainActivity.this.mHELLING.setText(Double.toString(spider.getSpiderAngle()) + (char) 0x00B0);
            }

            @Override
            public void onFailure(Call<Spider> call, Throwable t) {

            }
        });

    }

    public class ButtonHandler implements OnClickListener {

        private LineGraph mLineGraph;
        @Override
        public void onClick(View v) {
            switch (v.getId()) {
                case R.id.stroom:
                    attribute = 0;
                    mLineGraph = new LineGraph();
                    Intent intent = new Intent(MainActivity.this, mLineGraph.getClass());
                    startActivity(intent);
                    break;
                case R.id.kracht:
                    attribute = 1;
                    Snackbar krachtSnackbar = Snackbar.make(v, "kracht", Snackbar.LENGTH_SHORT);
                    krachtSnackbar.show();
                    break;
                case R.id.stand:
                    attribute = 2;
                    Snackbar standSnackbar = Snackbar.make(v, "stand", Snackbar.LENGTH_SHORT);
                    standSnackbar.show();
                    break;
                case R.id.koppel:
                    attribute = 3;
                    Snackbar koppelSnackbar = Snackbar.make(v, "koppel", Snackbar.LENGTH_SHORT);
                    koppelSnackbar.show();
                    break;
                case R.id.temperatuur:
                    attribute = 4;
                    Snackbar temperatuurSnackbar = Snackbar.make(v, "temperatuur", Snackbar.LENGTH_SHORT);
                    temperatuurSnackbar.show();
                    break;
                case R.id.lfl:
                    selectedLeg = 0;
                    mPOOT.setText("Linker VoorPoot");
                    updateText(mSPIDER);
                    break;
                case R.id.lml:
                    selectedLeg = 1;
                    mPOOT.setText("Linker Middenpoot");
                    updateText(mSPIDER);
                    break;
                case R.id.lrl:
                    selectedLeg = 2;
                    mPOOT.setText("Linker Achterpoot");
                    updateText(mSPIDER);
                    break;
                case R.id.lfr:
                    selectedLeg = 3;
                    mPOOT.setText("Rechter Voorpoot");
                    updateText(mSPIDER);
                    break;
                case R.id.lmr:
                    selectedLeg = 4;
                    mPOOT.setText("Rechter Middenpoot");
                    updateText(mSPIDER);
                    break;
                case R.id.lrr:
                    selectedLeg = 5;
                    mPOOT.setText("Rechter Achterpoot");
                    updateText(mSPIDER);
                    break;
            }
        }
    }

    private void updateText(Spider spider) {
        if(selectedLeg != -1) {
            mCOXASTROOM.setText(Double.toString(spider.getLegs().get(selectedLeg).getServos().get(0).getVoltage()));
            mCOXAKRACHT.setText(Double.toString(spider.getLegs().get(selectedLeg).getServos().get(0).getForce()));
            mCOXASTAND.setText(Double.toString(spider.getLegs().get(selectedLeg).getServos().get(0).getPosition()));
            mCOXAKOPPEL.setText(Double.toString(spider.getLegs().get(selectedLeg).getServos().get(0).getTorque()));
            mCOXATEMPERATUUR.setText(Double.toString(spider.getLegs().get(selectedLeg).getServos().get(0).getTemperature()));
            mFEMURSTROOM.setText(Double.toString(spider.getLegs().get(selectedLeg).getServos().get(1).getVoltage()));
            mFEMURKRACHT.setText(Double.toString(spider.getLegs().get(selectedLeg).getServos().get(1).getForce()));
            mFEMURSTAND.setText(Double.toString(spider.getLegs().get(selectedLeg).getServos().get(1).getPosition()));
            mFEMURKOPPEL.setText(Double.toString(spider.getLegs().get(selectedLeg).getServos().get(1).getTorque()));
            mFEMURTEMPERATUUR.setText(Double.toString(spider.getLegs().get(selectedLeg).getServos().get(1).getTemperature()));
            mTIBIASTROOM.setText(Double.toString(spider.getLegs().get(selectedLeg).getServos().get(2).getVoltage()));
            mTIBIAKRACHT.setText(Double.toString(spider.getLegs().get(selectedLeg).getServos().get(2).getForce()));
            mTIBIASTAND.setText(Double.toString(spider.getLegs().get(selectedLeg).getServos().get(2).getPosition()));
            mTIBIAKOPPEL.setText(Double.toString(spider.getLegs().get(selectedLeg).getServos().get(2).getTorque()));
            mTIBIATEMPERATUUR.setText(Double.toString(spider.getLegs().get(selectedLeg).getServos().get(2).getTemperature()));
        }
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.main_activity_menu, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        switch (item.getItemId()) {
            case R.id.video:
                startActivity(new Intent(MainActivity.this, Video.class));
                return true;
            default:
                return super.onOptionsItemSelected(item);
        }
    }

    public ArrayList<Spider> getSpiderArrayList(){
        return spiderArrayList;
    }
}
