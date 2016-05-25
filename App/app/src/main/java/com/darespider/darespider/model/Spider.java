package com.darespider.darespider.model;

import android.os.Parcel;
import android.os.Parcelable;

import com.google.gson.annotations.SerializedName;

import java.util.ArrayList;

/**
 * Created by Allard on 19-5-2016.
 */
public class Spider implements Parcelable {

    @SerializedName("battery_percentage")
    int BatteryPercentage;

    @SerializedName("spider_angle")
    double SpiderAngle;

    @SerializedName("legs")
    ArrayList<Leg> Legs;

    public int getBatteryPercentage(){
        return BatteryPercentage;
    }

    public void setBatteryPercentage(int batteryPercentage){
        BatteryPercentage = batteryPercentage;
    }

    public double getSpiderAngle(){
        return SpiderAngle;
    }

    public void setSpiderAngle(double spiderAngle){
        SpiderAngle = spiderAngle;
    }

    public ArrayList<Leg> getLegs(){
        return Legs;
    }

    public void setLeg(ArrayList<Leg> legs){
        Legs = legs;
    }

    public Spider(){}

    protected Spider(Parcel in) {
        BatteryPercentage = in.readInt();
        SpiderAngle = in.readDouble();
        if (in.readByte() == 0x01) {
            Legs = new ArrayList<Leg>();
            in.readList(Legs, Leg.class.getClassLoader());
        } else {
            Legs = null;
        }
    }

    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel dest, int flags) {
        dest.writeInt(BatteryPercentage);
        dest.writeDouble(SpiderAngle);
        if (Legs == null) {
            dest.writeByte((byte) (0x00));
        } else {
            dest.writeByte((byte) (0x01));
            dest.writeList(Legs);
        }
    }

    @SuppressWarnings("unused")
    public static final Parcelable.Creator<Spider> CREATOR = new Parcelable.Creator<Spider>() {
        @Override
        public Spider createFromParcel(Parcel in) {
            return new Spider(in);
        }

        @Override
        public Spider[] newArray(int size) {
            return new Spider[size];
        }
    };
}