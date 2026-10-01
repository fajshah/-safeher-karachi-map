import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="SafeHer Karachi", page_icon="🛡️")
st.title("🛡️ SafeHer - Women Safety Map Karachi")
st.markdown("For WTQ 2026 | By Syeda Farzana Shah")

# Sample safety data
data = {
    'Area': ['Clifton', 'Gulshan', 'Saddar', 'Orangi', 'DHA Phase 6', 'Korangi'],
    'Area': ['Clifton', 'Gulshan', 'Saddar', 'Orangi', 'DHA Phase 6', 'Korangi', 'F.B Area Block 19', 'Nazimabad', 'North Nazimabad'],
'Safety_Score': [85, 75, 40, 35, 90, 45, 65, 60, 70],
'Lat': [24.8138, 24.9265, 24.8615, 24.9500, 24.8045, 24.8250, 24.9345, 24.9210, 24.9370],
'Lon': [67.03, 67.0896, 67.0099, 66.99, 67.08, 67.13, 67.0687, 67.0300, 67.0370],
'Tip': ['Well-lit, CCTV', 'Crowded till 9pm', 'Avoid after 8pm', 'Avoid late night', 'Very Safe', 'Be cautious', 'Moderate, stay on main road', 'Okay till 10pm', 'Safe in day time']
    
   
}
df = pd.DataFrame(data)

# Map
m = folium.Map(location=[24.8607, 67.0011], zoom_start=11)
for i, row in df.iterrows():
    color = 'green' if row['Safety_Score'] > 70 else 'orange' if row['Safety_Score'] > 50 else 'red'
    folium.Marker(
        [row['Lat'], row['Lon']],
        popup=f"{row['Area']}: {row['Safety_Score']}/100 - {row['Tip']}",
        icon=folium.Icon(color=color)
    ).add_to(m)

st_folium(m, width=700, height=450)

st.subheader("📊 Area Safety Report")
st.dataframe(df)

# Safety Checker
st.subheader("🔍 Check Your Route")
area_input = st.text_input("Area ka naam likho (e.g. Saddar):")
if st.button("Check Safety"):
    result = df[df['Area'].str.contains(area_input, case=False)]
    if not result.empty:
        score = result.iloc[0]['Safety_Score']
        if score > 70:
            st.success(f"✅ {area_input} - SAFE ({score}/100) - {result.iloc[0]['Tip']}")
        elif score > 50:
            st.warning(f"⚠️ {area_input} - MODERATE ({score}/100) - {result.iloc[0]['Tip']}")
        else:
            st.error(f"❌ {area_input} - UNSAFE ({score}/100) - {result.iloc[0]['Tip']} | Share live location!")
    else:
        st.info("Area data me nahi hai, add karen?")