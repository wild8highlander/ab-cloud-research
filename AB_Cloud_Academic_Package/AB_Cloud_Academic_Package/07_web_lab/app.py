"""The Streamlit face of the AB-Cloud web laboratory.

Run: streamlit run app.py
The static index.html is the offline default; this app adds server-side
widgets for those who run Streamlit anyway. Same funnel: the registry.
"""
import json
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "02_data" / "processed" / "research_registry.json"

st.set_page_config(page_title="AB-Cloud Web Lab", page_icon=" ζ ".strip() or "ζ", layout="wide")

@st.cache_data
def load():
    return json.loads(REGISTRY.read_text(encoding="utf-8"))

data = load()
lang = st.sidebar.radio("language", ["en", "ru"], horizontal=True)
T = {
    "en": dict(title="AB-Cloud Research Programme", tag="four levels · one registry · honest boundaries",
               rh="RH status", blocked="blocked (V13 obligation machine)"),
    "ru": dict(title="Программа AB-Cloud", tag="четыре уровня · один реестр · честные границы",
               rh="Статус RH", blocked="заблокирована (машина обязательств V13)"),
}[lang]

st.title(T["title"])
st.caption(T["tag"])
st.warning(f"{T['rh']}: {T['blocked']}" if lang == "en" else f"{T['rh']}: {T['blocked']}")

tabs = st.tabs(["levels", "verdicts", "flagship", "numbers"] if lang == "en"
               else ["уровни", "вердикты", "результаты", "числа"])
with tabs[0]:
    st.dataframe([{"id": l["id"], "name": l.get("name_ru") if lang == "ru" else l["name"],
                   "campaigns": l["campaigns"], "essence": l["essence"]} for l in data["levels"]],
                 use_container_width=True, hide_index=True)
with tabs[1]:
    st.dataframe(data["verdicts"], use_container_width=True, hide_index=True)
with tabs[2]:
    st.dataframe(data["flagship_results"], use_container_width=True, hide_index=True)
with tabs[3]:
    st.dataframe([{ "n": n["n"], "metric": n["metric_ru"] if lang == "ru" else n["metric_en"],
                    "value": n["value"], "campaign": n["campaign"]} for n in data["numbers_registry"]],
                 use_container_width=True, hide_index=True)

st.markdown("---")
st.caption("offline default: index.html · DOI 10.5281/zenodo.21825394 · every number names its campaign")
