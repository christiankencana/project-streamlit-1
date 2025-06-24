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

# Ganti bagian Chart random dengan yang lebih relevan
st.subheader('📊 Tren Harapan Hidup Indonesia')

# Data harapan hidup Indonesia dari tahun ke tahun
years = [2010, 2012, 2014, 2016, 2018, 2020, 2022]
life_expectancy_trend = [68.1, 68.6, 69.1, 69.4, 70.8, 71.1, 71.7]

chart_data = pd.DataFrame({
    'Tahun': years,
    'Harapan Hidup': life_expectancy_trend
})

st.line_chart(chart_data.set_index('Tahun'))
st.caption("Data harapan hidup rata-rata di Indonesia menunjukkan tren peningkatan")

# Atau bisa diganti dengan grafik distribusi populasi berdasarkan umur
st.subheader('📈 Distribusi Populasi Indonesia Berdasarkan Kelompok Umur')

age_groups = ['0-14', '15-24', '25-34', '35-44', '45-54', '55-64', '65+']
population_percentage = [24.6, 16.7, 17.0, 13.8, 11.8, 8.8, 7.3]

population_data = pd.DataFrame({
    'Kelompok Umur': age_groups,
    'Persentase Populasi': population_percentage
})

st.bar_chart(population_data.set_index('Kelompok Umur'))
st.caption("Distribusi populasi Indonesia berdasarkan kelompok umur (data BPS)")

# Atau hapus bagian file uploader juga dan ganti dengan something more relevant
st.subheader('🎯 Target Pencapaian Berdasarkan Dekade')

decades = {
    '20-30 tahun': ['Lulus kuliah', 'Mulai karir', 'Membangun network', 'Menikah (opsional)'],
    '30-40 tahun': ['Naik jabatan', 'Membeli rumah', 'Punya anak (opsional)', 'Investasi serius'],
    '40-50 tahun': ['Karir puncak', 'Pendidikan anak', 'Persiapan pensiun', 'Kesehatan optimal'],
    '50-60 tahun': ['Mentoring junior', 'Hobi & passion', 'Persiapan pensiun', 'Wisdom sharing'],
    '60+ tahun': ['Menikmati pensiun', 'Cucu & keluarga', 'Traveling', 'Kontribusi sosial']
}

# Tentukan dekade user saat ini
current_decade = f"{(age//10)*10}-{((age//10)+1)*10} tahun"

if current_decade in decades:
    st.info(f"Target untuk dekade Anda ({current_decade}):")
    for target in decades[current_decade]:
        st.write(f"• {target}")
else:
    st.write("Setiap fase kehidupan memiliki target dan pencapaiannya masing-masing!")