import pandas as pd
import streamlit as st
import plotly_express as px
import plotly.graph_objects as go
import json


st.set_page_config(page_title="Sebaran Kiriman Jakarta", layout='wide')

col1, col2 = st.columns([5,2] ,gap="small")

jkt=pd.read_excel("data/UOB_jkt_sept_update4okt.xlsx")
jkt["join"]=jkt["alam5"].astype(str) +" " + jkt["alam6"].astype(str)
jkt['pod'].fillna("empty",inplace=True)


with open('data/new_jakarta.geojson') as f:
      geojson = json.load(f)



df = pd.DataFrame(
    {"distrik": pd.json_normalize(geojson["features"])["properties.WADMKC"]}
).assign(kec=lambda d: d["distrik"].str.upper())


for kec in df['kec'].to_list():
  jkt.loc[ jkt['join'].str.contains(kec), 'kec'] = kec

kec_2=[["PALMERAH", "KBN JERUK"], ["PAL MERAH", "KEBON JERUK"]]
df_kec=pd.DataFrame(kec_2, columns=['alias', 'kec_alias'])

for alias in df_kec['kec_alias'].to_list():
  jkt.loc[ jkt['join'].str.contains(alias), 'kec_alias'] = kec



st.dataframe(df_kec)
st.dataframe(jkt)


p_table = pd.pivot_table(jkt, index= ['kec'],  columns=['pod'], values='konid', aggfunc = 'count' ).fillna(0).reset_index()

df2 = jkt.groupby(['kec'], as_index=False)['konid'].count()
df2a= jkt.groupby(['kec', 'pod'], as_index=False)['konid'].count()
df3 = pd.merge(pd.merge(df, df2, on='kec', how='left'), p_table, on='kec', how='left').reset_index(drop=True)

df3["sukses"]=round(df3["Y"] / df3["konid"] * 100,2)
df3["failed"]=round(df3["C"] / df3["konid"] * 100,2)
df3["no_status"]=round(df3["empty"] / df3["konid"] * 100,2)
df3["judul"]=df3["distrik"].astype(str)+ " : " + df3["konid"].astype(str) + " Dokumen"
df3["Sukses"]= df3["Y"].astype(str)+ " ("+ df3["sukses"].astype(str)+" %)"
df3["Gagal"]= df3["C"].astype(str)+ " ("+ df3["failed"].astype(str)+" %)"
df3["No Status"]= df3["empty"].astype(str)+ " ("+ df3["no_status"].astype(str)+" %)"


n=df3["konid"].sum()
na=jkt['kec'].isna().sum()
all=jkt['konid'].count()


text=df3.apply(lambda row: f"{row['Y']}%<br>{row['C']}", axis=1),
hoverinfo="text"





##----batam-----##

batam=pd.read_excel('data/batam_UOB_sept.xlsx')
batam["join"]=batam["alam5"].astype(str) +" " + batam["alam6"].astype(str)
batam['pod'].fillna("empty",inplace=True)


with open('data/batam_kec.geojson') as h:
      geojson01 = json.load(h)



df_batam = pd.DataFrame(
    {"distrik": pd.json_normalize(geojson01["features"])["properties.WADMKC"]}
).assign(kec=lambda d: d["distrik"].str.upper())


for kec in df_batam['kec'].to_list():
  batam.loc[ batam['join'].str.contains(kec), 'kec'] = kec

p_batam = pd.pivot_table(batam, index= ['kec'],  columns=['pod'], values='konid', aggfunc = 'count' ).fillna(0).reset_index()


#st.table(p_batam)


df2_batam = batam.groupby(['kec'], as_index=False)['konid'].count()
df2a_batam= jkt.groupby(['kec', 'pod'], as_index=False)['konid'].count()
df3_batam = pd.merge(pd.merge(df_batam, df2_batam, on='kec', how='left'), p_batam, on='kec', how='left').reset_index(drop=True)

