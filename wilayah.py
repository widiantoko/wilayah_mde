import pandas as pd
import streamlit as st
import plotly_express as px
import plotly.graph_objects as go
import json


st.set_page_config(page_title="Kiriman Jakarta", layout='wide')

col1, col2 = st.columns([5,2] ,gap="small")

#jkt=pd.read_excel("data/baru.xlsx")
#jkt=pd.read_excel("data/baru_UOB.xlsx")
jkt=pd.read_csv("data/baru.csv")

jkt["join"]=jkt["alam4"].astype(str) +" "+jkt["alam5"].astype(str) +" "+jkt["alam6"].astype(str)
jkt['join'] = jkt['join'].str.upper() 

jkt['pod'].fillna("empty",inplace=True)

jkt['join'] = jkt['join'].str.replace('  ', ' ')
jkt['join'] = jkt['join'].str.replace('SLTN', 'SELATAN')
jkt['join'] = jkt['join'].str.replace('SLT', 'SELATAN')
jkt['join'] = jkt['join'].str.replace('BRT', 'BARAT')
jkt['join'] = jkt['join'].str.replace('TWR', 'TOWER')
jkt['join'] = jkt['join'].str.replace('BLVD', 'BOULEVARD')
jkt['join'] = jkt['join'].str.replace('TMN', 'TAMAN')
jkt['join'] = jkt['join'].str.replace('BSR', 'BESAR')
jkt['join'] = jkt['join'].str.replace('SWH', 'SAWAH')
jkt['join'] = jkt['join'].str.replace('KB KOSONG', 'KEBON KOSONG')
jkt['join'] = jkt['join'].str.replace('KMYRN', 'KEMAYORAN')
jkt['join'] = jkt['join'].str.replace('KEMOYARAN', 'KEMAYORAN')

jkt['join'] = jkt['join'].str.replace('KV', 'KAV')
jkt['join'] = jkt['join'].str.replace('KAV.', 'KAV')
jkt['join'] = jkt['join'].str.replace('KAVL', 'KAV')
jkt['join'] = jkt['join'].str.replace('KELURAHAN', 'KEL')
jkt['join'] = jkt['join'].str.replace('PNTAI', 'PANTAI')
jkt['join'] = jkt['join'].str.replace('PLZ', 'PLAZA')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN NO KAV', 'SUDIRMAN KAV')
jkt['join'] = jkt['join'].str.replace('MANGGA 2', 'MANGGA DUA')
jkt['join'] = jkt['join'].str.replace('PTMBRN', 'PETAMBURAN')


jkt['join'] = jkt['join'].str.replace('MALL OF INDONESIA', 'KELAPA GADING')
jkt['join'] = jkt['join'].str.replace('MOI', 'KELAPA GADING')
jkt['join'] = jkt['join'].str.replace('PLAZA SUMMARECON', 'PULOGADUNG')

jkt['join'] = jkt['join'].str.replace('PONDOK INDAH OFFICE TOWER', 'KEBAYORAN LAMA')
jkt['join'] = jkt['join'].str.replace('PD INDAH OFFICE TOWER', 'KEBAYORAN LAMA')


jkt['join'] = jkt['join'].str.replace('DUTA MERLIN', 'GAMBIR')

jkt['join'] = jkt['join'].str.replace('GREEN SEDAYU BIZ', 'KALIDERES')

jkt['join'] = jkt['join'].str.replace('HARMONI PLAZA', 'TAMAN SARI')
jkt['join'] = jkt['join'].str.replace('PINTU BESAR SELATAN', 'TAMAN SARI')
jkt['join'] = jkt['join'].str.replace('PINTU BESAR', 'TAMAN SARI')

