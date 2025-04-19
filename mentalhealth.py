import streamlit as st
import numpy as np
import joblib

model = joblib.load("Model_Caps_2.pkl")

st.title("Hai! TemanCekin✨​")
st.write("Membantu kamu tahu, apa kabar kamu hari ini? ​📝​")

st.divider()

st.markdown("TemanCekin akan menjadi teman untuk membantu ngecekin skor kesehatan batin kamu hari ini!")
st.write("Yuk bantu TemanCekin memahami kamu lebih jauh:")

st.write(" ")
st.write(" ")

age = st.number_input("Umur Kamu", min_value=13, max_value=60)
gender_before = st.pills("Jenis Kelamin", ["Laki-laki", "Perempuan"])
study_hours_per_day = st.number_input("Jam Belajar/Tugas dalam Sehari", min_value=0.0, max_value=24.0)
social_media_hours = st.number_input("Jam Media Sosial dalam Sehari", min_value=0.0, max_value=24.0)
sleep_hours = st.number_input("Jam Tidur dalam Sehari", min_value=0.0, max_value=24.0)
part_time_job_before = st.radio("Punya Kerja Sampingan?", ["Tidak", "Ya"])
attendance_percentage	 = st.slider("Persentase Kehadiran Kuliah (%)", min_value=0, max_value=100)
exercise_frequency = st.slider("Frekuensi Olahraga dalam Seminggu", min_value=0, max_value=7)
extracurricular_participation_2 = st.radio("Ikut UKM atau Organisasi?", ["Tidak", "Ya"])
exam_score = st.number_input("Nilai Ujian Terakhir", min_value=0.0, max_value=100.0)

gender = 0 if gender_before == "Perempuan" else 1
part_time_job = 1 if part_time_job_before == "Ya" else 0
extracurricular_participation= 1 if extracurricular_participation_2 == "Ya" else 0

st.write(" ")
col1, col2, col3 = st.columns(3)
with col1:
    pass
with col3:
    pass
with col2 :
    cek = st.button("TemanCekin Cek!")

if cek:
    st.balloons()
    fitur = np.array([[age, gender, study_hours_per_day, social_media_hours, part_time_job,
                       attendance_percentage, sleep_hours, exercise_frequency, extracurricular_participation, exam_score]])
    prediksi = model.predict(fitur)[0]
    prediksi = round(float(prediksi), 2)

    st.write(f"Skor Kesehatan Mental Kamu (1-10)")
    tile = st.container(height=120)
    tile.title(prediksi)
    
    if prediksi <= 3:
        buruk = '''📝Buruk  
        Kesehatan mental kamu berada pada kondisi yang sangat memprihatinkan dan perlu perhatian lebih segera.'''
        st.warning(buruk)
    elif prediksi > 3 and prediksi <= 5:
        rendah = '''📝Rendah  
        Kesehatan mental kamu sedang tidak stabil, mungkin kamu sedang menghadapi tekanan atau kelelahan.'''
        st.warning(rendah)
    elif prediksi > 5 and prediksi <=6:
        netral = '''📝Sedang  
        Kesehatan mental kamu cukup netral, ada keseimbangan tetapi juga ada tantangan yang perlu diperhatikan.'''
        st.info(netral)
    elif prediksi > 6 and prediksi <= 7:
        kurang = '''📝Kurang Baik  
        Kamu berada di jalur yang positif, tapi masih ada beberapa hal yang bisa ditingkatkan.'''
        st.info(kurang)
    elif prediksi > 7 and prediksi < 8.5:
        baik = '''📝Baik  
        Kesehatan mentalmu berada dalam kondisi yang cukup baik dan stabil.'''
        st.success(baik)
    elif prediksi >= 8.5 :
        terbaik = '''📝Sangat Baik  
        Kamu menunjukkan kondisi mental yang sehat, stabil, dan produktif secara keseluruhan.'''
        st.success(terbaik)


    with st.expander("Lihat lebih lanjut"):
        st.write(f"📚Kamu belajar {study_hours_per_day} jam sehari.")
        if study_hours_per_day == 0:
            st.write("Hepi sih hepi, tapi orang tuamu mencari nafkah agar kualitas dirimu naik, masa kamunya malas malasan?")
        elif study_hours_per_day > 0 and study_hours_per_day < 5:
            st.write("Bagus! Kamu sudah meluangkan waktu yang cukup untuk mempelajari hal-hal baru.")
        else:
            st.write("Belajar boleh, tapi hidup gak cuman belajar depan kertas/laptop doang. Ayo keluar dan nikmati hidupmu:)")
        st.write(" ")

        st.write(f"📱Kamu berselancar di media sosial {social_media_hours} jam sehari.")
        if social_media_hours < 1:
            st.write("Sekadar info, main medsos juga penting loh. Selain untuk refreshing, apa kamu gak takut kelihatan kampungan/katro?")
        elif social_media_hours >= 1 and social_media_hours <= 6:
            st.write("Kamu sudah meluangkan waktu yang cukup untuk berselancar di media sosial, sekarang tinggal manfaatin buat yang lain.")
        else:
            st.write("Stalking siapa sih?? Udah, kalau suka sampaikan ajaa.")
        st.write(" ")

        st.write(f"🛌Kamu tidur selama {sleep_hours} jam sehari")
        if sleep_hours < 5:
            st.write("Jam tidurmu sangat kurang, apa sih yang kau cari di dunia kawan?? Segera istirahatkan tubuhmu!")
        elif sleep_hours >=5 and sleep_hours <= 8.5:
            st.write("Kamu sudah mengistirahatkan tubuhmu dengan waktu yang cukup. Kamu punya 2 pilihan, " \
            "bangun untuk meraih mimpimu atau tidur lagi dan terlena oleh mimpimu yang bukan apa apa.")
        else:
            st.write("Malas-malasan mulu, kapan suksesnya??")
        st.write(" ")

        st.write(f"🏋️‍♂️Kamu olahraga sebanyak {exercise_frequency} kali dalam seminggu.")
        if exercise_frequency <= 1:
            st.write("Jarang olahraga yaa? Gak takut tubuhmu di masa tua cepat rusak?")
        elif exercise_frequency > 1 and exercise_frequency < 6:
            st.write("Mantap! Kamu di masa depan pasti bangga lihat kamu yang sekarang sangat produktif.")
        else:
            st.write("Sudah, istirahatkan tubuhmu. Kasihan, kecapekan dia..")
        st.write(" ")

        if part_time_job == 1:
            st.write("💪Kamu memiliki pekerjaan sampingan")
            st.write("Keren! Kamu adalah orang yang mandiri dan pekerja keras. Tetapi ingat, tetap selalu jaga kesehatan hati dan fisikmu:)")
            st.write(" ")
        if extracurricular_participation == 1:
            st.write("📢Kamu tergabung dengan UKM/organisasi")
            st.write("Keren! Kamu adalah orang yang aktif dan semangat. Tetapi ingat, tetap selalu jaga kesehatan hati dan fisikmu:)")




