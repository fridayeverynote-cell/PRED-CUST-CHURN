from pathlib import Path
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="위험 고객 관리",
    page_icon="⚠️",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    padding-top: 1.2rem;
    padding-bottom: 2rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

.main-title {
    font-size: 2.2rem;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 0.2rem;
}

.sub-title {
    font-size: 1.05rem;
    color: #64748b;
    margin-bottom: 1.5rem;
}

.card-danger {
    background-color: #fff5f5;
    border: 1px solid #fecaca;
    border-radius: 18px;
    padding: 16px 20px;
}

.card-warning {
    background-color: #fffbeb;
    border: 1px solid #fed7aa;
    border-radius: 18px;
    padding: 16px 20px;
}

.card-success {
    background-color: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-radius: 18px;
    padding: 16px 20px;
}

.card-label {
    font-size: 1rem;
    margin-bottom: 0.3rem;
}

.card-number {
    font-size: 2rem;
    font-weight: 800;
}

.section-card {
    background-color: white;
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    padding: 18px 20px;
    margin-top: 18px;
}
</style>
""", unsafe_allow_html=True)

DATA_PATH = "././data/insurance_policyholder_churn_synthetic.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df["risk_level"] = pd.cut(
        df["churn_probability_true"],
        bins=[-1, 0.4, 0.7, 1.0],
        labels=["저위험", "중위험", "고위험"]
    )
    return df

df = load_data()

st.markdown('<div class="main-title">위험 고객 관리</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">이탈 위험 고객 모니터링</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

high_cnt = int((df["risk_level"] == "고위험").sum())
mid_cnt = int((df["risk_level"] == "중위험").sum())
low_cnt = int((df["risk_level"] == "저위험").sum())

with col1:
    st.markdown(f"""
    <div class="card-danger">
        <div class="card-label" style="color:#dc2626;">고위험</div>
        <div class="card-number" style="color:#b91c1c;">{high_cnt}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card-warning">
        <div class="card-label" style="color:#d97706;">중위험</div>
        <div class="card-number" style="color:#c2410c;">{mid_cnt}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="card-success">
        <div class="card-label" style="color:#16a34a;">저위험</div>
        <div class="card-number" style="color:#15803d;">{low_cnt}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)

search = st.text_input("고객 검색", placeholder="고객 ID 또는 지역 검색")
risk_filter = st.selectbox("위험도", ["모든 위험도", "고위험", "중위험", "저위험"])

filtered = df.copy()

if search:
    keyword = search.strip()
    filtered = filtered[
        filtered["customer_id"].astype(str).str.contains(keyword, case=False, na=False) |
        filtered["region_name"].astype(str).str.contains(keyword, case=False, na=False)
    ]

if risk_filter != "모든 위험도":
    filtered = filtered[filtered["risk_level"] == risk_filter]

show_cols = [
    "customer_id", "age", "policy_type", "current_premium",
    "churn_probability_true", "risk_level"
]

result = filtered[show_cols].copy()
result.columns = ["고객 ID", "나이", "보험 상품", "월 보험료", "이탈 확률", "위험도"]
result["이탈 확률"] = (result["이탈 확률"] * 100).round(1).astype(str) + "%"
result["월 보험료"] = result["월 보험료"].apply(lambda x: f"{int(x):,}원")

st.dataframe(result, use_container_width=True, hide_index=True)
st.markdown('</div>', unsafe_allow_html=True)