df3_batam["sukses"]=round(df3_batam["Y"] / df3_batam["konid"] * 100,2)
df3_batam["failed"]=round(df3_batam["C"] / df3_batam["konid"] * 100,2)
df3_batam["no_status"]=round(df3_batam["empty"] / df3_batam["konid"] * 100,2)
df3_batam["judul"]=df3_batam["distrik"].astype(str)+ " : " + df3_batam["konid"].astype(str) + " Dokumen"
df3_batam["Sukses"]= df3_batam["Y"].astype(str)+ " ("+ df3_batam["sukses"].astype(str)+" %)"
df3_batam["Gagal"]= df3_batam["C"].astype(str)+ " ("+ df3_batam["failed"].astype(str)+" %)"
df3_batam["No Status"]= df3_batam["empty"].astype(str)+ " ("+ df3_batam["no_status"].astype(str)+" %)"








with col1:

      fig8 = go.Figure(
    data=go.Choropleth(
      geojson=geojson,
      locations=df3["distrik"], 
      customdata=df3["distrik"],
      text=df3.apply(lambda row: f"""Sukses: {row['Y']} ({row['sukses']}%)
                     <br>Reject: {row['C']} ({row['failed']}%)
                     <br>No Status: {row['empty']} ({row['no_status']}%) """, axis=1),
      featureidkey="properties.WADMKC",
      z=df3["konid"], 
      colorbar_title="<b>Kiriman UOB",
      colorscale='Greens',
      autocolorscale=False,
      name="",
      hoverlabel=dict(bgcolor="white",font_size=14),
      hovertemplate="<b>%{customdata} : %{z} Kiriman</b>" + "<br>%{text} <br>"
          
        
    )#type: ignore
)
      fig8.update_layout( width=700,height=750,  margin=dict(l=1, r=1, t=1, b=1), title= f"""<br>Sebaran Data Dokumen UOB di Kecamatan DKI Jakarta 
                   <br>(n : {n} dari {all} Dokumen) """, autosize=True, 
                 title_y=0.9, title_font_size=22, title_yanchor="top", title_xanchor='left' ,margin_t=50, showlegend=True)
      fig8.update_geos(fitbounds="locations", visible=False) #type: ignore
   

      #st.plotly_chart(fig8, use_container_width=True)


      
      

      fig9 = px.choropleth_mapbox(df3, geojson=geojson,
                                  locations=df3["distrik"],
                     featureidkey="properties.WADMKC",color=df3["konid"],
      color_continuous_scale="Viridis_r",
                           range_color=(0, 1400),
                           mapbox_style="carto-positron",
                           zoom=10, center = {"lat": -6.202905, "lon": 106.778419},
                           opacity=0.5, height=700,
                           hover_name="judul",
                           hover_data = {'konid':False, 'distrik':False, "Sukses": True, "Gagal":True, "No Status":True}
                                    
                          
                     )#type: ignore 
      #fig9.update_traces(hovertemplate="<b> {custom_data} Kiriman</b>")
      
      fig9.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
      fig9.update_layout(
    hoverlabel=dict(
        bgcolor="white",
        font_size=12
    )
)
      
    
      st.subheader("Kiriman UOB Jakarta September 2023 (Update 4 Okt 2023)")
      st.plotly_chart(fig9, use_container_width=True)


      
      figbatam = px.choropleth_mapbox(df3_batam, geojson=geojson01,
                                  locations=df3_batam["distrik"],
                     featureidkey="properties.WADMKC",color=df3_batam["konid"],
      color_continuous_scale="Viridis_r",
                           range_color=(0, 1400),
                           mapbox_style="carto-positron",
                           zoom=10, center = {"lat": 1.054507, "lon": 104.004120},
                           opacity=0.5, height=700,
                           hover_name="judul",
                           hover_data = {'konid':False, 'distrik':False, "Sukses": True, "Gagal":True, "No Status":True}
                                    
                          
                     )#type: ignore 
      #fig9.update_traces(hovertemplate="<b> {custom_data} Kiriman</b>")
      
      figbatam.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
      figbatam.update_layout(
    hoverlabel=dict(
        bgcolor="white",
        font_size=12
    )
)
      
      st.subheader("Kiriman UOB Batam September 2023")

      st.plotly_chart(figbatam, use_container_width=True)

      #st.dataframe(df3_batam)


with col2:
  
  st.header(" ")
  st.header(" ")
  st.text(f"Total Kiriman UOB Jakarta: {all} Dokumen")
  st.markdown(f"**{n}** / **{na}**")
 
