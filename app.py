import streamlit as st
import pandas as pd
import numpy as np

# Judul aplikasi
st.title('🧬 Life Analytics Dashboard')

# Header
st.header('Dashboard Analisis Kehidupan Berdasarkan Umur')

# Text input
name = st.text_input('Masukkan nama Anda:')
if name:
    st.write(f'Halo, {name}! Mari kita analisis fase kehidupan Anda.')

# Slider
age = st.slider('Pilih umur:', 0, 100, 25)
st.write(f'Umur Anda: {age} tahun')

# === ANALISIS BERDASARKAN UMUR ===
if age > 0:
    col1, col2 = st.columns(2)
    
    with col1:
        # 1. Fase Kehidupan
        st.subheader('🌱 Fase Kehidupan')
        if age <= 2:
            fase = "Bayi"
            desc = "Masa pertumbuhan pesat dan perkembangan dasar"
        elif age <= 12:
            fase = "Anak-anak"
            desc = "Masa belajar dan eksplorasi dunia"
        elif age <= 17:
            fase = "Remaja"
            desc = "Masa pencarian identitas dan perubahan fisik"
        elif age <= 25:
            fase = "Dewasa Muda"
            desc = "Masa membangun karir dan hubungan"
        elif age <= 65:
            fase = "Dewasa"
            desc = "Masa produktif dan mapan"
        else:
            fase = "Lansia"
            desc = "Masa kebijaksanaan dan menikmati hidup"
        
        st.info(f"**{fase}**: {desc}")
    
    with col2:
        # 2. Statistik Usia
        st.subheader('📊 Statistik Umur')
        days_lived = age * 365
        weeks_lived = age * 52
        months_lived = age * 12
        
        st.metric("Hari yang telah dijalani", f"{days_lived:,}")
        st.metric("Minggu yang telah dijalani", f"{weeks_lived:,}")
        st.metric("Bulan yang telah dijalani", f"{months_lived:,}")

    # 3. Grafik Ekspektasi Hidup
    st.subheader('📈 Proyeksi Kehidupan')
    
    # Data ekspektasi hidup Indonesia (rata-rata)
    life_expectancy = 71
    years_remaining = max(0, life_expectancy - age)
    life_percentage = (age / life_expectancy) * 100 if age <= life_expectancy else 100
    
    # Progress bar kehidupan
    st.progress(life_percentage / 100)
    st.write(f"Persentase hidup yang telah dijalani: {life_percentage:.1f}%")
    st.write(f"Estimasi tahun tersisa: {years_remaining} tahun")

    # 4. Grafik Kemampuan Fisik vs Umur (versi sederhana)
    st.subheader('💪 Kemampuan Fisik Berdasarkan Umur')
    
    ages = list(range(0, 101, 5))
    physical_ability = [100 * np.exp(-0.5 * ((x - 27) / 15) ** 2) for x in ages]
    
    df_physical = pd.DataFrame({
        'Umur': ages,
        'Kemampuan Fisik (%)': physical_ability
    })
    st.line_chart(df_physical.set_index('Umur'))

    # 5. Grafik Tahapan Pendidikan & Karir
    st.subheader('🎓 Timeline Pendidikan & Karir')
    
    milestones = [
        (6, "Mulai SD", "education"),
        (12, "Mulai SMP", "education"),
        (15, "Mulai SMA", "education"),
        (18, "Lulus SMA", "education"),
        (22, "Lulus Kuliah", "education"),
        (23, "Mulai Karir", "career"),
        (30, "Karir Menengah", "career"),
        (45, "Karir Senior", "career"),
        (55, "Menuju Pensiun", "career"),
        (60, "Pensiun", "retirement")
    ]
    
    # Tampilkan timeline sebagai tabel
    timeline_data = []
    for milestone_age, event, category in milestones:
        status = "✅ Sudah" if milestone_age <= age else "⏳ Belum"
        timeline_data.append({
            "Umur": milestone_age,
            "Tahapan": event,
            "Kategori": category.title(),
            "Status": status
        })
    
    df_timeline = pd.DataFrame(timeline_data)
    st.dataframe(df_timeline, use_container_width=True)
    
    # Progress bar untuk milestone
    completed_milestones = len([m for m in milestones if m[0] <= age])
    total_milestones = len(milestones)
    progress = completed_milestones / total_milestones
    
    st.progress(progress)
    st.write(f"Progress: {completed_milestones}/{total_milestones} milestone tercapai ({progress:.1%})")

    # 6. Rekomendasi Berdasarkan Umur
    st.subheader('💡 Rekomendasi untuk Usia Anda')
    
    recommendations = []
    if age < 18:
        recommendations = [
            "🎯 Fokus pada pendidikan dan pengembangan minat",
            "🏃‍♂️ Jaga kesehatan dengan olahraga teratur",
            "👥 Bangun hubungan sosial yang sehat",
            "📚 Kembangkan kebiasaan membaca dan belajar"
        ]
    elif age < 30:
        recommendations = [
            "💼 Bangun fondasi karir yang kuat",
            "💰 Mulai menabung dan investasi",
            "🎯 Tentukan tujuan hidup jangka panjang",
            "💪 Jaga kesehatan fisik dan mental"
        ]
    elif age < 50:
        recommendations = [
            "📈 Kembangkan keahlian profesional",
            "👨‍👩‍👧‍👦 Fokus pada keluarga dan hubungan",
            "💰 Tingkatkan investasi untuk masa depan",
            "🧘‍♂️ Jaga keseimbangan hidup-kerja"
        ]
    else:
        recommendations = [
            "🎯 Persiapkan masa pensiun",
            "👥 Berbagi pengalaman dengan generasi muda",
            "🏥 Prioritaskan kesehatan",
            "🌅 Nikmati pencapaian dan hobi"
        ]
    
    for rec in recommendations:
        st.write(f"• {rec}")

# Chart random (kode asli)
st.subheader('📊 Data Random untuk Demonstrasi')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)

# File uploader
st.subheader('📁 Upload File CSV')
uploaded_file = st.file_uploader("Upload CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)