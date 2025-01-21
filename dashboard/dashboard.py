import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


rental_df = pd.read_csv('dashboard/main_data.csv')

with st.sidebar:
    st.write("Istia Budi")
    st.write("istiabudi@gmail.com")

    st.write("### Filter Data")
    start_date = st.date_input("Mulai Tanggal", pd.to_datetime(rental_df['dteday']).min())
    end_date = st.date_input("Akhir Tanggal", pd.to_datetime(rental_df['dteday']).max())

st.header("Bike Sharing Analysis")

st.subheader("Bagaimana cuaca mempengaruhi rental sepeda?")

result = rental_df.groupby(by="weathersit").instant.nunique().sort_index().reset_index()

fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='weathersit', y='cnt', data=rental_df, palette='pastel', ax=ax)
ax.set_title("Hubungan Cuaca dan Jumlah Rental")
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Jumlah Rental')
ax.set_xticks(result.index)
st.pyplot(fig)

with st.expander("Lihat Analisis"):
    st.write(
        '''
        Pengaruh Cuaca terhadap Rental Sepeda:

Cuaca sangat memengaruhi jumlah penyewaan sepeda. Cuaca cerah dan berawan ringan mencatat jumlah rental tertinggi, menunjukkan bahwa kondisi yang nyaman meningkatkan minat masyarakat untuk bersepeda. Sebaliknya, kondisi berkabut dan berawan memiliki jumlah rental yang sedang, sedangkan hujan dan salju ringan mencatat jumlah rental terendah. Hal ini mengindikasikan bahwa cuaca buruk seperti hujan atau salju secara signifikan mengurangi minat pengguna untuk menyewa sepeda.
'''
    )

st.subheader("Bagaimana musim mempengaruhi rental sepeda?")

result = rental_df.groupby(by="season").instant.nunique().sort_index().reset_index()

fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='season', y='cnt', data=rental_df, palette='pastel', ax=ax)
ax.set_title("Hubungan Musim dan Jumlah Rental")
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah Rental')
ax.set_xticks(result.index)

st.pyplot(fig)

with st.expander("Lihat Analisis"):
    st.write(
        '''
        Pengaruh Musim terhadap Rental Sepeda:

Jumlah penyewaan sepeda bervariasi berdasarkan musim. Musim panas mencatat jumlah rental tertinggi karena cuaca yang hangat dan mendukung aktivitas luar ruangan, diikuti oleh musim gugur yang masih cukup nyaman untuk bersepeda. Sebaliknya, musim dingin dan musim semi memiliki jumlah rental lebih rendah, kemungkinan karena suhu dingin atau cuaca yang kurang stabil. Secara keseluruhan, aktivitas penyewaan sepeda lebih populer di musim dengan cuaca yang nyaman.
'''
    )

st.subheader("Apakah jumlah peminjam sepeda meningkat dari tahun 2011 ke 2012?")

monthly_rentals = rental_df.groupby(['yr', 'mnth'])['cnt'].sum().reset_index()

monthly_rentals['month_label'] = monthly_rentals['mnth'].apply(
    lambda x: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][x - 1]
)

fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x='month_label', y='cnt', hue='yr', data=monthly_rentals, marker='o', ax=ax)
ax.set_title('Jumlah Rental Sepeda per Bulan (2011 vs 2012)', fontsize=14)
ax.set_xlabel('Bulan')
ax.set_ylabel('Jumlah Rental')
ax.legend(title='Tahun', labels=['2011', '', '2012'])
ax.grid(axis='y', linestyle='--', alpha=0.7)

st.pyplot(fig)

with st.expander("Lihat Analisis"):
    st.write(
        '''
        Perbandingan Rental Sepeda Tahun 2011 dan 2012:

Jumlah penyewaan sepeda secara keseluruhan meningkat dari tahun 2011 ke 2012. Peningkatan signifikan terlihat khususnya pada bulan Februari hingga Juni di tahun 2012, yang menunjukkan minat yang semakin tinggi terhadap layanan rental sepeda. Tren musiman juga tetap terlihat pada kedua tahun, dengan puncak rental terjadi pada musim panas dan penurunan pada musim dingin. Peningkatan ini dapat disebabkan oleh berbagai faktor, seperti promosi layanan, penambahan fasilitas, atau meningkatnya kesadaran akan transportasi ramah lingkungan.
'''
    )