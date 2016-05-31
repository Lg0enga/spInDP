package com.darespider.darespider.model;

import android.os.Parcel;
import android.os.Parcelable;

import java.util.List;
import com.google.gson.annotations.SerializedName;
/**
 * Created by Allard on 19-5-2016.
 */
public class Servo implements Parcelable {
    @SerializedName("id")
    int Id;

    @SerializedName("temperature")
    double Temperature;

    @SerializedName("voltage")
    double Voltage;

    @SerializedName("force")
    double Force;

    @SerializedName("position")
    double Position;

    @SerializedName("torque")
    double Torque;

    public int getId(){
        return Id;
    }

    public void setId(int id){
        Id = id;
    }

    public double getTemperature(){
        return Temperature;
    }

    public void setTemperature(double temperature){
        Temperature = temperature;
    }

    public double getVoltage(){
        return Voltage;
    }

    public void setVoltage(double voltage){
        Voltage = voltage;
    }

    public double getForce(){
        return Force;
    }

    public void setForce(double force){
        Force = force;
    }

    public double getPosition(){
        return Position;
    }

    public void setPosition(double position){
        Position = position;
    }

    public double getTorque(){
        return Torque;
    }

    public void setTorque(double torque){
        Torque = torque;
    }

    public Servo(){}

    protected Servo(Parcel in) {
        Id = in.readInt();
        Temperature = in.readDouble();
        Voltage = in.readDouble();
        Force = in.readDouble();
        Position = in.readDouble();
        Torque = in.readDouble();
    }

    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel dest, int flags) {
        dest.writeInt(Id);
        dest.writeDouble(Temperature);
        dest.writeDouble(Voltage);
        dest.writeDouble(Force);
        dest.writeDouble(Position);
        dest.writeDouble(Torque);
    }

    @SuppressWarnings("unused")
    public static final Parcelable.Creator<Servo> CREATOR = new Parcelable.Creator<Servo>() {
        @Override
        public Servo createFromParcel(Parcel in) {
            return new Servo(in);
        }

        @Override
        public Servo[] newArray(int size) {
            return new Servo[size];
        }
    };
}