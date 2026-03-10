from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="보험 이탈 예측",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================
# 공통 스타일
# =============================
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

.card {
    background-color: white;
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    padding: 20px 22px;
    box-shadow: 0 1px 2px rgba(0,0,0,0.04);
    min-height: 120px;
}

.card-title {
    font-size: 1rem;
    color: #475569;
    margin-bottom: 0.6rem;
}

.card-value {
    font-size: 2.2rem;
    font-weight: 800;
    color: #0f172a;
}

.section-card {
    background-color: white;
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    padding: 18px 20px;
    margin-top: 12px;
}

.section-title {
    font-size: 1.6rem;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 0.25rem;
}

.small-muted {
    font-size: 0.95rem;
    color: #64748b;
}

div[data-testid="stSidebarNav"] {
    padding-top: 1rem;
}

div[data-testid="stSidebarNav"]::before {
    content: "보험 이탈 예측\\A고객 관리 시스템";
    white-space: pre-line;
    display: block;
    font-size: 2rem;
    line-height: 1.5;
    font-weight: 800;
    color: #2563eb;
    margin-bottom: 1.2rem;
    padding-left: 0.2rem;
}

div[data-testid="stSidebarNav"] ul {
    margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

# =============================
# 데이터 로드
# =============================
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_PATH = DATA_DIR / "insurance_policyholder_churn_synthetic.csv"
DICT_PATH = DATA_DIR / "insurance_policyholder_churn_data_dictionary.csv"


@st.cache_data
def load_data():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"데이터 파일이 없습니다: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    data_dict = None
    if DICT_PATH.exists():
        data_dict = pd.read_csv(DICT_PATH)

    df["as_of_date"] = pd.to_datetime(df["as_of_date"], errors="coerce")

    df["risk_level"] = pd.cut(
        df["churn_probability_true"],
        bins=[-1, 0.4, 0.7, 1.0],
        labels=["저위험", "중위험", "고위험"]
    )

    return df, data_dict


df, data_dict = load_data()

# =============================
# 홈 화면
# =============================
total_customers = len(df)
churn_count = int(df["churn_flag"].sum())
churn_rate = (churn_count / total_customers) * 100 if total_customers > 0 else 0
high_risk_count = int((df["risk_level"] == "고위험").sum())

st.markdown('<div class="main-title">대시보드</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">고객 이탈 예측 분석 현황</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">전체 고객 수</div>
        <div class="card-value">{total_customers:,}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">이탈률</div>
        <div class="card-value">{churn_rate:.1f}%</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">고위험 고객 수</div>
        <div class="card-value">{high_risk_count:,}</div>
    </div>
    """, unsafe_allow_html=True)

left, right = st.columns(2)

with left:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">연령대별 이탈률</div>', unsafe_allow_html=True)

    age_churn = (
        df.groupby("age_band")["churn_flag"]
        .mean()
        .mul(100)
        .round(2)
        .reset_index()
        .rename(columns={"age_band": "연령대", "churn_flag": "이탈률"})
    )
    st.bar_chart(age_churn.set_index("연령대"))
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">상품별 분포</div>', unsafe_allow_html=True)

    product_counts = df["policy_type"].value_counts().reset_index()
    product_counts.columns = ["상품", "고객수"]

    fig = px.pie(
        product_counts,
        names="상품",
        values="고객수",
        hole=0.35
    )
    fig.update_layout(margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("### 데이터 미리보기")
preview_cols = [
    "customer_id", "as_of_date", "region_name", "age", "age_band",
    "policy_type", "current_premium", "churn_flag",
    "churn_probability_true", "risk_level"
]
st.dataframe(df[preview_cols].head(20), use_container_width=True)

if data_dict is not None:
    with st.expander("컬럼 설명 보기"):
        st.dataframe(data_dict, use_container_width=True)