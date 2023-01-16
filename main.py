import streamlit as st

import numpy as np

from streamlit_option_menu import option_menu


# welcome        
with st.sidebar :
    
    from PIL import Image
    
    image = Image.open("Logo Azors.jpg")

    st.image(image, caption="")
    
    selected = option_menu ("Aplikasi Analisis Kuantitatif",
    ["Identitas Kelompok",
     "Tabel Periodik",
     "Perhitungan Bobot Sampel", 
     "Perhitungan Volume Sampel",
     "Perhitungan Normalitas (N)",
     "Perhitungan Molaritas (M)",
     "Perhitungan Molalitas (m)",
     "Perhitungan Konsentrasi PPM",
     "Perhitungan Pengenceran Konsentrasi Larutan Induk",
     "Perhitungan Pengenceran Konsentrasi Larutan Encer",
     "Perhitungan Pengenceran Volume Larutan Induk",
     "Perhitungan Pengenceran Volume larutan Encer",
     "Perhitungan Kadar Unsur Logam",
     "Perhitungan Kadar Sampel (%)",
     "Perhitungan Standarisasi Larutan Standar"], 
    default_index=0)
    
if (selected == "Identitas Kelompok") :
    
    tab1, tab2 = st.tabs(["Home", "Anggota"])

    with tab1:
        from PIL import Image
    
        image = Image.open("k.jpg")

        st.image(image, caption="")
    
    with tab2:
        st.write("1. Ainun Salsabila")
        st.write("2. Muhammad Zikrian Erwanda")
        st.write("3. Olin Riliana Agustin")
        st.write("4. Rafie Azri Avveroes")
        st.write("5. Siti Raskiah Nur Pratiwi")
         
    
if (selected == "Tabel Periodik") :
    st.title("Tabel Periodik")
    
    from PIL import Image
    
    image = Image.open("tt.jpg")

    st.image(image, caption="Tabel Periodik")


    
# Halaman hitung bobot sampel
if (selected == "Perhitungan Bobot Sampel") :
    st.title('Perhitungan mencari bobot sampel (mg) ')
    
    st.write("Perhitungan mencari bobot sampel (mg) ")
    st.latex(r''' (Mr/Ar)*Volume*Konsentrasi ''')
    Mr = st.number_input("Masukkan Mr senyawa = ")
    Ar = st.number_input("Masukkan Ar unsur = ")
    Konsentrasi = st.number_input("Masukkan konsentrasi (N) sampel = ")
    Volume = st.number_input("Masukkan volume sampel (L) yang dibutuhkan = ")
    tombol = st.button ("Hitung nilai bobot sampel")
    
    if tombol:
        bobot_sampel = (Mr/Ar)*Volume*Konsentrasi
        st.success(f"Jumlah Bobot Sampel (mg) sebesar... {round (bobot_sampel,4)}")
        st.balloons()
               
# Halaman hitung volume sampel           
if (selected == "Perhitungan Volume Sampel") :
    st.title("Perhitungan mencari volume sampel")
    
    st.write("Perhitungan mencari volume sampel")
    st.latex(r''' Bobot/(Mr/Ar)*Konsentrasi ''')
    Bobott = st.number_input("Masukkan bobot (mg) sampel = ")
    Mrr = st.number_input("Masukkan Mr sampel")
    Arr = st.number_input("Masukkan Ar sampel")
    Konsentrasi = st.number_input("Masukkan consentrasi (N) sampel = ")
    tombol = st.button ("Hitung jumlah volume (L) sampel")
    if tombol:
        volume_sampel = Bobott/((Mrr/Arr)*Konsentrasi)
        st.success(f"Jumlah Volume Sampel (L) sebesar...{round (volume_sampel,2)}")
        st.balloons()
    
    
# Halaman hitung Normalitas
if (selected == "Perhitungan Normalitas (N)") :
    st.title("Perhitungan mencari Normalitas sampel")
        
    st.write("Perhitungan mencari Normalitas sampel")
    st.latex(r''' (Bobot/BE)*Volume ''')
    Bobottt = st.number_input("Masukkan bobot (gr) sampel = ")
    Bst = st.number_input("Masukkan BE sampel")
    Volumee = st.number_input("Masukkan volume (L) sampel")
    tombol = st.button ("Hitung Konsentrasi (N) sampel")
    if tombol:
        konsentrasi_sampel = ((Bobottt/Bst)*Volumee)
        st.success(f"Konsentrasi Sampel (N) sebesar...{round (konsentrasi_sampel,4)}")
        st.balloons()

        
# Halaman hitung Molaritas
if (selected == "Perhitungan Molaritas (M)") :
    st.title("Perhitungan mencari Molaritas sampel")
        
    st.write("Perhitungan mencari Molaritas sampel")
    st.latex(r''' (Bobot/Mr)*Volume ''')
    Bobottt = st.number_input("Masukkan bobot (gr) sampel = ")
    Mrrr = st.number_input("Masukkan Mr sampel")
    Volumee = st.number_input("Masukkan volume (L) sampel")
    tombol = st.button ("Hitung Konsentrasi (M) sampel")
    if tombol:
        konsentrasi_sampel = ((Bobottt/Mrrr)*Volumee)
        st.success(f"Konsentrasi Sampel (M) sebesar...{round (konsentrasi_sampel,4)}")
        st.balloons()
        
