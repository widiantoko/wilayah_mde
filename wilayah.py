import pandas as pd
import streamlit as st
import plotly
import plotly_express as px
import plotly.graph_objects as go
import json


st.set_page_config(page_title="Sebaran Kiriman Jakarta", layout='wide')

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

df3["sukses"]=round(df3["Y"] / df3["konid"] * 100,2)
df3["failed"]=round(df3["C"] / df3["konid"] * 100,2)
df3["no_status"]=round(df3["empty"] / df3["konid"] * 100,2)

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

      st.plotly_chart(fig8, use_container_width=True)


#st.dataframe(df3)

#st.text(n)
#with col2:
     
     #st.text(all)
     #st.text(n)
     #st.text(na)
     
      


      #token = open(".mapbox_token").read()




      #token=pk.eyJ1Ijoid2lkaWFudG9rbyIsImEiOiJjbG1rM254a3EwOXRyMmlvb3QwZzJqZmJnIn0.pOxdoUDqgaSkFE5r52IZNw

      
      

      fig9 = px.choropleth_mapbox(df3, geojson=geojson,
                                  locations=df3["distrik"],
                     featureidkey="properties.WADMKC",color=df3["konid"],
      color_continuous_scale="Viridis_r",
                           range_color=(0, 2000),
                           mapbox_style="carto-positron",
                           zoom=10, center = {"lat": -6.202905, "lon": 106.778419},
                           opacity=0.5, height=700,
                           hover_name="distrik", text='sukses'
                           hover_data = {'distrik':False}
                     
                    
                           
                          
                     )#type: ignore 
      #fig9.update_traces(hovertemplate="<b> {custom_data} Kiriman</b>")
      
      fig9.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
      
    

      st.plotly_chart(fig9, use_container_width=True)


      fig7 = go.Figure(go.Choroplethmapbox(geojson=geojson, 
                                    locations=df3.distrik, z=df3.konid, marker_opacity=0.5,
                                    colorscale="Viridis", marker_line_width=.5))

      fig7.update_layout(mapbox_style="carto-positron",
              
                        height = 600,
                        autosize=True,
                        margin={"r":0,"t":0,"l":0,"b":0}, mapbox_center = {"lat":-6.202905, "lon": 106.778419},
                        mapbox_zoom=8,
                        )


      #st.plotly_chart(fig7, use_container_width=True)
      #st.dataframe(df3)
      


