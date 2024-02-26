import pandas as pd
import streamlit as st
import plotly_express as px
import plotly.graph_objects as go
import json


st.set_page_config(page_title="Sebaran Kiriman Jakarta", layout='wide')

#st.subheader("Sebaran Kiriman Per Kecamatan di Jakarta Per Bulan")
st.markdown("<h2 style='text-align: center; color: darkblue;'>Sebaran Kiriman Per Kecamatan di Jakarta Per Bulan</h2>", unsafe_allow_html=True)

col1, col2 = st.columns([2,2] ,gap="small")



with col1:
      jkt=pd.read_csv("data/file_new.csv")


      with open('data/new_jakarta.geojson') as f:
            geojson = json.load(f)


      df = pd.DataFrame(
    {"distrik": pd.json_normalize(geojson["features"])["properties.WADMKC"]}
).assign(kec=lambda d: d["distrik"].str.upper())


      for kec in df['kec'].to_list():
            jkt.loc[ jkt['join'].str.contains(kec), 'kec'] = kec

      bulan=jkt['bulan'].drop_duplicates().reset_index(drop=True).sort_index(ascending=True)
      pilihan=st.radio("A", key=1, options= bulan, label_visibility= "collapsed",horizontal=True)
      data_hasil= jkt[(jkt['bulan'] == pilihan)]



      new = data_hasil[data_hasil['pod'].isin(['C','Y'])]
      new_1= p_table = pd.pivot_table(new, index= ['kec'],  columns=['pod'], values='konid', aggfunc = 'count' ).fillna(0).reset_index()
      new_2=data_hasil.groupby(['kec'], as_index=False)['konid'].count()
      new_3=pd.merge(new_2, new_1, on='kec', how='left').reset_index(drop=True)
      new_3["empty"]=new_3["konid"]-new_3["Y"]-new_3["C"]

      df3=pd.merge(df, new_3, on='kec', how='left').reset_index(drop=True)





#kec_none=jkt.loc[jkt['kec'].isnull()].sort_values(by=['kab'], ascending=False)
#kec_pilih=jkt[(jkt['join'].str.contains("GD PELURU",  na = False, case=False)) & (jkt['kec'].isnull())]
#kec_pilih=jkt[(jkt['join'].str.contains("SUDIRMAN",  na = False, case=False)) & (jkt['kec'].isnull())]
      kec_pilih=data_hasil[(data_hasil['kec'].isnull())]

      st.dataframe(kec_pilih)
#st.dataframe(kec_pilih)

      df3["sukses"]=round(df3["Y"] / df3["konid"] * 100,2)
      df3["failed"]=round(df3["C"] / df3["konid"] * 100,2)
      df3["no_status"]=round(df3["empty"] / df3["konid"] * 100,2)
      df3["judul"]=df3["distrik"].astype(str)+ " : " + df3["konid"].astype(str) + " Dokumen"
      df3["Sukses"]= df3["Y"].astype(str)+ " ("+ df3["sukses"].astype(str)+" %)"
      df3["Gagal"]= df3["C"].astype(str)+ " ("+ df3["failed"].astype(str)+" %)"
      df3["No Status"]= df3["empty"].astype(str)+ " ("+ df3["no_status"].astype(str)+" %)"


      n=df3["konid"].sum()
      pod_Y=df3["Y"].sum()
      pod_C=df3["C"].sum()
      pod_empty=df3["empty"].sum()


      na=data_hasil['kec'].isna().sum()
      all=data_hasil['konid'].count()


      fig9 = px.choropleth_mapbox(df3, geojson=geojson,
                                  locations=df3["distrik"],featureidkey="properties.WADMKC",
                                  color=df3["konid"],color_continuous_scale="Viridis_r",
                           range_color=(0, 1300),
                           mapbox_style="carto-positron",
                           zoom=10, center = {"lat": -6.2089, "lon": 106.8284},
                           #zoom=10, center = {"lat": -6.202905, "lon": 106.778419},
                           opacity=0.7, height=500,
                           hover_name="judul",
                           hover_data = {'konid':False, 'distrik':False, "Sukses": True, "Gagal":True, "No Status":True}
                                    
                          
                     )#type: ignore 
      #fig9.update_traces(hovertemplate = "%{judul}")
      
      fig9.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
      fig9.update_layout(
    hoverlabel=dict(
        bgcolor="white",
        font_size=12
    )
)

      st.plotly_chart(fig9, use_container_width=True)
  
      st.markdown(f"Jumlah Kiriman UOB {pilihan} : **{all}** Dokumen")
      st.markdown(f"**{n}** / **{na}**")
      st.markdown(f"**{pod_Y}** / **{pod_C}** / **{pod_empty}**")



      
      
