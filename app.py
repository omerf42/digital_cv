from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Ömer Eroglu"
PAGE_ICON = ":wave:"
NAME = "Ömer Eroglu"
DESCRIPTION = """
Welkom op mijn digitale, interactieve CV. Ik ben Ömer Eroglu, 28 jaar en woon in Zaandam. Ik hou van avontuurlijk
reizen in het verre zuidoosten. Verder vind ik het leuk om te padellen en te klimmen.
"""
EMAIL = "omerfaruk_eroglu@hotmail.com"
SOCIAL_MEDIA = {
#    "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://www.linkedin.com/in/%C3%B6mer-e-291660106/",
#    "GitHub": "https://github.com",
#    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Machine Learning modellen getraind om te voorspellen of een transactie frauduleus is.": "",
    "🏆 Heuristieken geprogrammeerd voor het oplossen van het proteïne vouw probleem": "",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
   cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Profiel")
st.write(
    """
- ✔️ Leergierig
- ✔️ Sterke hands-on ervaring en kennis in Python
- ✔️ Uitstekende teamspeler met een sterk gevoel voor initiatief bij taken
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, C, SQL
- 📊 Data Visulization: Matplotlib, Pandas, Seaborn
"""
)


# --- WORK & UNIVERSITY HISTORY ---
st.write('\n')
st.subheader("Work & University History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Wiskunde met programmeerrichting | Universiteit van Amsterdam**")
st.write("09/2022 - heden")
st.write(
    """
- ► Minor Programmeren
- ► Minor Artificial Intelligence
"""
)

# --- JOB 1
st.write("🚧", "**KPN | Verkoopadviseur**")
st.write("08/2018 - heden")
st.write(
    """
- ► Verantwoordelijk voor het adviseren aan klanten over KPN producten
- ► Verantwoordelijk geweest voor het communiceren van de doelen aan het team
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Vrijwilliger | Bijles wiskunde**")
st.write("05 / 2022 - 09 / 2023")
st.write(
    """
- ► Bijles wiskunde gegeven aan middelbare scholieren
"""
)



# --- Projects ---
st.write('\n')
st.subheader("Eigen projecten")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
    

# --- Referenties ---
st.write('\n')
st.subheader("Referenties")
st.write("---")
st.write("Massih Sakhi, clustermanager KPN, 0613885738")
st.write("Doesjent Mahabiersing, clustermanager KPN, 0630688799")