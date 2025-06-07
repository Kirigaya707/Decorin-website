import streamlit as st
from PIL import Image
import os

# Page config
st.set_page_config(page_title="Decor In - Interior Designs", layout="wide")

# Logo Header
col1, col2 = st.columns([1, 5])
with col1:
    st.image("images/logo.png", width=180)
with col2:
    st.markdown("""
        <h1 style='margin-bottom: 0;'>
            <span style='color: goldenrod;'>Decor</span> <span style='color: red;'>In</span>
        </h1>
        <h4 style='margin: 0; color: #edd915;'>Interior Design Studio</h4>
        <p style='font-family: cursive; font-size: 0.9rem; color: #555; margin-top: 4px;'>
            <em style='color: red'>The Ultimate Choice</em>
        </p>
    """, unsafe_allow_html=True)



st.markdown("### ")

# Hero Slideshow (Manual Next/Previous)
hero_images = [
    "images/hero1.webp",
    "images/hero2.webp",
    "images/hero3.webp"
]

if "hero_index" not in st.session_state:
    st.session_state.hero_index = 0

col_prev, col_img, col_next = st.columns([1, 6, 1])
with col_prev:
    if st.button("◄ Previous"):
        st.session_state.hero_index = (st.session_state.hero_index - 1) % len(hero_images)

with col_next:
    if st.button("Next ►"):
        st.session_state.hero_index = (st.session_state.hero_index + 1) % len(hero_images)

with col_img:
    st.image(hero_images[st.session_state.hero_index], use_container_width=True)

# Welcome Message
st.markdown("""
    <h1 style='text-align: center; color: #5A5A5A;'>Welcome to Decor In</h1>
    <h3 style='text-align: center; color: #A17F4D;'>Where Creativity Meets Comfort</h3>
    <hr style='border: 1px solid #CCC;' />
""", unsafe_allow_html=True)

# About Section
st.markdown("### About Us")
st.write("""
At **Decor In**, we bring over 20 years of expertise in interior design to create exceptional modular kitchen and furniture solutions tailored to your lifestyle. Our commitment to quality is unmatched — from free physical measurements to detailed drawings, designs, and quotations, we ensure a seamless experience from concept to completion.

We use only premium-grade materials like Century Club Prime Ply (₹1400/sq ft, 30-year warranty) and Century Sainik Ply (₹1300/sq ft, 20-year warranty), offering long-lasting protection against termites and water damage. Our laminates and finishes are sourced from leading brands, and all hardware and accessories are exclusively from Hettich — ensuring functionality meets elegance.
""")

# Services Section
st.markdown("### Our Services")
cols = st.columns(3)
services = [
    ("Residential Interiors", "Elegant and comfortable living spaces designed to your taste."),
    ("Modular Kitchen", "Smart, modern, and productivity-focused working environments."),
    ("Custom Furniture & Decor", "Bespoke pieces to bring a unique personality to your space.")
]
for col, (title, desc) in zip(cols, services):
    col.subheader(title)
    col.write(desc)

# Gallery Section
st.markdown("### Project Gallery")

gallery_folder = "images"
image_files = [
    f for f in os.listdir(gallery_folder)
    if f.lower().endswith(('.png', '.jpg', '.jpeg')) and f.startswith("gallery")
]
image_files.sort()

gallery_cols = st.columns(3)
for idx, img_file in enumerate(image_files):
    img_path = os.path.join(gallery_folder, img_file)
    with gallery_cols[idx % 3]:
        st.image(img_path, use_container_width=True)

# Contact Section
st.markdown("### Contact Us")

st.markdown("""
Need assistance or want to get started?  
📞 **Call us at: 9830072946**  
📧 **Mail us at: decorinkitchen1@gmail.com**

We’d be happy to help you design your dream space!
""")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submitted = st.form_submit_button("Send Message")
    if submitted:
        st.success("Thank you! We'll get back to you soon.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2025 Decor In | Designed with 💛</p>", unsafe_allow_html=True)