# Halaman hitung Molalitas       
if (selected == "Perhitungan Molalitas (m)") :
    st.title("Perhitungan mencari Molalitas sampel")
        
    st.write("Perhitungan mencari Molalitas sampel")
    st.latex(r''' (Bobot Zat Terlarut/Mr)/(Bobot Zat Pelarut) ''')
    Bobotterlarut = st.number_input("Masukkan Bobot Zat Terlarut (gr) sampel = ")
    MMrr = st.number_input("Masukkan Mr sampel")
    Bobotlarutan = st.number_input("Masukkan Bobot larutan (Kg) sampel")
    tombol = st.button ("Hitung Konsentrasi (m) sampel")
    if tombol:
        konsentrasi_sampel = ((Bobotterlarut/MMrr)/Bobotlarutan)
        st.success(f"Konsentrasi Sampel (m) sebesar...{round (konsentrasi_sampel,4)}")
        st.balloons()

# Halaman hitung ppm        
if (selected == "Perhitungan Konsentrasi PPM") :
    st.title("Perhitungan mencari Konsentrasi ppm")
        
    st.write("Perhitungan mencari Konsentrasi ppm")
    st.latex(r''' (Bobot/Volume) ''')
    Bobot1 = st.number_input("Masukkan bobot zat terlarut (mg)")
    Volumeee = st.number_input("Masukkan Volume Larutan (L)")
    tombol = st.button ("Hitung Konsentrasi (ppm) sampel")
    if tombol:
        ppm_sampel = (Bobot1/Volumeee)
        st.success(f"Konsentrasi Sampel (ppm) sebesar...{round (ppm_sampel,2)}")
        st.balloons()
 

# Halaman hitung pengenceran


if (selected == "Perhitungan Pengenceran Konsentrasi Larutan Induk") :
    st.title("Perhitungan Konsentrasi Larutan Induk")
    
    st.latex(r''' (V1*C1(induk)/V2(encer)) ''')
    VolumeIndukk = st.number_input("Masukkan Volume (mL) larutan induk")
    KonsentrasiEncerr = st.number_input("Masukkan konsentrasi larutan encer ")
    VolumeEncerr = st.number_input("Masukkan volume (mL) larutan encer")
    tombol = st.button ("Hitung Konsentrasi larutan encer")
    if tombol:
        pengenceran_larutan = (VolumeEncerr*KonsentrasiEncerr)/(VolumeIndukk)
        st.success(f"Konsentrasi Larutan Induk sebesar...{round (pengenceran_larutan,4)}")
        st.balloons()
        
        
if (selected == "Perhitungan Pengenceran Konsentrasi Larutan Encer") :
    st.title("Perhitungan Konsentrasi Larutan Encer")
    
    st.latex(r''' (V1*C1(induk)/V2(encer)) ''')
    VolumeIndukk = st.number_input("Masukkan Volume (mL) larutan induk")
    KonsentrasiIndukk = st.number_input("Masukkan konsentrasi larutan induk ")
    VolumeEncerr = st.number_input("Masukkan volume (mL) larutan encer")
    tombol = st.button ("Hitung Konsentrasi larutan encer")
    if tombol:
        pengenceran_larutan = (VolumeIndukk*KonsentrasiIndukk)/(VolumeEncerr)
        st.success(f"Konsentrasi Larutan Encer sebesar...{round (pengenceran_larutan,4)}")
        st.balloons() 
        
 
if (selected == "Perhitungan Pengenceran Konsentrasi Larutan Induk") :
    st.title("Perhitungan Konsentrasi Larutan induk")
    
    st.latex(r''' (V1(induk)/V2*C2(encer)) ''')
    VolumeInduk = st.number_input("Masukkan Volume (mL) larutan induk")
    KonsentrasiEncer = st.number_input("Masukkan konsentrasi larutan encer ")
    VolumeEncerr = st.number_input("Masukkan volume (mL) larutan encer")
    tombol = st.button ("Hitung Konsentrasi larutan induk")
    if tombol:
        pengenceran_larutan = (VolumeInduk)/(VolumeEncerr*KonsentrasiEncer)
        st.success(f"Konsentrasi Larutan Encer sebesar...{round (pengenceran_larutan,4)}")
        st.balloons() 
 

if (selected == "Perhitungan Pengenceran Volume Larutan Induk") :
    st.title("Perhitungan Volume Larutan induk")
    
    st.latex(r''' (V2*C2(encer)/C1(induk)) ''')
    KonsentrasiIndukk = st.number_input("Masukkan konsentrasi larutan induk ")
    KonsentrasiEncer = st.number_input("Masukkan konsentrasi larutan encer ")
    VolumeEncerr = st.number_input("Masukkan volume (mL) larutan encer")
    tombol = st.button ("Hitung Volume larutan induk")
    if tombol:
        pengenceran_larutan = (VolumeEncerr*KonsentrasiEncer)/(KonsentrasiIndukk)
        st.success(f"Volume Larutan Induk sebesar...{round (pengenceran_larutan,2)}")
        st.balloons() 
        
        
