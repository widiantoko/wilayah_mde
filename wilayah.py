import pandas as pd
import streamlit as st
import plotly
import plotly_express
import plotly.graph_objects as go
import json


st.set_page_config(page_title="Sebaran KirimanJakarta", layout='wide')

col1, col2 = st.columns([5,1] ,gap="small")

jkt=pd.read_excel("data/uob_jkt_07sept.xlsx")
jkt["join"]=jkt["alam5"].astype(str) +" " + jkt["alam6"].astype(str)
jkt['pod'].fillna("empty",inplace=True)


with open('data/new_jakarta.geojson') as f:
      geojson = json.load(f)



df = pd.DataFrame(
    {"distrik": pd.json_normalize(geojson["features"])["properties.WADMKC"]}
).assign(kec=lambda d: d["distrik"].str.upper())



for kec in df['kec'].to_list():
  jkt.loc[ jkt['join'].str.contains(kec), 'kec'] = kec

p_table = pd.pivot_table(jkt, index= ['kec'],  columns=['pod'], values='konid', aggfunc = 'count' ).fillna(0).reset_index()

df2 = jkt.groupby(['kec'], as_index=False)['konid'].count()
df2a= jkt.groupby(['kec', 'pod'], as_index=False)['konid'].count()
df3 = pd.merge(pd.merge(df, df2, on='kec', how='left'), p_table, on='kec', how='left').reset_index(drop=True)



n=df3["konid"].sum()
na=jkt['kec'].isna().sum()
all=jkt['konid'].count()



text=df3.apply(lambda row: f"{row['Y']}%<br>{row['C']}", axis=1),
hoverinfo="text"



with col1:

      fig8 = go.Figure(
    data=go.Choropleth(
      geojson=geojson,
      locations=df3["distrik"], 
      customdata=df3["distrik"],
      text=df3.apply(lambda row: f"Sukses: {row['Y']}<br>Reject: {row['C']}<br>No Status: {row['empty']}", axis=1),
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

      st.plotly_chart(fig8, use_container_width=True)


#st.dataframe(df3)

#st.text(n)
#with col2:
     
     #st.text(all)
     #st.text(n)
     #st.text(na)
     