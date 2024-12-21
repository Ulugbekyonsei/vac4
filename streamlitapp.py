import streamlit as st
import math
st.title("Oilada bolalarga nisbatan jismoniy zo'ravonlik riskini hisoblovchi dastur")
st.write("*Ulug'bek Tursunov*")
st.write("Har bir ko'rsatkich uchun qiymatlarni kiriting:")

# Coefficients from the provided model
intercept = 0.615
coef_bolaning_yoshi = -0.011
coef_ogil_bola = 0.198
coef_bolada_nogironlik = 0.636
coef_bolaning_yetimligi = -0.304
coef_qarovchi_yoshi = -0.044
coef_qarovchi_oliy = -0.11
coef_qarovchida_nogironlik = 0.185
coef_oilada_bolalar_soni = 0.057
coef_mulk_indeksi = -0.089
coef_oila_boshligi_yoshi = -0.005
coef_oila_boshligi_jinsi = 0.105
coef_oila_boshligi_oliy = 0.115
coef_oilada_kattalar_bolalarga_nisbati = 0.004
coef_qishloq=-0.134
coef_viloyat=1

# Input widgets
bolaning_yoshi = st.number_input("Bolaning yoshi", min_value=0, max_value=14, value=5)
ogil_bola = st.selectbox("Bola jinsi (o'g'il = 1, qiz = 0)", [0,1])
bolada_nogironlik = st.selectbox("Bolada nogironlik mavjudligi (bor = 1, yo'q = 0)", [0,1])
bolaning_yetimligi = st.selectbox("Bolaning yetimligi (ota yoki onasining vafot etganligi) (yetim = 1, yetim emas = 0)", [0,1])
qarovchi_yoshi = st.number_input("Qarovchining yoshi", min_value=0, max_value=100, value=35)
qarovchi_oliy = st.selectbox("Qarovchi oliy ta'limga ega (ha = 1, yo'q = 0)", [0,1])
qarovchida_nogironlik = st.selectbox("Qarovchida nogironlik (bor = 1, yo'q = 0)", [0,1])
oilada_bolalar_soni = st.number_input("Oilada bolalar soni", min_value=0, max_value=20, value=2)
selected_option = st.selectbox(
    "Oilaning farovonlik holati",
    ["Kambag'al", "O'rtachadan past", "O'rtacha", "O'rtachadan yuqori", "Boy"]
)

# Map the selected option to the corresponding mulk_indeksi value
mulk_indeksi_values = {
    "Kambag'al": -1.255064,
    "O'rtachadan past": -0.7030844,
    "O'rtacha": -0.2666492,
    "O'rtachadan yuqori": 0.2791034,
    "Boy": 1.334109
}

# Assign the corresponding value to mulk_indeksi
mulk_indeksi = mulk_indeksi_values[selected_option]
oila_boshligi_yoshi = st.number_input("Oila boshlig'i yoshi", min_value=0, max_value=100, value=40)
oila_boshligi_jinsi = st.selectbox("Oila boshlig'i jinsi (erkak = 1, ayol = 0)", [0,1])
oila_boshligi_oliy = st.selectbox("Oila boshlig'i oliy ta'limga ega (ha = 1, yo'q = 0)", [0,1])
oilada_kattalar_bolalarga_nisbati = st.number_input("Oilada kattalar sonining bolalar soniga nisbati", value=1.0, format="%.3f")
qishloq = st.selectbox("Qishloq yoki shahar (Qishloq = 1, Shahar = 0)", [0,1])
selected_option_viloyat=st.selectbox(
    "Oila yashovchi hudud:",
    ["Qoraqolpog'iston", "Andijon", "Buxoro",
     "Jizzax", "Qashqadaryo", "Navoiy",
      "Namangan", "Samarqand", "Surxandaryo",
       "Sirdaryo", "Toshkent viloyati", "Farg'ona",
        "Xorazm", "Toshkent shahri" ]
)

viloyat_values = {
    "Qoraqolpog'iston": 0,
    "Andijon": -1.002,
    "Buxoro": 0.112,
    "Jizzax": -0.408,
    "Qashqadaryo": 0.430,
    "Navoiy": 0.047,
    "Namangan": -0.598,
    "Samarqand":0.650,
    "Surxandaryo": 0.551,
    "Sirdaryo" : -0.799,
    "Toshkent viloyati": 0.298,
    "Farg'ona": -0.457,
    "Xorazm": -0.403,
    "Toshkent shahri": 0 

}

viloyat = viloyat_values[selected_option_viloyat]


# Compute the predicted value
y= (intercept
              + coef_bolaning_yoshi * bolaning_yoshi
              + coef_ogil_bola * ogil_bola
              + coef_bolada_nogironlik * bolada_nogironlik
              + coef_bolaning_yetimligi * bolaning_yetimligi
              + coef_qarovchi_yoshi * qarovchi_yoshi
              + coef_qarovchi_oliy * qarovchi_oliy
              + coef_qarovchida_nogironlik * qarovchida_nogironlik
              + coef_oilada_bolalar_soni * oilada_bolalar_soni
              + coef_mulk_indeksi * mulk_indeksi
              + coef_oila_boshligi_yoshi * oila_boshligi_yoshi
              + coef_oila_boshligi_jinsi * oila_boshligi_jinsi
              + coef_oila_boshligi_oliy * oila_boshligi_oliy
              + coef_oilada_kattalar_bolalarga_nisbati * oilada_kattalar_bolalarga_nisbati
              + coef_viloyat*viloyat 
              +coef_qishloq*qishloq)

prediction=1/(1+math.exp(-y))

st.write("### Oilada bolaga nisbatan zo'ravonlik yuz berish ehtimoli:")
st.write(100*prediction)

st.write("Ushbu dastur test rejimida!")