if (selected == "Perhitungan Pengenceran Volume Larutan Encer") :
    st.title("Perhitungan Volume Larutan Encer")
    
    st.latex(r''' (V1*C1(induk)/C2(encer)) ''')
    VolumeIndukk = st.number_input("Masukkan volume (mL) larutan induk")
    KonsentrasiIndukkk = st.number_input("Masukkan Konsentrasi larutan induk ")
    KonsentrasiEncerr = st.number_input("Masukkan konsentrasi larutan encer")
    tombol = st.button ("Hitung Volume larutan encer")
    if tombol:
        pengenceran_larutan = (VolumeIndukk*KonsentrasiIndukkk)/(KonsentrasiEncerr)
        st.success(f"Volume Larutan Encer sebesar...{round (pengenceran_larutan,2)}")
        st.balloons() 

# Halaman hitung kadar logam       
if (selected == "Perhitungan Kadar Unsur Logam") :
    st.title("Perhitungan mencari kadar (%) logam")
    
    st.write("Perhitungan mencari kadar logam")
    st.latex(r''' ((V*N*Be)/gr))*100% ''')
    V = st.number_input("Masukkan volume (mL) sampel = ")
    N = st.number_input("Masukkan Normalitas sampel")
    BE = st.number_input("Masukkan Be sampel")
    gr = st.number_input("Masukkan bobot sampel")
    tombol = st.button ("Hitung jumlah kadar (%) sampel")
    if tombol:
        kadar_sampel = (((V*N*BE)/gr)*100)
        st.success(f"Jumlah Kadar Sampel (%) sebesar...{round (kadar_sampel,2)}")
        st.balloons()
        
if (selected == "Perhitungan Kadar Sampel (%)") :

    tab1, tab2, tab3 = st.tabs(["%b/b", "%v/v", "%b/v"])

    with tab1:
        st.title("Perhitungan mencari %b/b")
    
        st.write("Perhitungan mencari %b/b sampel")
        st.latex(r''' (gr Zat Terlarut/gr Larutan)*100%  ''')
        grzat1 = st.number_input("Masukkan bobot (gr) zat terlarut sampel = ")
        grlarutan = st.number_input("Masukkan bobot (gr) larutan sampel")
        tombol = st.button ("Hitung jumlah persen berat (% b/b) sampel")
        if tombol:
            berat_sampel = ((grzat1/grlarutan)*100)
            st.success(f"Jumlah Persen (% b/b) Sampel sebesar...{round (berat_sampel,2)}")
            st.balloons()

    with tab2:
        st.title("Perhitungan mencari %v/v")
    
        st.write("Perhitungan mencari %v/v sampel")
        st.latex(r''' (mL Zat Terlarut/mL Larutan)*100%  ''')
        mLZatTerlarut = st.number_input("Masukkan volume (mL) zat terlarut sampel = ")
        mLlarutan = st.number_input("Masukkan volume (mL) larutan sampel")
        tomboll = st.button ("Hitung jumlah persen berat (% v/v) sampel")
        if tomboll:
            volume_sampel = ((mLZatTerlarut/mLlarutan)*100)
            st.success(f"Jumlah Persen (%v/v) Sampel sebesar...{round (volume_sampel,2)}")
            st.balloons()
        
    with tab3:
        st.title("Perhitungan mencari %b/v")
    
        st.write("Perhitungan mencari %b/v sampel")
        st.latex(r''' (gr Zat Terlarut/mL Larutan)*100%  ''')
        grZatTerlarutt = st.number_input("Masukkan gram (gr) zat terlarut sampel = ")
        mLLarutann = st.number_input("Masukkan Volume (mL) larutan sampel")
        tombolll = st.button ("Hitung jumlah persen berat / volume (% b/v) sampel")
        if tombolll:
            volume_sampel = ((grZatTerlarutt/mLLarutann)*100)
            st.success(f"Jumlah Persen (% b/v) Sampel sebesar...{round (volume_sampel,2)}")
            st.balloons()
    
# Halaman hitung standarirasi        
if (selected == "Perhitungan Standarisasi Larutan Standar") :
    st.title("Perhitungan mencari Standarisasi Larutan Standar (N)")
    
    st.write("Perhitungan mencari Standarisasi Larutan Standar")
    st.latex(r''' mg Bahan Baku/(ml Larutan*BE Bahan Baku) ''')
    mgBahanBaku = st.number_input("Masukkan bobot (mg) bahan baku = ")
    mlLLarutan = st.number_input("Masukkan volume (ml) larutan yang dititar")
    BEBahanBaku = st.number_input("Masukkan Be Bahan Baku")
    tombol = st.button ("Hitung Standarisasi Larutan Standar (N)")
    if tombol:
        kadar_sampel = mgBahanBaku/(mlLLarutan*BEBahanBaku)
        st.success(f"Standarisasi Larutan Standar (N) sebesar...{round (kadar_sampel,4)}")
        st.balloons()
        
        
        

        

        



        
