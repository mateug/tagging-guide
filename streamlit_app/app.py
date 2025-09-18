
import streamlit as st
from scraper_utils import scrape_url, get_html, get_markdown, get_summary, get_json, get_screenshot
import config

api_key = config.API_KEY

st.set_page_config(page_title=config.PAGE_TITLE, layout=config.PAGE_LAYOUT)
st.title(config.PAGE_TITLE)

url = st.text_input("Introduce la URL a scrapear:")
output_format = st.radio("Formato de salida:", ("HTML", "MARKDOWN", "SUMMARY", "SCREENSHOT"), index=0 if config.DEFAULT_OUTPUT_FORMAT == "HTML" else 1)

if st.button("Scrapear"):
    if url:
        try:
            result = scrape_url(url,api_key)
            if output_format == "HTML":
                st.subheader("Resultado en HTML")
                st.code(get_html(result), language="html")
            elif output_format == "MARKDOWN":
                st.subheader("Resultado en MARKDOWN")
                st.code(get_markdown(result), language="markdown")
            elif output_format == "SUMMARY":
                st.subheader("Resultado en SUMMARY")
                st.text(get_summary(result))
            else:
                st.subheader("Captura de pantalla")
                screenshot = get_screenshot(result)
                if screenshot != "No se encontró screenshot":
                    st.image(screenshot)
                else:
                    st.warning(screenshot)
        except Exception as e:
            st.error(f"Error al scrapear la URL: {e}")
    else:
        st.warning("Por favor, introduce una URL válida.")
