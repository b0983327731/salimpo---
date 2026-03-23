import streamlit as st
import time

# --- [10-1] 底層架構：系統全域設定與資源分配 ---
st.set_page_config(
    page_title="NINGPU Voyager v9.5 | 寧埔生態圈",
    page_icon="🌊",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- [10-3] 介面視覺：CSS 視覺降熵與長濱藍主題 ---
st.markdown("""
<style>
    .stApp { background-color: #003366; color: white; }
    h1, h2, h3 { color: #F5D105 !important; font-weight: 800; }
    
    /* 核心 CTA 按鈕改造：零摩擦設計 */
    .stButton>button {
        background-color: #F5D105; color: #000000; font-weight: 900;
        font-size: 18px; border-radius: 8px; border: none; width: 100%;
        padding: 15px 0; transition: all 0.3s;
    }
    .stButton>button:hover { background-color: #D4B404; transform: scale(1.02); }
    
    /* 生態圈資訊卡片降熵設計 */
    .eco-card {
        background-color: #004488; padding: 18px; border-radius: 12px;
        margin-bottom: 15px; border-left: 6px solid #F5D105;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .eco-title { color: #F5D105; font-size: 1.15rem; font-weight: bold; margin-bottom: 5px; }
    .eco-tag { background-color: #F5D105; color: #003366; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; margin-right: 5px; }
    .eco-desc { color: #E0E0E0; font-size: 0
