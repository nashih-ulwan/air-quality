import streamlit as st 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.io as pio

pio.templates.default = "plotly_dark"
sns.set_style("darkgrid")

st.title('Air Quality in Beijing')
st.write("This dashboard was created using Streamlit as a final project assignment for the \"Belajar Analisis Data dengan Python\" course. In this dashboard, you will find the results of analysis in the form of visualizations related to Air Quality in Beijing.")

st.header("Dataset")
st.write(
    """
    This dataset contains about substances or particles that present in the air and can be referred as an air pollutant from 11 station in Beijing, China. 
    """
)


#Data collecting
#membaca data
df_aotizhongxin = pd.read_csv("https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Aotizhongxin_20130301-20170228.csv")
df_changping = pd.read_csv("https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Changping_20130301-20170228.csv")
df_dingling = pd.read_csv("https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Dingling_20130301-20170228.csv")
df_dongsi = pd.read_csv("https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Dongsi_20130301-20170228.csv")
df_guanyuan = pd.read_csv("https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Guanyuan_20130301-20170228.csv")
df_gucheng = pd.read_csv("https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Gucheng_20130301-20170228.csv")
df_huairou = pd.read_csv("https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Huairou_20130301-20170228.csv")
df_nongzhanguan = pd.read_csv("https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Nongzhanguan_20130301-20170228.csv")
df_shunyi = pd.read_csv("https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Aotizhongxin_20130301-20170228.csv")
df_tiantan = pd.read_csv("https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Tiantan_20130301-20170228.csv")
df_wanliu = pd.read_csv("https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Wanliu_20130301-20170228.csv")
df_wanshouxigong = pd.read_csv("https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Wanshouxigong_20130301-20170228.csv")

#Menggabungkan data menjadi satu dataframe
df = pd.concat([df_aotizhongxin,df_changping, df_dingling, df_dongsi, df_guanyuan, df_gucheng, df_huairou, df_nongzhanguan, df_shunyi, df_tiantan, df_wanliu, df_wanshouxigong])

#Imputing misssing value
df["PM2.5"].fillna(df["PM2.5"].median(), inplace=True)
df["PM10"].fillna(df["PM10"].median(), inplace=True)
df["SO2"].fillna(df["SO2"].median(), inplace=True)
df["NO2"].fillna(df["NO2"].median(), inplace=True)
df["O3"].fillna(df["O3"].median(), inplace=True)
df["CO"].fillna(df["CO"].median(), inplace=True)
df["TEMP"].fillna(df["TEMP"].mean(), inplace=True)
df["PRES"].fillna(df["PRES"].mean(), inplace=True)
df["DEWP"].fillna(df["DEWP"].mean(), inplace=True)
df["RAIN"].fillna(df["RAIN"].median(), inplace=True)
df["WSPM"].fillna(df["WSPM"].median(), inplace=True)

st.write("Head of the datasets")
st.dataframe(data=df.head(5), width=800, height=150)
st.write("Tail of the datasets")
st.dataframe(data=df.tail(5), width=800, height=150)

grouped_df = df[["PM2.5","PM10","SO2","NO2","CO","O3","TEMP","PRES","DEWP","RAIN","WSPM", 'station']].groupby("station").mean(numeric_only=True)
grouped_df = grouped_df.reset_index()
 
#

st.header("Air Quality Based on Station")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12 = st.tabs(['Aotizhongxin', 'Changping', 'Dingling', 'Dongsi', 'Guanyuan',
       'Gucheng', 'Huairou', 'Nongzhanguan', 'Tiantan', 'Wanliu',
       'Wanshouxigong', "All"])
 
