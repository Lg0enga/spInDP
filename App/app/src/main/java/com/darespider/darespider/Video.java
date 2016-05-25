package com.darespider.darespider;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.webkit.WebSettings;
import android.webkit.WebView;

/**
 * Created by Allard on 17-5-2016.
 */
public class Video extends AppCompatActivity {

    private WebView mVID;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.video);

        mVID = (WebView) findViewById(R.id.vid);
        mVID.loadUrl("http://10.42.0.28");

        WebSettings webSettings = mVID.getSettings();
        webSettings.setJavaScriptEnabled(true);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu){
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.video_menu, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item){
        switch (item.getItemId()){
            case R.id.mainPage:
                finish();
                return true;
            default:
                return super.onOptionsItemSelected(item);
        }
    }
}
