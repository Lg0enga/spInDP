package com.darespider.darespider;

import android.app.Activity;
import android.app.Fragment;
import android.net.Uri;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.webkit.HttpAuthHandler;
import android.webkit.WebView;
import android.webkit.WebViewClient;

import com.darespider.darespider.R;

/**
 * Created by Allard on 26-5-2016.
 */
public class VideoFragment extends Fragment{

    OnVideoFragmentListener mCallback;

    public interface OnVideoFragmentListener{

    }

    public void onAttach(Activity activity) {
        super.onAttach(activity);

        try {
            mCallback = (OnVideoFragmentListener) activity;
        } catch (ClassCastException e) {
            throw new ClassCastException(activity.toString()
                    + " must implement OnVideoFragmentListener");
        }
    }

    //Creates the view for the video fragment.
    //Takes an ip address as a string an converts it to a url.
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.video_fragment, container, false);

        String video = "http://172.24.1.1/html";
        WebView web = (WebView) view.findViewById(R.id.vid);

        web.setWebViewClient(new MyWebViewClient());


        web.loadUrl(video);
        web.getSettings().setJavaScriptEnabled(true);


        return view;
    }
    private class MyWebViewClient extends WebViewClient {
        public void onReceivedHttpAuthRequest(WebView view,
                                              HttpAuthHandler handler, String host, String realm) {

            handler.proceed("darespider", "darespider12301");

        }
    }
}