with tab1:
    st.subheader("Aotizhongxin")
    st.write("Average substances level by year")
    df_1 = df[df["station"]=="Aotizhongxin"].groupby("year").mean(numeric_only=True).reset_index()
    
    #graph 1
    df1_long1=pd.melt(df_1, id_vars=['year'], value_vars=["PM2.5","PM10","SO2","NO2","O3"])
    fig = px.line(df1_long1, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
    #graph 2
    df1_long2=pd.melt(df_1, id_vars=['year'], value_vars=["CO", "PRES"])
    fig = px.line(df1_long2, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
    #graph 3
    df1_long3=pd.melt(df_1, id_vars=['year'], value_vars=["TEMP", "RAIN", "WSPM"])
    fig = px.line(df1_long3, x="year", y="value", color="variable")
    st.plotly_chart(fig)
with tab2:
    st.subheader("Changping")
    st.write("Average substances level by year")
    df_2 = df[df["station"]=="Changping"].groupby("year").mean(numeric_only=True).reset_index()
    
    #graph 1
    df2_long1=pd.melt(df_2, id_vars=['year'], value_vars=["PM2.5","PM10","SO2","NO2","O3"])
    fig = px.line(df2_long1, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
    #graph 2
    df2_long2=pd.melt(df_2, id_vars=['year'], value_vars=["CO", "PRES"])
    fig = px.line(df2_long2, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
    #graph 3
    df2_long3=pd.melt(df_2, id_vars=['year'], value_vars=["TEMP", "RAIN", "WSPM"])
    fig = px.line(df2_long3, x="year", y="value", color="variable")
    st.plotly_chart(fig)
with tab3:
    st.subheader("Dingling")
    st.write("Average substances level by year")
    df_3 = df[df["station"]=="Dingling"].groupby("year").mean(numeric_only=True).reset_index()
    
    #graph 1
    df3_long1=pd.melt(df_3, id_vars=['year'], value_vars=["PM2.5","PM10","SO2","NO2","O3"])
    fig = px.line(df3_long1, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
    #graph 2
    df3_long2=pd.melt(df_3, id_vars=['year'], value_vars=["CO", "PRES"])
    fig = px.line(df3_long2, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
    #graph 3
    df3_long3=pd.melt(df_3, id_vars=['year'], value_vars=["TEMP", "RAIN", "WSPM"])
    fig = px.line(df3_long3, x="year", y="value", color="variable")
    st.plotly_chart(fig)
with tab4:
    st.subheader("Dongsi")
    st.write("Average substances level by year")
    df_4 = df[df["station"]=="Dingling"].groupby("year").mean(numeric_only=True).reset_index()
    #graph 1
    df4_long1=pd.melt(df_4, id_vars=['year'], value_vars=["PM2.5","PM10","SO2","NO2","O3"])
    fig = px.line(df4_long1, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
    #graph 2
    df4_long2=pd.melt(df_4, id_vars=['year'], value_vars=["CO", "PRES"])
    fig = px.line(df4_long2, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
    #graph 3
    df4_long3=pd.melt(df_4, id_vars=['year'], value_vars=["TEMP", "RAIN", "WSPM"])
    fig = px.line(df4_long3, x="year", y="value", color="variable")
    st.plotly_chart(fig)
        
with tab5:
    st.subheader("Guanyuan")  
    st.write("Average substances level by year")
    df_5 = df[df["station"]=="Guanyuan"].groupby("year").mean(numeric_only=True).reset_index()
    #graph 1
    df5_long1=pd.melt(df_5, id_vars=['year'], value_vars=["PM2.5","PM10","SO2","NO2","O3"])
    fig = px.line(df5_long1, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
    #graph 2
    df5_long2=pd.melt(df_5, id_vars=['year'], value_vars=["CO", "PRES"])
    fig = px.line(df5_long2, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
    #graph 3
    df5_long3=pd.melt(df_4, id_vars=['year'], value_vars=["TEMP", "RAIN", "WSPM"])
    fig = px.line(df5_long3, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
with tab6:
    st.subheader("Gucheng")
    st.write("Average substances level by year")  
    df_6 = df[df["station"]=="Gucheng"].groupby("year").mean(numeric_only=True).reset_index()
    #graph 1
    df6_long1=pd.melt(df_6, id_vars=['year'], value_vars=["PM2.5","PM10","SO2","NO2","O3"])
    fig = px.line(df6_long1, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
    #graph 2
    df6_long2=pd.melt(df_6, id_vars=['year'], value_vars=["CO", "PRES"])
    fig = px.line(df6_long2, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
    #graph 3
    df6_long3=pd.melt(df_6, id_vars=['year'], value_vars=["TEMP", "RAIN", "WSPM"])
    fig = px.line(df6_long3, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
with tab7:
    st.subheader("Huairou") 
    st.write("Average substances level by year")
    df_7 = df[df["station"]=="Huairou"].groupby("year").mean(numeric_only=True).reset_index()
    #graph 1
    df7_long1=pd.melt(df_7, id_vars=['year'], value_vars=["PM2.5","PM10","SO2","NO2","O3"])
    fig = px.line(df7_long1, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
    #graph 2
    df7_long2=pd.melt(df_7, id_vars=['year'], value_vars=["CO", "PRES"])
    fig = px.line(df7_long2, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
    #graph 3
    df7_long3=pd.melt(df_7, id_vars=['year'], value_vars=["TEMP", "RAIN", "WSPM"])
    fig = px.line(df7_long3, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
with tab8:
    st.subheader("Nongzhanguan")  
    st.write("Average substances level by year")
    df_8 = df[df["station"]=="Nongzhanguan"].groupby("year").mean(numeric_only=True).reset_index()
    #graph 1
    df8_long1=pd.melt(df_8, id_vars=['year'], value_vars=["PM2.5","PM10","SO2","NO2","O3"])
    fig = px.line(df8_long1, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
    #graph 2
    df8_long2=pd.melt(df_8, id_vars=['year'], value_vars=["CO", "PRES"])
    fig = px.line(df8_long2, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
    #graph 3
    df8_long3=pd.melt(df_8, id_vars=['year'], value_vars=["TEMP", "RAIN", "WSPM"])
    fig = px.line(df8_long3, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
with tab9:
    st.subheader("Tiantan")   
    st.write("Average substances level by year")
    df_9 = df[df["station"]=="Tiantan"].groupby("year").mean(numeric_only=True).reset_index()
    #graph 1
    df9_long1=pd.melt(df_9, id_vars=['year'], value_vars=["PM2.5","PM10","SO2","NO2","O3"])
    fig = px.line(df9_long1, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
    #graph 2
    df9_long2=pd.melt(df_9, id_vars=['year'], value_vars=["CO", "PRES"])
    fig = px.line(df9_long2, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
    #graph 3
    df9_long3=pd.melt(df_9, id_vars=['year'], value_vars=["TEMP", "RAIN", "WSPM"])
    fig = px.line(df9_long3, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
with tab10:
    st.subheader("Wanliu")  
    st.write("Average substances level by year")
    df_10 = df[df["station"]=="Wanliu"].groupby("year").mean(numeric_only=True).reset_index()
    #graph 1
    df10_long1=pd.melt(df_10, id_vars=['year'], value_vars=["PM2.5","PM10","SO2","NO2","O3"])
    fig = px.line(df10_long1, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
    #graph 2
    df10_long2=pd.melt(df_10, id_vars=['year'], value_vars=["CO", "PRES"])
    fig = px.line(df10_long2, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
    #graph 3
    df10_long3=pd.melt(df_10, id_vars=['year'], value_vars=["TEMP", "RAIN", "WSPM"])
    fig = px.line(df10_long3, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
with tab11:
    st.subheader("Wanshouxigong")  
    st.write("Average substances level by year")
    df_11 = df[df["station"]=="Wanshouxigong"].groupby("year").mean(numeric_only=True).reset_index()
    #graph 1
    df11_long1=pd.melt(df_11, id_vars=['year'], value_vars=["PM2.5","PM10","SO2","NO2","O3"])
    fig = px.line(df11_long1, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
    #graph 2
    df11_long2=pd.melt(df_11, id_vars=['year'], value_vars=["CO", "PRES"])
    fig = px.line(df11_long2, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
    #graph 3
    df11_long3=pd.melt(df_11, id_vars=['year'], value_vars=["TEMP", "RAIN", "WSPM"])
    fig = px.line(df11_long3, x="year", y="value", color="variable")
    st.plotly_chart(fig)

with tab12:
    st.subheader("All")
    st.write("Average substances level by year")
    year_grouped_df = df[["PM2.5","PM10","SO2","NO2","CO","O3","TEMP","PRES","DEWP","RAIN","WSPM", "year"]].groupby("year").mean(numeric_only=True).reset_index()
    #graph 1
    df_long=pd.melt(year_grouped_df, id_vars=['year'], value_vars=["PM2.5","PM10","SO2","NO2","O3"])
    fig = px.line(df_long, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
    #graph 2
    df_long2=pd.melt(year_grouped_df, id_vars=['year'], value_vars=["CO", "PRES"])
    fig = px.line(df_long2, x="year", y="value", color="variable")
    st.plotly_chart(fig)
    
    #graph 3
    df_long3=pd.melt(year_grouped_df, id_vars=['year'], value_vars=["TEMP", "RAIN", "WSPM"])
    fig = px.line(df_long3, x="year", y="value", color="variable")
    st.plotly_chart(fig)

st.header("Every Substances in each Station")

#tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(['PM2.5', 'PM10', 'SO2', 'N02', 'CO','O3', 'TEMP', 'PRES', 'RAIN'])
fig = go.Figure(go.Bar(x=grouped_df["station"], y=grouped_df["PM2.5"], name='PM2.5'))
fig.add_trace(go.Bar(x=grouped_df["station"], y=grouped_df["PM10"], name='PM10'))
fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})    
st.plotly_chart(fig)

fig = go.Figure(go.Bar(x=grouped_df["station"], y=grouped_df["SO2"], name='SO2'))
fig.add_trace(go.Bar(x=grouped_df["station"], y=grouped_df["NO2"], name='NO2'))
fig.add_trace(go.Bar(x=grouped_df["station"], y=grouped_df["CO"], name='CO'))
fig.add_trace(go.Bar(x=grouped_df["station"], y=grouped_df["O3"], name='O3'))
fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
st.plotly_chart(fig)

fig = go.Figure(go.Bar(x=grouped_df["station"], y=grouped_df["PRES"], name='PRES'))
fig.add_trace(go.Bar(x=grouped_df["station"], y=grouped_df["RAIN"]*1000, name='RAIN'))
fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
    
st.plotly_chart(fig)
        
fig = go.Figure(go.Bar(x=grouped_df["station"], y=grouped_df["TEMP"], name='TEMP'))
fig.add_trace(go.Bar(x=grouped_df["station"], y=grouped_df["WSPM"], name='WSPM'))

fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
    
st.plotly_chart(fig)

st.header("Conclusion")
st.write("1. The conclusion from the first question is that each station in Beijing tends to exhibit a similar pattern of increase and decrease in substances from 2013 to 2017. However, there are differences in the levels of each substance in each station.")
st.write("2. The conclusion from the second question is that for PM2.5 and PM10 pollutants, the Gucheng station has the highest levels, while the Dingling station has the lowest levels. As for SO2, NO2, CO, and O3 pollutants, the Wansouxigong station has the highest levels, while the Dingling station has the lowest levels. From these observations, it can be inferred that the Dingling station has the best air quality. Additionally, the rainfall, pressure, and temperature at each station tend to be similar, but the temperature at the Huariou station tends to be lower compared to the other stations.")





