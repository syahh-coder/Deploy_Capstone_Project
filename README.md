# 🌍 TemanCekin*

## 📌 Deskripsi  
Kesehatan mental generasi muda kerap kali terabaikan di tengah padatnya aktivitas pendidikan. Padahal, tekanan akademik maupun sosial bisa berdampak serius pada keseharian. Sayangnya, terkadang akses untuk diagnosis maupun konsultasi kesehatan mental masih tergolong sulit, terutama bagi mahasiswa. Oleh karena itu, kami hadir dengan TemanCekin*.
TemanCekin* adalah sebuah website yang akan menjadi teman untuk membantu ngecekin kesehatan mental mahasiswa hanya dengan gadget dalam waktu sekejap. Dengan mengimplementasi model machine mearning yang sudah dilatih dengan data “Student Mental Health Rating” yang real, TemanCekin* dapat membantu mahasiswa untuk mendapatkan nilai serta evaluasi terkait mental health penggunanya yang didasarkan dari inputan sederhana.

## 🎥 Video Pitch & Presentation
- *Video Pitch (3-5 menit)*: [Berisi gambaran umum proyek, masalah yang diselesaikan, dan manfaatnya]

- *Video Presentation (10-15 menit)*: [Berisi penjelasan mendetail tentang teknis proyek, model, hasil, dan demo]

- *Link Video*: [YouTube]

## 🎯 Tujuan & Keterkaitan dengan SDGs  
Proyek ini berkontribusi terhadap *SDG 3 dan 4* yaitu **Quality Education dan Good Health and Well-being*.
TemanCekin* hadir di ranah edukasi yang memerhatikan kesehatan mental, terutama mahasiswa, dengan mengusung SDGs “Quality Education” serta “Good Health and Wellbeing”. TemanCekin* memberikan gambaran serta evaluasi kesehatan mental mahasiswa dengan compact sehingga dapat dipakai dengan mudah dan cepat.

## 🛠 Teknologi yang Digunakan  
- *Framework ML/DL:* Scikit-Learn (model RandomForestRegressor)
- *Dataset:* Student Habits vs Academic Performance: https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-performance   
- *Deployment:* Streamlit

## 📊 Model & Metodologi  :
Model yang digunakan dalam proyek ini adalah RandomForestRegressor, sebuah algoritma ensemble learning yang terdiri dari banyak decision tree. Setiap pohon dalam model ini menghasilkan prediksi sendiri, lalu seluruh prediksi tersebut dirata-rata untuk menghasilkan output akhir. Pendekatan ini membuat RandomForestRegressor mampu menangani data yang kompleks dan non-linear serta lebih tahan terhadap overfitting. Pada bagian arsitektur, model ini dibangun dari sejumlah pohon keputusan yang masing-masing dilatih pada subset acak dari data, dengan kedalaman pohon yang dapat disesuaikan. Untuk mengukur performa model, digunakan Mean Squared Error (MSE) sebagai teknik evaluasi. MSE menghitung rata-rata selisih kuadrat antara nilai prediksi dan nilai sebenarnya, di mana semakin kecil nilai MSE, maka semakin baik akurasi prediksi yang dihasilkan oleh model.



## 🚀 Cara Menjalankan Proyek  
1. Clone repository ini:  
   bash
   git clone https://github.com/syahh-coder/Deploy_Capstone_Project
   cd Deploy_Capstone_Project

2. Install dependencies:
bash
pip install -r requirements.txt

3. Jalankan model atau aplikasi
bash
streamlit run mentalhealth.py

## 🔗 Link Deployment
Aplikasi dapat diakses di sini: https://temancekin.streamlit.app/
## 📈 Hasil & Analisis
*Performa Metrik Model* : MSE (Mean Squared Error): 5,02. sebenarnya pada saat train model, banyak model regresi yang lebih akurat dibanding RandomforestRegressor seperti RidgerRegressor dengan MSE 3,6 kemudian Linear Regression dengan 3,6 jg, hanya saja saat menampilkan prediksi hasilnya dapat mencapai lebih dari interval pada nilat target (rating mentalhealth), sebagai contoh pada Linear Regression hasil prediksi dapat mencapai 16,7/10. Disamping itu, pada saat menggunakan RandomForestRegressor hasilnya belum pernah mencapai lebih dari interval. Hal ini disebabkan, pada model lain hasil prediksi bisa menjadi liar (tak terbatas) sedangkan pada randomForest terbatas secara alami disebabkan Random Forest Regressor adalah ensemble dari banyak decision tree, Masing-masing tree memprediksi angka, dan hasil akhirnya adalah rata-rata dari semua prediksi tree Karena setiap tree-nya hanya memetakan ke nilai target yang pernah ada di data latih, maka Output cenderung berada di dalam rentang nilai-nilai di data training dan tidak ada prediksi "liar" seperti 16,7 kalau tidak ada rating 16,7 di data latih.

*Kesimpulan*: Model yang paling cocok untuk kasus menentukan rating mentalhealth adalah RandomForestRegressor disebabkan adanya batas alami yang menyebabkan hasil prediksi tidak melebihi maksimal rating.

## 👨‍💻 Tim Pengembang (SukaML)
- Ukasyah - www.linkedin.com/in/ukasyah2005/ 
- Naufal Hanif - http://www.linkedin.com/in/naufal-hanif-8a8162331

