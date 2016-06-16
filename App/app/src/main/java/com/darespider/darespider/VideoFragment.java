package com.darespider.darespider;

import android.app.Activity;
import android.app.Fragment;
import android.net.Uri;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.webkit.WebView;

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

        Uri uri = Uri.parse("tcp/h264://10.42.0.80:9000");
        String url1 ="tcp/h264://10.42.0.76:9000";
        String url="https://www.google.com";
        WebView web = (WebView) view.findViewById(R.id.vid);
        web.getSettings().setJavaScriptEnabled(true);


        return view;
    }
}
