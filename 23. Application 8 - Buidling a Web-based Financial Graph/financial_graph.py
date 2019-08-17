# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 22:38:11 2019

@author: viren
"""

from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file

start=datetime.datetime(2016,3,2);
end=datetime.datetime(2016,5,10);
df=data.DataReader(name="GOOG",data_source="yahoo",start=start,end=end);

def inc_dec(c,o):
    if c>o:
        value="Increase";
    elif c<o:
        value="Decrease";
    else:
        value="Equal";
    return value;

df["Status"]=[inc_dec(c,o) for c, o in zip(df.Close,df.Open)];
df["Middle"]=(df.Open + df.Close)/2;
df["Height"]=abs(df.Close-df.Open);
hours_12=12*60*60*1000; 

p=figure(x_axis_type='datetime',width=1500,height=500, title="Candlestick Chart");
p.grid.grid_line_alpha=0.3;

p.segment(df.index, df.High, df.index, df.Low, color="Black");
p.rect(df.index[df.Status=="Increase"],df.Middle[df.Status=="Increase"], hours_12, df.Height[df.Status=="Increase"],
       fill_color="blue",line_color="black");
p.rect(df.index[df.Status=="Decrease"],df.Middle[df.Status=="Decrease"], hours_12, df.Height[df.Status=="Decrease"], 
       fill_color="orange",line_color="black");

output_file("Candlestick.html");
show(p);