jkt['join'] = jkt['join'].str.replace('HARCO MANGGA DUA', 'SAWAH BESAR')
jkt['join'] = jkt['join'].str.replace('WISMA 46', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('WISMA MANDIRI', 'MENTENG')

jkt['join'] = jkt['join'].str.replace('GLODOK PLAZA', 'MANGGA BESAR')
jkt['join'] = jkt['join'].str.replace('HARMONI PLAZA', 'TAMAN SARI')
jkt['join'] = jkt['join'].str.replace('PLAZA ATRIUM', 'SENEN')
jkt['join'] = jkt['join'].str.replace('ATRIUM PLAZA', 'SENEN')
jkt['join'] = jkt['join'].str.replace('WISMA KEIAI', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('WISMA GKBI', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('CHASE PLAZA', 'SETIABUDI')
jkt['join'] = jkt['join'].str.replace('MENARA BATAVIA', 'SETIABUDI')
jkt['join'] = jkt['join'].str.replace('MANGGALA WANABAKTI', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('DIPO TOWER', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('BATAVIA TOWER', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN PARK', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('MIDPLAZA', 'TANAH ABANG')

jkt['join'] = jkt['join'].str.replace('SAMPOERNA STRATEGIC', 'SETIA BUDI')
jkt['join'] = jkt['join'].str.replace('ROXY', 'GAMBIR')
jkt['join'] = jkt['join'].str.replace('ROXY MAS', 'GAMBIR')
jkt['join'] = jkt['join'].str.replace('ROXI MAS', 'GAMBIR')
jkt['join'] = jkt['join'].str.replace('GEDUNG ALIA', 'GAMBIR')
jkt['join'] = jkt['join'].str.replace('ISTANA HARMONI', 'GAMBIR')
jkt['join'] = jkt['join'].str.replace('ALIA BUILDING', 'GAMBIR')
jkt['join'] = jkt['join'].str.replace('WISMA CORMIC', 'GAMBIR')
jkt['join'] = jkt['join'].str.replace('IBIS JAKARTA HARMONI', 'GAMBIR')
jkt['join'] = jkt['join'].str.replace('SUPERMARKET REZEKI HAYAM WURUK', 'GAMBIR')
jkt['join'] = jkt['join'].str.replace('WISMA HAYAM WURUK', 'GAMBIR')
jkt['join'] = jkt['join'].str.replace('WISMA INDOMOBIL', 'JATINEGARA')
jkt['join'] = jkt['join'].str.replace('WISMA 77', 'PAL MERAH')
jkt['join'] = jkt['join'].str.replace('WISMA RAHARJA', 'CILANDAK')
jkt['join'] = jkt['join'].str.replace('SEASONS CITY', 'TAMBORA')
jkt['join'] = jkt['join'].str.replace('SEASON CITY', 'TAMBORA')
jkt['join'] = jkt['join'].str.replace('CITILOFTS', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('TAMAN PALEM', 'CENGKARENG')
jkt['join'] = jkt['join'].str.replace('CIPUTRA INTERNATIONAL', 'CENGKARENG')
jkt['join'] = jkt['join'].str.replace('PURI INDAH', 'KEMBANGAN')

jkt['join'] = jkt['join'].str.replace('RUKO HARMONI MAS', 'PENJARINGAN')
jkt['join'] = jkt['join'].str.replace('RUKO GLODOK', 'MANGGA BESAR')
jkt['join'] = jkt['join'].str.replace('RUKO GREEN GARDEN', 'KEBON JERUK')
jkt['join'] = jkt['join'].str.replace('RUKAN GREEN GARDEN', 'KEBON JERUK')
jkt['join'] = jkt['join'].str.replace('GREEN VILLE', 'KEBON JERUK')
jkt['join'] = jkt['join'].str.replace('GREENVILLE', 'KEBON JERUK')
jkt['join'] = jkt['join'].str.replace('PALM CROWN', 'KALIDERES')
jkt['join'] = jkt['join'].str.replace('RUKO IMPERIAL BUSINESS', 'KALIDERES')
jkt['join'] = jkt['join'].str.replace('CITRA GARDEN', 'KALIDERES')

jkt['join'] = jkt['join'].str.replace('RUKO KETAPANG INDAH', 'GAMBIR')
jkt['join'] = jkt['join'].str.replace('RUKO CEMPAKA INDAH', 'CEMPAKA PUTIH')


jkt['join'] = jkt['join'].str.replace('PALMERAH', 'PAL MERAH')
jkt['join'] = jkt['join'].str.replace('PALMERA H', 'PAL MERAH')
jkt['join'] = jkt['join'].str.replace('SLIPI', 'PAL MERAH')
jkt['join'] = jkt['join'].str.replace('KEMANGGISAN', 'PAL MERAH')


jkt['join'] = jkt['join'].str.replace('KEBUN JERUK', 'KEBON JERUK')
jkt['join'] = jkt['join'].str.replace('KEBONJERUK', 'KEBON JERUK')
jkt['join'] = jkt['join'].str.replace('KBN JERUK', 'KEBON JERUK')
jkt['join'] = jkt['join'].str.replace('KBN JRK', 'KEBON JERUK')
jkt['join'] = jkt['join'].str.replace('KBJERUK', 'KEBON JERUK')
jkt['join'] = jkt['join'].str.replace('JRK', 'JERUK')
jkt['join'] = jkt['join'].str.replace('KB JERUK', 'KEBON JERUK')
jkt['join'] = jkt['join'].str.replace('KEDOYA', 'KEBON JERUK')
jkt['join'] = jkt['join'].str.replace('KLP DUA RAYA', 'KEBON JERUK')
jkt['join'] = jkt['join'].str.replace('DURI KEPA', 'KEBON JERUK')
jkt['join'] = jkt['join'].str.replace('KEL KELAPA DUA', 'KEBON JERUK')
jkt['join'] = jkt['join'].str.replace('SUKABUMI UTARA', 'KEBON JERUK')


jkt['join'] = jkt['join'].str.replace('TG PRIOK',  'TANJUNG PRIOK')
jkt['join'] = jkt['join'].str.replace('TJ PRIOK', 'TANJUNG PRIOK')
jkt['join'] = jkt['join'].str.replace('SUNTER AGUNG', 'TANJUNG PRIOK')
jkt['join'] = jkt['join'].str.replace('SUNTER JAYA', 'TANJUNG PRIOK')
jkt['join'] = jkt['join'].str.replace('SUNTER', 'TANJUNG PRIOK')

jkt['join'] = jkt['join'].str.replace('DURI PULO', 'GAMBIR')
jkt['join'] = jkt['join'].str.replace('PETOJO', 'GAMBIR')
jkt['join'] = jkt['join'].str.replace('GAJAH MADA', 'GAMBIR')
jkt['join'] = jkt['join'].str.replace('CIDENG', 'GAMBIR')
jkt['join'] = jkt['join'].str.replace('BALIK PAPAN', 'GAMBIR')
jkt['join'] = jkt['join'].str.replace('GAMBI R', 'GAMBIR')

jkt['join'] = jkt['join'].str.replace('BALIKPAPAN', 'GAMBIR')
jkt['join'] = jkt['join'].str.replace('PECENONGAN', 'GAMBIR')
jkt['join'] = jkt['join'].str.replace('MEDAN MERDEKA', 'GAMBIR')

jkt['join'] = jkt['join'].str.replace('KLP GADING', 'KELAPA GADING')
jkt['join'] = jkt['join'].str.replace('KLP GDNG', 'KELAPA GADING')
jkt['join'] = jkt['join'].str.replace('KLP GDG', 'KELAPA GADING')
jkt['join'] = jkt['join'].str.replace('BUKIT GADING', 'KELAPA GADING')
jkt['join'] = jkt['join'].str.replace('ARTHA GADING', 'KELAPA GADING')
jkt['join'] = jkt['join'].str.replace('VILLA GADING', 'KELAPA GADING')
jkt['join'] = jkt['join'].str.replace('GADING INDAH', 'KELAPA GADING')

jkt['join'] = jkt['join'].str.replace('BANDENGAN UTARA', 'TAMBORA')
jkt['join'] = jkt['join'].str.replace('DURI SELATAN', 'TAMBORA')
jkt['join'] = jkt['join'].str.replace('JEMBATAN LIMA', 'TAMBORA')
jkt['join'] = jkt['join'].str.replace('ROA MALAKA', 'TAMBORA')

jkt['join'] = jkt['join'].str.replace('HALIM PERDANA KUSUMA', 'MAKASAR')
jkt['join'] = jkt['join'].str.replace('HALIM PERDANAKUSUMA', 'MAKASAR')
jkt['join'] = jkt['join'].str.replace('MAKASSAR', 'MAKASAR')


jkt['join'] = jkt['join'].str.replace('KBYRN', 'KEBAYORAN')
jkt['join'] = jkt['join'].str.replace('KBY', 'KEBAYORAN')
jkt['join'] = jkt['join'].str.replace('KABAYORAN', 'KEBAYORAN')
jkt['join'] = jkt['join'].str.replace('KEB LAMA', 'KEBAYORAN LAMA')
jkt['join'] = jkt['join'].str.replace('PONDOK INDAH', 'KEBAYORAN LAMA')
jkt['join'] = jkt['join'].str.replace('PONDOK PINANG', 'KEBAYORAN LAMA')
jkt['join'] = jkt['join'].str.replace('GANDARIA', 'KEBAYORAN LAMA')
jkt['join'] = jkt['join'].str.replace('PERMATA HIJAU', 'KEBAYORAN LAMA')
jkt['join'] = jkt['join'].str.replace('SIMPRUG', 'KEBAYORAN LAMA')
jkt['join'] = jkt['join'].str.replace('GROGOL SELATAN', 'KEBAYORAN LAMA')
jkt['join'] = jkt['join'].str.replace('KEB BARU', 'KEBAYORAN BARU')
jkt['join'] = jkt['join'].str.replace('PAKUBUWONO', 'KEBAYORAN BARU')
jkt['join'] = jkt['join'].str.replace('SENAYAN', 'KEBAYORAN BARU')

jkt['join'] = jkt['join'].str.replace('SAWAHBESAR', 'SAWAH BESAR')
jkt['join'] = jkt['join'].str.replace('MANGGA DUA', 'SAWAH BESAR')
jkt['join'] = jkt['join'].str.replace('MANGGA II', 'SAWAH BESAR')
jkt['join'] = jkt['join'].str.replace('PASAR BARU', 'SAWAH BESAR')
jkt['join'] = jkt['join'].str.replace('JAYAKARTA', 'SAWAH BESAR')
jkt['join'] = jkt['join'].str.replace('LAP BANTENG', 'SAWAH BESAR')
jkt['join'] = jkt['join'].str.replace('LAPANGAN BANTENG', 'SAWAH BESAR')
jkt['join'] = jkt['join'].str.replace('KARANG ANYAR', 'SAWAH BESAR')
jkt['join'] = jkt['join'].str.replace('KARANGANYAR', 'SAWAH BESAR')
jkt['join'] = jkt['join'].str.replace('KEL KARTINI', 'SAWAH BESAR')
jkt['join'] = jkt['join'].str.replace('KEL.KARTINI', 'SAWAH BESAR')


jkt['join'] = jkt['join'].str.replace('BUNGUR BESAR', 'SENEN')
jkt['join'] = jkt['join'].str.replace('PASEBAN', 'SENEN')

jkt['join'] = jkt['join'].str.replace('KEL PETAMBURAN', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('BENDUNGAN HILIR', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('KEBON KACANG', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('TN ABANG', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('TNABANG', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('TNABG', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('TNH ABANG', 'TANAH ABANG')


jkt['join'] = jkt['join'].str.replace('KARET', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('KEBON MELATI', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('PEJOMPONGAN', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('BENHIL', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('BENHILL', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('PENJERNIHAN', 'TANAH ABANG')

jkt['join'] = jkt['join'].str.replace('GONDANGDIA', 'MENTENG')
jkt['join'] = jkt['join'].str.replace('MANGGA BESAR', 'TAMAN SARI')

jkt['join'] = jkt['join'].str.replace('PONDOK KELAPA', 'DUREN SAWIT')
jkt['join'] = jkt['join'].str.replace('PONDOK BAMBU', 'DUREN SAWIT')
jkt['join'] = jkt['join'].str.replace('PONDOK KOPI', 'DUREN SAWIT')
jkt['join'] = jkt['join'].str.replace('DURENSAWIT', 'DUREN SAWIT')

jkt['join'] = jkt['join'].str.replace('PEGADUNGAN', 'KALIDERES')
jkt['join'] = jkt['join'].str.replace('SEMANAN', 'KALIDERES')
jkt['join'] = jkt['join'].str.replace('TEGAL ALUR', 'KALIDERES')

jkt['join'] = jkt['join'].str.replace('BINTARO', 'PESANGGRAHAN')
jkt['join'] = jkt['join'].str.replace('PSGGRAHAN', 'PESANGGRAHAN')

jkt['join'] = jkt['join'].str.replace('KEDAUNG', 'CENGKARENG')
jkt['join'] = jkt['join'].str.replace('RAWA BUAYA', 'CENGKARENG')

jkt['join'] = jkt['join'].str.replace('WIJAYA KUSUMA', 'GROGOL PETAMBURAN')
jkt['join'] = jkt['join'].str.replace('GROGOL', 'GROGOL PETAMBURAN')
jkt['join'] = jkt['join'].str.replace('TANJUNG DUREN', 'GROGOL PETAMBURAN')
jkt['join'] = jkt['join'].str.replace('LATUMENTEN', 'GROGOL PETAMBURAN')
jkt['join'] = jkt['join'].str.replace('JELAMBAR', 'GROGOL PETAMBURAN')
jkt['join'] = jkt['join'].str.replace('PARMAN', 'GROGOL PETAMBURAN')
jkt['join'] = jkt['join'].str.replace('TOMANG', 'GROGOL PETAMBURAN')
jkt['join'] = jkt['join'].str.replace('GRGL PTMBRN', 'GROGOL PETAMBURAN')
jkt['join'] = jkt['join'].str.replace('GRGLPTMBRN', 'GROGOL PETAMBURAN')

jkt['join'] = jkt['join'].str.replace('CEMPAKA BARU', 'KEMAYORAN')
jkt['join'] = jkt['join'].str.replace('KEBON KOSONG', 'KEMAYORAN')
jkt['join'] = jkt['join'].str.replace('HARAPAN MULIA', 'KEMAYORAN')
jkt['join'] = jkt['join'].str.replace('SAHARI', 'KEMAYORAN')

jkt['join'] = jkt['join'].str.replace('KEL KRAMAT', 'SENEN')
jkt['join'] = jkt['join'].str.replace('KEL KWITANG', 'SENEN')

jkt['join'] = jkt['join'].str.replace('SETIA BUDI', 'SETIABUDI')
jkt['join'] = jkt['join'].str.replace('STIABDI', 'SETIABUDI')
jkt['join'] = jkt['join'].str.replace('STIABUDI', 'SETIABUDI')

jkt['join'] = jkt['join'].str.replace('PULO GADUNG', 'PULOGADUNG')
jkt['join'] = jkt['join'].str.replace('KEL JATI', 'PULOGADUNG')
jkt['join'] = jkt['join'].str.replace('P GADUNG', 'PULOGADUNG')
jkt['join'] = jkt['join'].str.replace('CIPINANG', 'PULOGADUNG')
jkt['join'] = jkt['join'].str.replace('RAWAMANGUN', 'PULOGADUNG')
jkt['join'] = jkt['join'].str.replace('KAYU PUTIH', 'PULOGADUNG')
jkt['join'] = jkt['join'].str.replace('PULOMAS', 'PULOGADUNG')
jkt['join'] = jkt['join'].str.replace('PULO LENTUT', 'PULOGADUNG')

jkt['join'] = jkt['join'].str.replace('GEDONG', 'PASAR REBO')
jkt['join'] = jkt['join'].str.replace('CILILITAN', 'KRAMATJATI')
jkt['join'] = jkt['join'].str.replace('KEBON SIRIH', 'MENTENG')
jkt['join'] = jkt['join'].str.replace('PEGANGSAAN', 'MENTENG')


jkt['join'] = jkt['join'].str.replace('CEMPAKAPUTIH', 'CEMPAKA PUTIH')
jkt['join'] = jkt['join'].str.replace('CEMP PUTIH', 'CEMPAKA PUTIH')
jkt['join'] = jkt['join'].str.replace('RAWASARI', 'CEMPAKA PUTIH')
jkt['join'] = jkt['join'].str.replace('RAWA SARI', 'CEMPAKA PUTIH')

jkt['join'] = jkt['join'].str.replace('BANDENGAN SELATAN', 'PENJARINGAN')
jkt['join'] = jkt['join'].str.replace('PANTAI INDAH KAPUK', 'PENJARINGAN')
jkt['join'] = jkt['join'].str.replace('PIK', 'PENJARINGAN')
jkt['join'] = jkt['join'].str.replace('KAMAL MUARA', 'PENJARINGAN')
jkt['join'] = jkt['join'].str.replace('KAPUK MUARA', 'PENJARINGAN')
jkt['join'] = jkt['join'].str.replace('PLUIT', 'PENJARINGAN')
jkt['join'] = jkt['join'].str.replace('MUARA KARANG', 'PENJARINGAN')
jkt['join'] = jkt['join'].str.replace('PEJAGALAN', 'PENJARINGAN')
jkt['join'] = jkt['join'].str.replace('PANTAI MUTIARA', 'PENJARINGAN')
jkt['join'] = jkt['join'].str.replace('KAPUK', 'PENJARINGAN')
jkt['join'] = jkt['join'].str.replace('JEMBATAN TIGA', 'PENJARINGAN')

jkt['join'] = jkt['join'].str.replace('JOGLO', 'KEMBANGAN')
jkt['join'] = jkt['join'].str.replace('MERUYA', 'KEMBANGAN')
jkt['join'] = jkt['join'].str.replace('SRENGSENG', 'KEMBANGAN')
jkt['join'] = jkt['join'].str.replace('KMBNGAN', 'KEMBANGAN')

jkt['join'] = jkt['join'].str.replace('KALI DERES', 'KALIDERES')

jkt['join'] = jkt['join'].str.replace('KRAMAT JATI', 'KRAMATJATI')

jkt['join'] = jkt['join'].str.replace('DURI KOSAMBI', 'CENGKARENG')
jkt['join'] = jkt['join'].str.replace('KAMAL RAYA', 'CENGKARENG')
jkt['join'] = jkt['join'].str.replace('RAYA KAMAL', 'CENGKARENG')
jkt['join'] = jkt['join'].str.replace('DURI RAYA KOSAMBI', 'CENGKARENG')
jkt['join'] = jkt['join'].str.replace('CGKRENG', 'CENGKARENG')


jkt['join'] = jkt['join'].str.replace('PANCORA', 'PANCORAN')

jkt['join'] = jkt['join'].str.replace('ANCOL', 'PADEMANGAN')
jkt['join'] = jkt['join'].str.replace('BANGKA', 'MAMPANG PRAPATAN')
jkt['join'] = jkt['join'].str.replace('PS MINGGU', 'PASAR MINGGU')
jkt['join'] = jkt['join'].str.replace('PS MINGG U', 'PASAR MINGGU')
jkt['join'] = jkt['join'].str.replace('PEJATEN BARAT', 'PASAR MINGGU')

jkt['join'] = jkt['join'].str.replace('TAMANSARI', 'TAMAN SARI')
jkt['join'] = jkt['join'].str.replace('GLODOK', 'TAMAN SARI')
jkt['join'] = jkt['join'].str.replace('LINDETEVES', 'TAMAN SARI')

jkt['join'] = jkt['join'].str.replace('SALEMBA', 'SENEN')
jkt['join'] = jkt['join'].str.replace('SEMANGGI', 'SETIABUDI')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 1', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 01', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 3', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 7', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 10', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 22', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 32', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 33', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('SUDIRMANKAV 33', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 34', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 44', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN BLK KAV45', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 45', 'TANAH ABANG')

jkt['join'] = jkt['join'].str.replace('SAHID', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV52', 'KEBAYORAN BARU')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV59', 'KEBAYORAN BARU')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 52', 'KEBAYORAN BARU')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 53', 'KEBAYORAN BARU')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 54', 'KEBAYORAN BARU')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 55', 'KEBAYORAN BARU')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 57', 'KEBAYORAN BARU')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 58', 'KEBAYORAN BARU')

jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 59', 'KEBAYORAN BARU')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 60', 'KEBAYORAN BARU')
jkt['join'] = jkt['join'].str.replace('SCBD', 'KEBAYORAN BARU')

jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 70', 'SETIABUDI')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 76', 'SETIABUDI')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 79', 'SETIABUDI')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 50', 'SETIABUDI')

jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 45', 'SETIABUDI')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 9', 'SETIABUDI')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 25', 'SETIABUDI')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 29', 'SETIABUDI')
jkt['join'] = jkt['join'].str.replace('SUDIRMAN KAV 21', 'SETIABUDI')
jkt['join'] = jkt['join'].str.replace('SUBROTO KAV 24', 'SETIABUDI')
jkt['join'] = jkt['join'].str.replace('SUBROTO KAV 34', 'SETIABUDI')
jkt['join'] = jkt['join'].str.replace('SUBROTO KAV 35', 'SETIABUDI')
jkt['join'] = jkt['join'].str.replace('SUBROTO KAV 37', 'SETIABUDI')
jkt['join'] = jkt['join'].str.replace('RASUNA SAID', 'SETIABUDI')
jkt['join'] = jkt['join'].str.replace('KUNINGAN', 'SETIABUDI')

jkt['join'] = jkt['join'].str.replace('THAMRIN', 'MENTENG')

jkt['join'] = jkt['join'].str.replace('CEMPAKA MAS', 'CEMPAKA PUTIH')
jkt['join'] = jkt['join'].str.replace('IMAM BONJOL', 'MENTENG')

jkt['join'] = jkt['join'].str.replace('LEBAK BULUS', 'CILANDAK')
jkt['join'] = jkt['join'].str.replace('PONDOK LABU', 'CILANDAK')
jkt['join'] = jkt['join'].str.replace('CILANDA K', 'CILANDAK')

jkt['join'] = jkt['join'].str.replace('CASABLANCA', 'TEBET')


jkt['join'] = jkt['join'].str.replace('CIPINANG MUARA', 'JATINEGARA')
jkt['join'] = jkt['join'].str.replace('DI PANJAITAN', 'JATINEGARA')
jkt['join'] = jkt['join'].str.replace('RAWA BUNGA', 'JATINEGARA')
jkt['join'] = jkt['join'].str.replace('TANJUNG BARAT', 'JAGAKARSA')
jkt['join'] = jkt['join'].str.replace('KOTA WISATA CIBUBUR', 'CIRACAS')

jkt['join'] = jkt['join'].str.replace('11450', 'GROGOL PETAMBURAN')
jkt['join'] = jkt['join'].str.replace('11460', 'GROGOL PETAMBURAN')
jkt['join'] = jkt['join'].str.replace('11470', 'GROGOL PETAMBURAN')
jkt['join'] = jkt['join'].str.replace('11480', 'GROGOL PETAMBURAN')
jkt['join'] = jkt['join'].str.replace('11490', 'GROGOL PETAMBURAN')

jkt['join'] = jkt['join'].str.replace('11110', 'TAMAN SARI')
jkt['join'] = jkt['join'].str.replace('11120', 'TAMAN SARI')
jkt['join'] = jkt['join'].str.replace('11130', 'TAMAN SARI')
jkt['join'] = jkt['join'].str.replace('11140', 'TAMAN SARI')
jkt['join'] = jkt['join'].str.replace('11150', 'TAMAN SARI')
jkt['join'] = jkt['join'].str.replace('11160', 'TAMAN SARI')
jkt['join'] = jkt['join'].str.replace('11170', 'TAMAN SARI')
jkt['join'] = jkt['join'].str.replace('11180', 'TAMAN SARI')


jkt['join'] = jkt['join'].str.replace('11410', 'PAL MERAH')
jkt['join'] = jkt['join'].str.replace('11420', 'PAL MERAH')
jkt['join'] = jkt['join'].str.replace('11430', 'PAL MERAH')
jkt['join'] = jkt['join'].str.replace('11440', 'PAL MERAH')


jkt['join'] = jkt['join'].str.replace('14430', 'PADEMANGAN')
jkt['join'] = jkt['join'].str.replace('14440', 'PENJARINGAN')
jkt['join'] = jkt['join'].str.replace('14450', 'PENJARINGAN')
jkt['join'] = jkt['join'].str.replace('14460', 'PENJARINGAN')
jkt['join'] = jkt['join'].str.replace('14470', 'PENJARINGAN')

jkt['join'] = jkt['join'].str.replace('10710', 'SAWAH BESAR')

jkt['join'] = jkt['join'].str.replace('11210', 'TAMBORA')
jkt['join'] = jkt['join'].str.replace('11220', 'TAMBORA')
jkt['join'] = jkt['join'].str.replace('11230', 'TAMBORA')
jkt['join'] = jkt['join'].str.replace('11240', 'TAMBORA')
jkt['join'] = jkt['join'].str.replace('11250', 'TAMBORA')
jkt['join'] = jkt['join'].str.replace('11260', 'TAMBORA')
jkt['join'] = jkt['join'].str.replace('11270', 'TAMBORA')

jkt['join'] = jkt['join'].str.replace('11330', 'TAMBORA')

jkt['join'] = jkt['join'].str.replace('13230', 'PULOGADUNG')
jkt['join'] = jkt['join'].str.replace('13220', 'PULOGADUNG')

jkt['join'] = jkt['join'].str.replace('13420', 'JATINEGARA')

jkt['join'] = jkt['join'].str.replace('13430', 'DUREN SAWIT')
jkt['join'] = jkt['join'].str.replace('13450', 'DUREN SAWIT')

jkt['join'] = jkt['join'].str.replace('10750', 'SAWAH BESAR')
jkt['join'] = jkt['join'].str.replace('10730', 'SAWAH BESAR')

jkt['join'] = jkt['join'].str.replace('10130', 'GAMBIR')
jkt['join'] = jkt['join'].str.replace('10140', 'GAMBIR')
jkt['join'] = jkt['join'].str.replace('10150', 'GAMBIR')

jkt['join'] = jkt['join'].str.replace('10610', 'KEMAYORAN')
jkt['join'] = jkt['join'].str.replace('10620', 'KEMAYORAN')
jkt['join'] = jkt['join'].str.replace('10630', 'KEMAYORAN')
jkt['join'] = jkt['join'].str.replace('10640', 'KEMAYORAN')

jkt['join'] = jkt['join'].str.replace('14240', 'KELAPA GADING')


jkt['join'] = jkt['join'].str.replace('14350', 'TANJUNG PRIOK')

jkt['join'] = jkt['join'].str.replace('11510', 'KEBON JERUK')
jkt['join'] = jkt['join'].str.replace('11520', 'KEBON JERUK')
jkt['join'] = jkt['join'].str.replace('11530', 'KEBON JERUK')
jkt['join'] = jkt['join'].str.replace('11540', 'KEBON JERUK')
jkt['join'] = jkt['join'].str.replace('11550', 'KEBON JERUK')

jkt['join'] = jkt['join'].str.replace('10120', 'GAMBIR')
jkt['join'] = jkt['join'].str.replace('10130', 'GAMBIR')
jkt['join'] = jkt['join'].str.replace('10140', 'GAMBIR')
jkt['join'] = jkt['join'].str.replace('10150', 'GAMBIR')
jkt['join'] = jkt['join'].str.replace('10160', 'GAMBIR')

jkt['join'] = jkt['join'].str.replace('10210', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('10220', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('10230', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('10240', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('10250', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('10260', 'TANAH ABANG')
jkt['join'] = jkt['join'].str.replace('10270', 'TANAH ABANG')


jkt['join'] = jkt['join'].str.replace('10310', 'MENTENG')
jkt['join'] = jkt['join'].str.replace('10320', 'MENTENG')
jkt['join'] = jkt['join'].str.replace('10330', 'MENTENG')
jkt['join'] = jkt['join'].str.replace('10340', 'MENTENG')
jkt['join'] = jkt['join'].str.replace('10350', 'MENTENG')


jkt['join'] = jkt['join'].str.replace('10420', 'SENEN')
jkt['join'] = jkt['join'].str.replace('10430', 'SENEN')
jkt['join'] = jkt['join'].str.replace('10440', 'SENEN')
jkt['join'] = jkt['join'].str.replace('10450', 'SENEN')
jkt['join'] = jkt['join'].str.replace('10460', 'SENEN')


jkt['join'] = jkt['join'].str.replace('10540', 'JOHAR BARU')
jkt['join'] = jkt['join'].str.replace('10550', 'JOHAR BARU')
jkt['join'] = jkt['join'].str.replace('10560', 'JOHAR BARU')


jkt['join'] = jkt['join'].str.replace('11810', 'KALIDERES')
jkt['join'] = jkt['join'].str.replace('11820', 'KALIDERES')
jkt['join'] = jkt['join'].str.replace('11830', 'KALIDERES')
jkt['join'] = jkt['join'].str.replace('11840', 'KALIDERES')
jkt['join'] = jkt['join'].str.replace('11850', 'KALIDERES')

jkt['join'] = jkt['join'].str.replace('11610', 'KEMBANGAN')
jkt['join'] = jkt['join'].str.replace('11620', 'KEMBANGAN')
jkt['join'] = jkt['join'].str.replace('11630', 'KEMBANGAN')
jkt['join'] = jkt['join'].str.replace('11640', 'KEMBANGAN')
jkt['join'] = jkt['join'].str.replace('11650', 'KEMBANGAN')


jkt['join'] = jkt['join'].str.replace('11710', 'CENGKARENG')
jkt['join'] = jkt['join'].str.replace('11720', 'CENGKARENG')
jkt['join'] = jkt['join'].str.replace('11730', 'CENGKARENG')
jkt['join'] = jkt['join'].str.replace('11740', 'CENGKARENG')
jkt['join'] = jkt['join'].str.replace('11750', 'CENGKARENG')



with open('data/new_jakarta.geojson') as f:
      geojson = json.load(f)


df = pd.DataFrame(
    {"distrik": pd.json_normalize(geojson["features"])["properties.WADMKC"]}
).assign(kec=lambda d: d["distrik"].str.upper())


for kec in df['kec'].to_list():
  jkt.loc[ jkt['join'].str.contains(kec), 'kec'] = kec

bulan=jkt['bulan'].drop_duplicates().reset_index(drop=True).sort_index(ascending=True)
pilihan=st.radio("Pilih Bulan:", key="visibility", options= bulan, label_visibility= "collapsed",horizontal=True)
data_hasil= jkt[(jkt['bulan'] == pilihan)]

new = data_hasil[data_hasil['pod'].isin(['C','Y'])]
new_1= p_table = pd.pivot_table(new, index= ['kec'],  columns=['pod'], values='konid', aggfunc = 'count' ).fillna(0).reset_index()
new_2=data_hasil.groupby(['kec'], as_index=False)['konid'].count()
new_3=pd.merge(new_2, new_1, on='kec', how='left').reset_index(drop=True)
new_3["empty"]=new_3["konid"]-new_3["Y"]-new_3["C"]

df3=pd.merge(df, new_3, on='kec', how='left').reset_index(drop=True)



#kec_none=jkt.loc[jkt['kec'].isnull()].sort_values(by=['kab'], ascending=False)
#kec_pilih=jkt[(jkt['join'].str.contains("GD PELURU",  na = False, case=False)) & (jkt['kec'].isnull())]
kec_pilih=jkt[(jkt['join'].str.contains("SUDIRMAN",  na = False, case=False)) & (jkt['kec'].isnull())]
#kec_pilih=data_hasil[(data_hasil['kec'].isnull())]

st.dataframe(kec_pilih)

#p_table_hsl = pd.pivot_table(new, index= ['kec'],  columns=['pod'], values='konid', aggfunc = 'count' ).fillna(0).reset_index()
#p_table = pd.pivot_table(jkt, index= ['kec'],  columns=['pod'], values='konid', aggfunc = 'count' ).fillna(0).reset_index()


#df2 = jkt.groupby(['kec'], as_index=False)['konid'].count()
#df2a= jkt.groupby(['kec', 'pod'], as_index=False)['konid'].count()
#df3 = pd.merge(pd.merge(df, df2, on='kec', how='left'), p_table, on='kec', how='left').reset_index(drop=True)


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





with col1:

      fig9 = px.choropleth_mapbox(df3, geojson=geojson,
                                  locations=df3["distrik"],featureidkey="properties.WADMKC",
                                  color=df3["konid"],color_continuous_scale="Viridis_r",
                           range_color=(0, 1300),
                           mapbox_style="carto-positron",
                           zoom=10, center = {"lat": -6.202905, "lon": 106.778419},
                           opacity=0.7, height=600,
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
      
    
      st.subheader("Sebaran Kiriman Per Kecamatan di Jakarta Per Bulan")
      st.plotly_chart(fig9, use_container_width=True)


      
      
with col2:
  
  st.header(" ")
  st.header(" ")
  st.text(f"Jumlah Kiriman UOB {pilihan} : {all} Dokumen")
  st.markdown(f"**{n}** / **{na}**")
  st.markdown(f"**{pod_Y}** / **{pod_C}** / **{pod_empty}**")
 
 
 