with col2:

      jkt_A=pd.read_csv("data/file_new.csv")

      with open('data/new_jakarta.geojson') as g:
            geojson = json.load(g)

     
      df_A = pd.DataFrame(
    {"distrik": pd.json_normalize(geojson["features"])["properties.WADMKC"]}
).assign(kec=lambda d: d["distrik"].str.upper())



      for kec in df_A['kec'].to_list():
            jkt_A.loc[ jkt_A['join'].str.contains(kec), 'kec'] = kec

      bulan_A=jkt_A['bulan'].drop_duplicates().reset_index(drop=True).sort_index(ascending=True)
      pilihan_A=st.radio("B", key=2, options= bulan_A, label_visibility= "collapsed",horizontal=True)
      data_hasil_A= jkt_A[(jkt_A['bulan'] == pilihan_A)]

  
      
     
      new_A = data_hasil_A[data_hasil_A['pod'].isin(['C','Y'])]
      new_1A= p_table = pd.pivot_table(new_A, index= ['kec'],  columns=['pod'], values='konid', aggfunc = 'count' ).fillna(0).reset_index()
      new_2A=data_hasil_A.groupby(['kec'], as_index=False)['konid'].count()
      new_3A=pd.merge(new_2A, new_1A, on='kec', how='left').reset_index(drop=True)
      new_3A["empty"]=new_3A["konid"]-new_3A["Y"]-new_3A["C"]

      df4=pd.merge(df_A, new_3A, on='kec', how='left').reset_index(drop=True)

      df4["sukses"]=round(df4["Y"] / df4["konid"] * 100,2)
      df4["failed"]=round(df4["C"] / df4["konid"] * 100,2)
      df4["no_status"]=round(df4["empty"] / df4["konid"] * 100,2)
      df4["judul"]=df4["distrik"].astype(str)+ " : " + df4["konid"].astype(str) + " Dokumen"
      df4["Sukses"]= df4["Y"].astype(str)+ " ("+ df4["sukses"].astype(str)+" %)"
      df4["Gagal"]= df4["C"].astype(str)+ " ("+ df4["failed"].astype(str)+" %)"
      df4["No Status"]= df4["empty"].astype(str)+ " ("+ df4["no_status"].astype(str)+" %)"


      n4=df4["konid"].sum()
      pod_Y4=df4["Y"].sum()
      pod_C4=df4["C"].sum()
      pod_empty4=df4["empty"].sum()


      na4=data_hasil_A['kec'].isna().sum()
      all4=data_hasil_A['konid'].count()


      fig4 = px.choropleth_mapbox(df4, geojson=geojson,
                                  locations=df4["distrik"],featureidkey="properties.WADMKC",
                                  color=df4["konid"],color_continuous_scale="Viridis_r",
                           range_color=(0, 1300),
                           mapbox_style="carto-positron",
                           zoom=10, center = {"lat": -6.2089, "lon": 106.8284},
                           #zoom=10, center = {"lat": -6.202905, "lon": 106.778419},
                           opacity=0.7, height=500,
                           hover_name="judul",
                           hover_data = {'konid':False, 'distrik':False, "Sukses": True, "Gagal":True, "No Status":True}
                                    
                          
                     )#type: ignore 
      #fig9.update_traces(hovertemplate = "%{judul}")
      
      fig4.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
      fig4.update_layout(
    hoverlabel=dict(
        bgcolor="white",
        font_size=12
    )
)

      st.plotly_chart(fig4, use_container_width=True)
  
      st.markdown(f"Jumlah Kiriman UOB {pilihan_A} : **{all4}** Dokumen")
      st.markdown(f"**{n4}** / **{na4}**")
      st.markdown(f"**{pod_Y4}** / **{pod_C4}** / **{pod_empty4}**")

