package com.darespider.darespider;

import android.app.Activity;
import android.app.Fragment;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

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

    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.video_fragment, container, false);

        return view;
    }
}
