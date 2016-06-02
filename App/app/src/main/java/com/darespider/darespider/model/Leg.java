package com.darespider.darespider.model;


import android.os.Parcel;
import android.os.Parcelable;

import com.google.gson.annotations.SerializedName;

import java.util.ArrayList;
import java.util.List;

import com.darespider.darespider.model.Servo;

/**
 * Created by Allard on 19-5-2016.
 */
public class Leg implements Parcelable {
    @SerializedName("servos")
    ArrayList<Servo> Servos;

    public ArrayList<Servo> getServos(){
        return Servos;
    }

    public void setServo(ArrayList<Servo> servo){
        Servos = servo;
    }

    public Leg(){}

    protected Leg(Parcel in) {
        if (in.readByte() == 0x01) {
            Servos = new ArrayList<Servo>();
            in.readList(Servos, Servo.class.getClassLoader());
        } else {
            Servos = null;
        }
    }

    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel dest, int flags) {
        if (Servos == null) {
            dest.writeByte((byte) (0x00));
        } else {
            dest.writeByte((byte) (0x01));
            dest.writeList(Servos);
        }
    }

    @SuppressWarnings("unused")
    public static final Parcelable.Creator<Leg> CREATOR = new Parcelable.Creator<Leg>() {
        @Override
        public Leg createFromParcel(Parcel in) {
            return new Leg(in);
        }

        @Override
        public Leg[] newArray(int size) {
            return new Leg[size];
        }
    };
}