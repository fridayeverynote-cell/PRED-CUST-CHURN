from pathlib import Path
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="고객 이탈 예측",
    page_icon="📉",
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

.section-card {
    background-color: white;
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    padding: 20px 22px;
}

.section-title {
    font-size: 1.8rem;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

DATA_PATH = "././data/insurance_policyholder_churn_synthetic.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    return df

df = load_data()

policy_options = sorted(df["policy_type"].dropna().unique().tolist())
gender_options = sorted(df["gender"].dropna().unique().tolist()) if "gender" in df.columns else ["Male", "Female"]
region_options = sorted(df["region_name"].dropna().unique().tolist())

st.markdown('<div class="main-title">고객 이탈 예측</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">AI 기반 고객 이탈 예측 분석</div>', unsafe_allow_html=True)

left, right = st.columns([1.1, 1])

with left:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">고객 정보 입력</div>', unsafe_allow_html=True)

    with st.form("predict_form"):
        age = st.number_input("나이", min_value=18, max_value=100, value=35)
        gender = st.selectbox("성별", gender_options)
        policy_type = st.selectbox("보험 상품", policy_options)
        premium = st.number_input("월 보험료 (원)", min_value=0, value=150000, step=10000)
        tenure = st.number_input("가입 기간 (개월)", min_value=1, max_value=600, value=24)
        region = st.selectbox("지역", region_options)

        submitted = st.form_submit_button("예측하기", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">예측 결과</div>', unsafe_allow_html=True)

    if submitted:
        # 임시 규칙 기반 점수
        score = 0.15

        if age >= 55:
            score += 0.15
        elif age <= 29:
            score += 0.08

        if premium >= 200000:
            score += 0.18
        elif premium >= 150000:
            score += 0.10

        if tenure < 12:
            score += 0.18
        elif tenure < 24:
            score += 0.10

        if policy_type in ["자동차보험", "건강보험"]:
            score += 0.10

        score = min(score, 0.95)

        if score >= 0.7:
            risk = "고위험"
            st.error(f"이탈 확률: {score*100:.1f}%")
            st.error(f"위험도: {risk}")
        elif score >= 0.4:
            risk = "중위험"
            st.warning(f"이탈 확률: {score*100:.1f}%")
            st.warning(f"위험도: {risk}")
        else:
            risk = "저위험"
            st.success(f"이탈 확률: {score*100:.1f}%")
            st.success(f"위험도: {risk}")

        result_df = pd.DataFrame({
            "항목": ["나이", "성별", "보험 상품", "월 보험료", "가입 기간", "지역"],
            "값": [age, gender, policy_type, f"{premium:,}원", f"{tenure}개월", region]
        })
        st.dataframe(result_df, use_container_width=True, hide_index=True)
    else:
        st.info("좌측 양식을 작성하고 예측 버튼을 클릭하세요.")

    st.markdown('</div>', unsafe_allow_html=True)