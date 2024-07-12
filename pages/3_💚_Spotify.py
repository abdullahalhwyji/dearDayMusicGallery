import streamlit as st
import webbrowser
from streamlit_extras.app_logo import add_logo
import streamlit.components.v1 as components

page_bg_img = """
<style>
div.stButton > button:first-child {
    all: unset;
    width: 300px;
    height: 60px;
    font-size: 32px;
    background: transparent;
    border: none;
    position: relative;
    color: #fff;
    cursor: pointer;
    z-index: 1;
    padding: 10px 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    white-space: nowrap;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;

}
div.stButton > button:before, div.stButton > button:after {
    content: '';
    position: absolute;
    bottom: 0;
    right: 0;
    z-index: -99999;
    transition: all .4s;
}

div.stButton > button:before {
    transform: translate(0%, 0%);
    width: 100%;
    height: 100%;
    background: #001a00;
    border-radius: 10px;
}
div.stButton > button:after {
  transform: translate(10px, 10px);
  width: 35px;
  height: 35px;
  background: #ffffff15;
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(5px);
  border-radius: 50px;
}

div.stButton > button:hover::before {
    transform: translate(5%, 20%);
    width: 110%;
    height: 110%;
}


div.stButton > button:hover::after {
    border-radius: 10px;
    transform: translate(0, 0);
    width: 100%;
    height: 100%;
}

div.stButton > button:active::after {
    transition: 0s;
    transform: translate(0, 5%);
}

[data-testid="stAppViewContainer"] {
# background-image: url("https://images.unsplash.com/photo-1581084324492-c8076f130f86?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80");
background-size: cover;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}

[data-testid="stSidebar"] > div:first-child {
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
background : #f0f2f6;
}

[data-testid="stHeader"] {
background: rgba(0,0,0,0);
}

[data-testid="stToolbar"] {
right: 2rem;
}
</style>
"""
add_logo("https://github.com/NebulaTris/go.png?raw=true")

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("DearDay-Spotify 💚")
# st.markdown(''':green[**Note : It is recommended that you scan your face , for Vibescape to groove with you!**]''')
st.sidebar.success("Spotify has been selected as your music player.")
st.sidebar.text("Developed by Alhwyji")

if "run" not in st.session_state:
    # st.write("**Looks like you have skipped the face scan on the homepage and came here, just for music, just choose your vibe manually for Vibescape to groove with you!**")
    option = st.selectbox(
    'What''s your vibe today?',
    ('Happy', 'Sad', 'Angry','Fear','Surprise','Neutral'))
    if option == "Happy":
        st.session_state["emotion"] = "Happy"
    elif option == "Sad":
        st.session_state["emotion"] = "Sad"
    elif option == "Angry":
        st.session_state["emotion"] = "Angry"
    elif option == "Fear":
        st.session_state["emotion"] = "Fear"
    elif option == "Surprise":
        st.session_state["emotion"] = "Surprise"
    else:
        st.session_state["emotion"] = "Neutral"
else:
    st.write("You current emotion is: " , st.session_state["emotion"])

col1, col2 = st.columns(2)

with col1:
    arabic = st.button("عربي")
    if arabic:
        if st.session_state["emotion"] == "Happy":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DX5cO1uP1XC1g?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """, height=600)
        elif st.session_state["emotion"] == "Sad":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/63UTK8xX2ramMrLSoY6Ixj?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """, height=600)
        elif st.session_state["emotion"] == "Angry":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DXaL8gtxi9eun?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>"""
            , height=600)
        elif st.session_state["emotion"] == "Fear":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DX2b68O2EwKjK?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """, height=600)
        elif st.session_state["emotion"] == "Surprise":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DX8uyRZTg1KGr?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """, height=600)
        elif st.session_state["emotion"] == "Neutral":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DX5cO1uP1XC1g?utm_source=generator" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """, height=600)
        else:
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1E4mS880sTV9QE?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """, height=180)
            
          
    indonesian = st.button("Bahasa Indonesia")
    if indonesian:
        if st.session_state["emotion"] == "Happy":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/716rg48FuucgfTlJxrcgly?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """, height=600)
        elif st.session_state["emotion"] == "Sad":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/24fxepcPPddsy2EGxIZnAi?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """, height=600)
        elif st.session_state["emotion"] == "Angry":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/1UHxnfhTQTkyKqvDboxpbQ?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """, height=600)
        elif st.session_state["emotion"] == "Fear":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/1bn6O6UpKiAV8veD4aCY9A?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """, height=600)
        elif st.session_state["emotion"] == "Surprise":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/1bn6O6UpKiAV8veD4aCY9A?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """, height=600)
        elif st.session_state["emotion"] == "Neutral":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZEVXbObFQZ3JLcXt?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """, height=600)
        else:
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZEVXbObFQZ3JLcXt?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """, height=600)
  
   
with col2:
   english = st.button("English")
   if english:
        if st.session_state["emotion"] == "Happy":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DXdPec7aLTmlC?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Sad":
           components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DX7qK8ma5wgG1?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Angry":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1EIgNZCaOGb0Mi?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Fear":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DWYWddJiPzbvb?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Surprise":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1EIfIhwClkyzKs?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Neutral":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZEVXbMDoHDwVN2tF?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write;  fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        else:
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/60eEo5VdhekyGJKTjK2xSV?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
            
   
   thai = st.button("ภาษาไทย")
   if thai:
        if st.session_state["emotion"] == "Happy":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DWZRLdKC8qik7?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """, height=600)
        elif st.session_state["emotion"] == "Sad":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/0yM5NWrEKI3heSu4zaj8qP?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """, height=600)
        elif st.session_state["emotion"] == "Angry":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/2dWTBjgmTMkGFOqfE8rKDR?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """, height=600)
        elif st.session_state["emotion"] == "Fear":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/3AIze7NsHjmFnJykAUgrKD?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """, height=600)
        elif st.session_state["emotion"] == "Surprise":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DXbsIkp5zMVV2?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """, height=600)
        elif st.session_state["emotion"] == "Neutral":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/2mNHLTh5NWhTRHUy6f6p77?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """, height=600)
        else:
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DWVstKlOmd8OR?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """, height=600)