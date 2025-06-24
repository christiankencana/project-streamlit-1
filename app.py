import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

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

    # 4. Grafik Kemampuan Fisik vs Umur
    st.subheader('💪 Kemampuan Fisik Berdasarkan Umur')
    
    ages = list(range(0, 101, 5))
    # Simulasi kurva kemampuan fisik (puncak di umur 25-30)
    physical_ability = [
        100 * np.exp(-0.5 * ((x - 27) / 15) ** 2) for x in ages
    ]
    
    fig_physical = go.Figure()
    fig_physical.add_trace(go.Scatter(
        x=ages, y=physical_ability,
        mode='lines+markers',
        name='Kemampuan Fisik (%)',
        line=dict(color='red', width=3)
    ))
    fig_physical.add_vline(x=age, line_dash="dash", 
                          annotation_text=f"Usia Anda: {age}")
    fig_physical.update_layout(
        title="Kemampuan Fisik vs Umur",
        xaxis_title="Umur (tahun)",
        yaxis_title="Kemampuan Fisik (%)",
        height=400
    )
    st.plotly_chart(fig_physical, use_container_width=True)

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
    
    fig_timeline = go.Figure()
    
    for milestone_age, event, category in milestones:
        color = 'blue' if category == 'education' else 'green' if category == 'career' else 'orange'
        opacity = 1.0 if milestone_age <= age else 0.3
        
        fig_timeline.add_trace(go.Scatter(
            x=[milestone_age], y=[1],
            mode='markers+text',
            marker=dict(size=15, color=color, opacity=opacity),
            text=event,
            textposition="top center",
            name=category,
            showlegend=False
        ))
    
    fig_timeline.add_vline(x=age, line_dash="dash", line_color="red",
                          annotation_text=f"Anda di sini ({age})")
    fig_timeline.update_layout(
        title="Timeline Kehidupan",
        xaxis_title="Umur (tahun)",
        yaxis=dict(visible=False),
        height=300,
        xaxis=dict(range=[0, 70])
    )
    st.plotly_chart(fig_timeline, use_container_width=True)

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