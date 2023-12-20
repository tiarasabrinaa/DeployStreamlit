import streamlit as st

st.title("Ini Title")
st.text("1234241")
nama = st.text_input("Nama", "Nama anda")
nim = st.text_input("NIM", "10 digit")
alamat = st.text_input("Alamat", "Jl.")

if nama:
    st.text("Nama : "+nama)
if len(nim)==10:
    st.text("NIM : "+nim)
else:
    st.text("NIM tidak valid")
    nim = "error"

inikotak = st.selectbox('Piiih Matkul', ['B.Inggirs', 'B.Indo'])
st.write(inikotak)

umur = st.slider("Umur",1,100, 10)
st.write(umur)
nilai = st.slider("Nilai",1.0,100.0, 10.0)

gender = st.radio('Gender', ['Pria', 'Wanita'])
st.write(gender)

list_hobi = st.text_area("Hobi", "Main bola, Main game")
list_hobi = [x.strip() for x in list_hobi.split(',')]
st.write(list_hobi)

st.image('https://cdn0-production-images-kly.akamaized.net/Egstv2ByRF68XG1HmJ9pSYkg4Ek=/1200x900/smart/filters:quality(75):strip_icc():format(webp)/kly-media-production/medias/1708993/original/076507700_1505298199-wesdrftgvyhbjnk.jpg', width=300, caption='ini hamster')
st.markdown('[Ini link ke bing](https://cdn0-production-images-kly.akamaized.net/Egstv2ByRF68XG1HmJ9pSYkg4Ek=/1200x900/smart/filters:quality(75):strip_icc():format(webp)/kly-media-production/medias/1708993/original/076507700_1505298199-wesdrftgvyhbjnk.jpg)')

import pandas as pd
data ={'Pekerjaan':['Programmer', 'Bakteri', 'Pengacara'],
       'Tier':['A', 'B', 'C']}
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

st.title("Buka Data")
file = st.file_uploader("Pilih file CSV", type=['jpg', 'csv'])
if file is not None:
    st.write(file.type)
    if file.type== "image/jpeg":
        st.image(file)
    else:
        data = pd.read_csv(file)
        st.dataframe(data)

# try:
#     st.image(file)
# except:
#     data = pd.read_csv(file)
#     st.dataframe(data)
    
print("Hello world")

st.title("Kalkulator")

angka1 = st.number_input("Masukkan angka 1 : ", value = 0)
angka2 = st.number_input("Masukkan angka 2 : ", value = 0)

operasi = st.radio("Pilih operasi",['+','-','/','*'])

if st.button('hitung'):
    if operasi=="+":
        hasil = angka1+angka2
    elif operasi=='-':
        hasil = angka1-angka2
    elif operasi=='/':
        hasil = angka1/angka2
    elif operasi=='*':
        hasil = angka1*angka2

    st.success(f'Hasil {operasi} : {hasil}')

st.sidebar.header('fitur kiri')
if st.sidebar.checkbox('Kuadrat'):
    st.sidebar.write(f'Kuadrat dari {angka1}: {angka1**2}')
