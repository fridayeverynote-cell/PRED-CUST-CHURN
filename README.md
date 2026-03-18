# ↪ RETURNS
## 머신러닝 기반 보험 가입 고객 이탈 예측 및 유지 전략 제안 프로젝트

## 📑 목차 (Table of Contents)
1. [📌 프로젝트 개요](#1-프로젝트-개요)
2. [🖐🏻 팀 소개](#2-팀-소개)
3. [🛠 기술 스택](#3-기술-스택)
4. [📊 데이터 분석 및 전처리](#4-데이터-분석-및-전처리)
5. [🧠 모델링 및 평가](#5-모델링-및-평가)
6. [📈 주요 기능 및 화면](#6-주요-기능-및-화면)
7. [📁 프로젝트 구조](#7-프로젝트-구조)

## 1. 📌 프로젝트 개요

📋 서비스 배경

- 보험 산업에서 신규 고객 유치 비용은 기존 고객 유지 비용보다 약 5~7배 더 높습니다.\
Team RETURNS는 보험사의 유지율(Retention Rate)을 극대화하기 위해 데이터 기반의 이탈 예측 솔루션을 제안합니다.

🎯 핵심 목표
- B2B 솔루션: 보험사가 보유한 방대한 고객 데이터를 활용하여, 해지 가능성이 높은 고객을 사전에 식별합니다.
- 비즈니스 가치: 신규 고객 유치보다 효율적인 **기존 고객 유지(Retention)** 를 통해 보험사의 운영 비용을 절감하고 손해율을 관리합니다.
- 데이터 기반 의사결정: 단순 감이 아닌, 머신러닝 모델이 산출한 이탈 확률을 바탕으로 마케팅 자원을 집중 투입합니다.

💡 기대 효과
- 이탈률 감소: 데이터 기반의 타겟팅을 통한 효율적인 고객 관리
- LTV(고객 생애 가치) 증대: 장기 가입 고객 확보를 통한 보험사 수익성 개선

## 2. 🖐🏻 팀소개
##  Team RETURNS
<table align="center">
  <tr>
    <td align="center" width="120">
      <img src="./images/readme/kys.webp" style="width: 100px; height: 120px; min-width: 100px; min-height: 120px; object-fit: cover;">
    </td>
    <td align="center" width="120">
      <img src="./images/readme/pej.jpeg" style="width: 100px; height: 120px; min-width: 100px; min-height: 120px; object-fit: cover;">
    </td>
    <td align="center" width="120">
      <img src="./images/readme/boo.webp" style="width: 100px; height: 120px; min-width: 100px; min-height: 120px; object-fit: cover;">
    </td>
    <td align="center" width="120">
      <img src="./images/readme/lsh.jpeg" style="width: 100px; height: 120px; min-width: 100px; min-height: 120px; object-fit: cover;">
    </td>
    <td align="center" width="120">
      <img src="./images/readme/hh.jpeg" style="width: 100px; height: 120px; min-width: 100px; min-height: 120px; object-fit: cover;">
    </td>
    <td align="center" width="120">
      <img src="./images/readme/dori.jpg" style="width: 100px; height: 120px; min-width: 100px; min-height: 120px; object-fit: cover;">
    </td>
  </tr>
  <tr>
    <td align="center"><b>김이선</b></td>
    <td align="center"><b>박은지</b></td>
    <td align="center"><b>박기은</b></td>
    <td align="center"><b>이선호</b></td>
    <td align="center"><b>위희찬</b></td>
    <td align="center"><b>홍지윤</b></td>
  </tr>
  <tr>
    <td align="center">FullStack</td>
    <td align="center">DB</td>
    <td align="center">FullStack</td>
    <td align="center">PM</td>
    <td align="center">FullStack</td>
    <td align="center">FullStack</td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/kysuniv-cyber"><img src="https://img.shields.io/badge/kysuniv--cyber-181717?style=for-the-badge&logo=github&logoColor=white"></a></td>
    <td align="center"><a href="https://github.com/lo1f0306"><img src="https://img.shields.io/badge/lo1f0306-181717?style=for-the-badge&logo=github&logoColor=white"></a></td>
    <td align="center"><a href="https://github.com/gieun-Park"><img src="https://img.shields.io/badge/gieun--Park-181717?style=for-the-badge&logo=github&logoColor=white"></a></td>
    <td align="center"><a href="https://github.com/fridayeverynote-cell"><img src="https://img.shields.io/badge/fridayeverynote--cell-181717?style=for-the-badge&logo=github&logoColor=white"></a></td>
    <td align="center"><a href="https://github.com/dnlgmlcks"><img src="https://img.shields.io/badge/dnlgmlcks-181717?style=for-the-badge&logo=github&logoColor=white"></a></td>
    <td align="center"><a href="https://github.com/jyh-skn"><img src="https://img.shields.io/badge/jyh--skn-181717?style=for-the-badge&logo=github&logoColor=white"></a></td>
  </tr>
</table>


## 3. 🛠 기술스택
- Language & Analysis: <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white"> <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"> <img src="https://img.shields.io/badge/Matplotlib-ffffff?style=for-the-badge&logo=matplotlib&logoColor=black"> <img src="https://img.shields.io/badge/Seaborn-4479A1?style=for-the-badge&logo=python&logoColor=white">


- Machine Learning: <img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white">
  - Core Model: HistGradientBoostingClassifier 
  

- Service: - **Service:** <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"> <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"> <img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white">

## 4. 📊 데이터 분석 및 전처리
📊 데이터셋 구성 (Dataset Overview)\
본 프로젝트는 보험 고객의 행동 데이터를 분석하여 이탈 확률을 예측하기 위해 Parquet 형식의 고성능 데이터셋을 활용했습니다.

- 데이터 규모: 약 40여 개의 피처(Features)로 구성된 고객별 보험 유지/청구 이력 데이터.
- 파일 형식: 대용량 데이터의 입출력 속도 향상 및 데이터 타입 보존을 위해 Apache Parquet 채택.

| 영역 | 주요 항목 (Features) | 비즈니스 의미 |
|---|---|---|
| 고객 프로필 | `region_name`, `age_band`, `tenure` | 지역별 / 연령대별 / 가입 기간별 고객 성향 파악 |
| 보험 및 청구 | `current_premium`, `num_claims_12m` | 현재 납입료 수준 및 최근 1년 내 서비스 이용 빈도 측정 |
| 리스크 지표 | `complaint_flag`, `late_payment_count` | 민원 발생 및 보험료 연체 등 직접적인 이탈 징후 포착 |

🛠️ 데이터 전처리 및 분석 (EDA & Processing)\
모델 성능 최적화를 위해 다음과 같은 분석과 가공 과정을 거쳤습니다.

1. 중복성 제거 (Feature Selection):
- total_payout_amount_12m와 total_claim_amount_12m처럼 상관관계가 1.0인 중복 지표를 정리하여 모델 복잡도 감소.

2. 타겟 지표 생성:
- 단순 이탈 여부(0, 1) 외에 모델이 산출한 churn_probability(이탈 확률)를 기반으로 위험 등급(Risk Tier) 도출 로직 설계.

3. 데이터 정제:
- 학습에 불필요한 고유 식별값(customer_id) 및 기준일(as_of_date)을 제거하여 모델의 일반화 성능 향상.

4. 범주형 변수 처리:
- region_name(지역명), policy_type(상품 유형) 등급의 텍스트 데이터를 머신러닝 모델이 이해할 수 있도록 인코딩 수행.
## 5. 🧠 모델링 및 평가

🏗️ 모델 구성 및 전략

- 사용 모델: HistGradientBoostingClassifier

- 모델 특성: * 정형 데이터 학습에 최적화된 히스토그램 기반 알고리즘을 통해 수만 건의 데이터를 고속으로 처리.

  - Scikit-learn 파이프라인과 ColumnTransformer를 활용하여 전처리부터 예측까지의 과정을 모듈화.

  - 버전 호환성 패치: Persisted Imputer 패치를 통해 sklearn 1.7.x와 1.8.x 간의 런타임 호환성 확보.

📈 모델 성능 결과\
테스트 데이터셋을 기준으로 산출된 주요 평가지표는 다음과 같습니다.

| Metric    | Value | Description                       |
| --------- | ----- | --------------------------------- |
| Accuracy  | 0.572 | 전체 예측 중 정답을 맞춘 비율                 |
| Precision | 0.406 | 이탈이라고 예측한 고객 중 실제 이탈자의 비율         |
| Recall    | 0.901 | 실제 이탈자 중 모델이 찾아낸 비율 (핵심 성과 지표)    |
| F1-Score  | 0.559 | Precision과 Recall의 조화 평균          |
| ROC-AUC   | 0.790 | 이탈 고객과 유지 고객을 구분하는 모델의 전반적인 분류 성능 |

### 🔍 Key Insight

* 모델은 **Recall(0.901)** 을 높게 유지하도록 설계되었습니다.
* 이는 **실제 이탈 고객을 최대한 많이 탐지하는 것**을 목표로 한 설정입니다.
* 고객 이탈 예측 문제에서는 **이탈자를 놓치는 것(False Negative)** 이 더 큰 비용을 초래할 수 있기 때문에 Recall이 중요한 지표입니다.


## 6. 📈 주요 기능 및 화면
1. 홈
![img.png](images/readme/img.png)
  - 영업팀에서 한 눈에 전체 고객과 대응이 필요한 고객을 확인할 수 있게 만들었습니다. 즉시 대응 고객 수는 숫자로, 관리 고객 수 (즉시 대응 + 고위험)은 퍼센티지로 볼 수 있게 만들었습니다. 상품별 고객 이탈률 분포도 만들어서 어떤 부서에서 이탈률에 대한 대응이 필요한지 한눈에 볼 수 있게 했습니다. 연령대 별로 만든 것은 마케팅 타겟을 용이하게 만들기 위함입니다.
3. 모델성능 대시보드
- 핵심 성능 지표
![img_1.png](images/readme/img_1.png)
  - 재현율이 가장 중요한 지표로 이탈 고객을 놓치지 않는데 집중했습니다. 그 외, ROC-AUC와 F1 스코어의 지표도 확인 가능하게 만들었습니다.
- 예측 및 분류 상세 분석
![img_2.png](images/readme/img_2.png)
  - 현재 고객의 이탈 위험도를 파이로 한 눈에 확인할 수 있게 만들었습니다. 또한, 모델이 이탈하는 고객을 잡아내는데 어느 정도 성능을 보이는지, 그리고 실제 이탈한 고객을 얼마나 놓쳤는지 confusion matrix를 통해 확인할 수 있게 만들었습니다.
- 모델판단근거 분석
![img_3.png](images/readme/img_3.png)
  - 모델의 핵심인 Threshold를 어떻게 구했는지 시각화하여 한눈에 볼 수 있게 만들었습니다. 또한, 가장 상관계수가 높은 변수 두 가지를 시각화하여 계수에 따른 이탈률을 볼 수 있도록 만들었습니다.
3. 예측 / 시뮬레이션
- 자동분석 레포트
![img_4.png](images/readme/img_4.png)
  - 이탈 예측 확률이 25% 미만이면 안정 고객, 25% 이상이면 관찰, 40% 이상이면 고위험, 60% 이상이면 즉시 대응으로 분류했습니다. 고객 수를 한눈에 볼 수 있도록 만들어서 영업팀에게 현재 이탈 가능성이 높은 고객의 상황을 파악할 수 있게 만들었습니다. 대략적으로나마 영업팀의 KPI를 추적하는데 도움이 될 수 있을 거라고 생각합니다. 또한, 가장 높은 이탈률을 가진 고객 샘플 30개를 볼 수 있게 하여 이탈 사유까지 확인할 수 있게 만들었습니다.
- 고객이탈예측
![img_5.png](images/readme/img_5.png)
  - 고객의 정보(나이, 보험료, 연체 횟수 등)을 입력하면 모델을 사용하여 이탈 확률과 위험등급을 알 수 있습니다. 입력하지 못한 데이터는 평균치나 중간값으로 대체하였습니다. 또한, 해석 포인트를 나타내 어떤 사유로 이탈 위험이 높은지, 어떤 특성이 있는지 볼 수 있게 하였습니다.
- 위험고객관리
![img_6.png](images/readme/img_6.png)
  - 전반적인 위험도 별 고객 수를 확인할 수 있게 만들었습니다. 고객 상세 리스트에서는 위험등급 등에 따른 필터링이 가능하게 만들었고, 모든 컬럼 기준으로 정렬이 가능합니다. 이탈 확률을 숫자 및 바/색깔로 확인할 수 있게 만들어 파악하기 용이합니다. 이탈 확률에 대한 사유도 나와있어서 영업팀에서 대응하기 편리합니다.
- 시뮬레이션
![img_7.png](images/readme/img_7.png)
  - 시뮬레이션 시나리오 별로 변수를 조절하면 그에 대한 결과가 나옵니다. 변수는 회사에서 조절할 수 있거나 외부 상황에 따라 변동하는 변수를 골랐습니다. 고객당 유지 가치는 현재 데이터 셋의 보험료 평균치입니다. 데이터가 변동 (고객 추가 등)에 따라 유연하게 조절됩니다.
  - 예시: 보험률 인상폭 완화(회사에서 조절 가능), 고연체 고객 정상화(외부 정책(정부 구제) 확장하는 경우 등), 급격한 보험료 인상 고객 완화(회사에서 조절 가능), 보장 축소 고객 감소(회사에서 조절 가능)
  - 시뮬레이션 결과: 이탈률 개선, 평균 확률 감소, 방어 고객 수, 예상 방어 매출 등을 확인할 수 있습니다.
![img_8.png](images/readme/img_8.png)
  - 정책별 기여도를 확인하여 어떤 정책이 가장 효과가 좋은지 확인할 수 있습니다. 다만, 시너지 효과 등이 있을 수도 있어서 정책의 중요도에 대한 순위 파악 정도로 활용할 수 있습니다.
![img_9.png](images/readme/img_9.png)
  - 시각화하여 평균 이탈 확률과 예상 이탈 확률의 변화를 파악할 수 있게 만들었습니다.

## 7. 📂 프로젝트 구조 (Project Structure)

```text
PRED-CUST-CHURN/
├── data/                               # 데이터 폴더
├── analysis/                           # 개별 가설 분석 폴더
├── src/                                # 공통 모듈 (팀원 공유용)
│   └── preprocess.py                   # 데이터 로드 및 전처리 클래스
├── pages/                              # Streamlit 웹 어플리케이션
│   ├── churn_predictor.py              # 이탈 예측 화면
│   ├── entry.py                        # 홈 대시보드 화면
│   ├── model_info.py                   # 모델성능 대시보드 화면
│   ├── model_monitor.py                # 데이터 자동분석 레포트 화면
│   ├── predicted_churn_watchlist.py    # 모델기반 고객 이탈 예측 분석 화면
│   ├── risk_watchlist.py               # 이탈 확률이 높은 고객 리스트 화면
│   └── simulation_kys.py               # 비즈니스 시뮬레이션 화면
├── model/                              # 학습된 모델 저장 폴더
├── requirements.txt                    # 필요 라이브러리 목록
└── app.py                              # 실행 streamlit
```

## 8. 🫱🏻‍🫲🏻팀원 회고

<table>
  <thead>
    <tr>
      <th>대상자</th>
      <th>작성자</th>
      <th>회고 내용</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="5">김이선</td>
      <td>박기은</td>
      <td>스트림릿의 전체 구조를 기획하고 화면 구성을 기반으로 하여 팀원들이 효율적으로 개발할 수 있도록 큰 역할을 해주셨습니다.</td>
    </tr>
    <tr>
      <td>박은지</td>
      <td>단순한 모델 구현에 그치지 않고, 이를 직접 체감할 수 있는 시뮬레이션 페이지까지 구축하여 프로젝트의 완성도를 한 단계 격상시켜 주셨습니다. 실무적인 활용도까지 고려하는 넓은 시야가 팀에 큰 힘이 되었습니다.</td>
    </tr>
    <tr>
      <td>위희찬</td>
      <td>모델을 활용한 스트림릿 페이지를 기획, 구성하시고 페이지에 웹 기능 개발을 주로 하셨습니다.</td>
    </tr>
    <tr>
      <td>이선호</td>
      <td>웹페이이지 내용이 바뀔때마다 수정하시고 디자인적 요소까지 고민하셔서 훌륭한 결과물이 나올 수 있었습니다. 마지막까지 고생 많으셨습니다.  </td>
    </tr>
    <tr>
      <td>홍지윤</td>
      <td>프론트엔드 면에서 스트림릿 화면 제작 및 피그마를 통한 화면 디자인, 백엔드 측면에서 모델의 성능을 높이기 위해서 파생변수나 다양한 모델을 학습 성능평가 하시는 등 프론트엔드와 백엔드를 망라하고 다양한 영역에서 고생해주셨습니다.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>대상자</th>
      <th>작성자</th>
      <th>회고 내용</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="5">박기은</td>
      <td>김이선</td>
      <td></td>
    </tr>
    <tr>
      <td>박은지</td>
      <td>비전공 분야(디자인)임에도 불구하고 웹사이트의 UI/UX 구축과 전반적인 디자인 과정에서 가장 핵심적인 역할을 수행해 주셨습니다. 기술적 구현을 넘어 사용자 친화적인 결과물을 만들어내는 데 결정적인 기여를 하신 분입니다.</td>
    </tr>
    <tr>
      <td>위희찬</td>
      <td>웹페이지의 디자인적인 부분을 색감부터 여러 부분을 조정하셨고 웹 기능 개발을 주로하셨습니다. </td>
    </tr>
    <tr>
      <td>이선호</td>
      <td>소리없이 강하신 분입니다. 개발 전 과정에서  실무를 담당해 주셔서 든든했습니다.  </td>
    </tr>
    <tr>
      <td>홍지윤</td>
      <td>스트림릿 화면의 초기 기획과 사용자 UI 및 디자인 영역까지 고생해주셨습니다. 모델 성능 향상에도 계속 공을 들여주셨고, 모델 선택 과정에서도 강력한 동기부여를 해주셨습니다. 또한,  README나 회의록 및 노션 정리에도 항상 신경을 써주셨습니다.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>대상자</th>
      <th>작성자</th>
      <th>회고 내용</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="5">박은지</td>
      <td>김이선</td>
      <td></td>
    </tr>
    <tr>
      <td>박기은</td>
      <td>프로젝트에 적합한 데이터셋 선정에 기여하였고, 컨디션이 좋지 않은 와중에도 발표 준비와 자료 정리에 힘써주셨습니다.</td>
    </tr>
    <tr>
      <td>위희찬</td>
      <td>주제를 정할 떄 경험을 살려 좋은 주제를 하게 되었고, 프로젝트를 자세히 공부하셔서 발표를 결과물보다 잘하신것 같습니다.</td>
    </tr>
    <tr>
      <td>이선호</td>
      <td>실무경험을 살려서 프로젝트의 방향성을 잘 고려해 주신 것 같습니다. 마지막 발표도 열정적으로 해주셔서 감사했습니다.</td>
    </tr>
    <tr>
      <td>홍지윤</td>
      <td>프로젝트 주제선정부터 프론트까지 도메인에 대한 지식을 살려 비즈니스적인 인사이트를 제공해주셨습니다. 프로젝트에 대한 애정을 담뿍 담은 발표 덕분에 좋은 마무리가 된 것 같아 감사했습니다.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>대상자</th>
      <th>작성자</th>
      <th>회고 내용</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="5">위희찬</td>
      <td>김이선</td>
      <td></td>
    </tr>
    <tr>
      <td>박기은</td>
      <td>프로젝트에서 가장 중요한 머신러닝 모델 학습과 성능 최적화를 담당하여 예측 결과 완성도를 높이는 데 기여하셨습니다.</td>
    </tr>
    <tr>
      <td>박은지</td>
      <td>프로젝트의 핵심인 ML 모델링을 전담하여 책임감 있게 이끌어 주셨습니다. 특히 다양한 모델 비교와 세밀한 하이퍼파라미터 및 임계값(Threshold) 조정 등 집요한 최적화 과정을 통해 최선의 성능을 이끌어내신 점이 인상적이었습니다.</td>
    </tr>
    <tr>
      <td>이선호</td>
      <td>모델 최적화 뿐만 아니라 배포까지 전공자로서 개발 전 과정에 참여하셔서 결과물을 만들어 내는 모습이 좋았습니다. 감사드립니다. </td>
    </tr>
    <tr>
      <td>홍지윤</td>
      <td>프로젝트에서 가장 중요한 머신러닝을 최종적으로 선정 및 학습시키셨고, 머신러닝 학습에 대한 결과나 성과도 잘 정리해주셨습니다. 또, 학습이 된 머신러닝을 사용자가 사용하기 위한 화면에 연결하기 위한 모든 작업을 도맡아 해주셨습니다. </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>대상자</th>
      <th>작성자</th>
      <th>회고 내용</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="5">이선호</td>
      <td>김이선</td>
      <td></td>
    </tr>
    <tr>
      <td>박기은</td>
      <td>프로젝트 과정에서 다양한 아이디어를 제시해 방향 설정에 큰 도움을 주셨습니다.</td>
    </tr>
    <tr>
      <td>박은지</td>
      <td>팀 프로젝트 진행 과정에서 전반적인 분위기를 유연하게 만들어 주셨으며, 팀원들의 의견을 경청하고 조율하는 서포터 역할을 충실히 해주셨습니다.</td>
    </tr>
    <tr>
      <td>위희찬</td>
      <td>프로젝트 중간 중간 개발의 방향성을 잘 잡아주셧습니다.</td>
    </tr>
    <tr>
      <td>홍지윤</td>
      <td>가설설정부터 모델학습, 화면 구성에 이르기까지 생각지도 못했던 다양한 시각과 포인트를 집어주시고 많은 발전방향을 제안해주셨습니다. 팀 안에서 좋은 분위기를 유지할 수 있도록 팀원들을 챙기시며 노력해주셨습니다.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>대상자</th>
      <th>작성자</th>
      <th>회고 내용</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="5">홍지윤</td>
      <td>김이선</td>
      <td></td>
    </tr>
    <tr>
      <td>박기은</td>
      <td>프로젝트 구조를 설계하여 전체 개발 흐름을 정리하고, 효율적인 작업 기반을 마련해 협업이 원활히 진행될 수 있었습니다.</td>
    </tr>
    <tr>
      <td>박은지</td>
      <td>모델링부터 웹 구축까지 프로젝트의 전 과정을 세심하게 챙기며 완성도를 높여주셨습니다. 특히 데이터 전처리 함수 제작 등 효율적인 작업 환경을 마련하여 팀원 전체의 생산성을 높이는 데 중추적인 역할을 해주셨습니다.</td>
    </tr>
    <tr>
      <td>위희찬</td>
      <td>팀의 리더 역할을 하셨습니다, 팀원간 의견조율과 프로젝트 환경을 구성, 수정 하시고 웹페이지 개발을 해주셨습니다. </td>
    </tr>
    <tr>
      <td>이선호</td>
      <td>리더로 부족한 사람까지 이끌어 주시면서 자세히 설명해 주시는 부분이 너무 감사했습니다. 작은 의견도 놓치지 않고 문제해결에 도움을 주려는 모습이 좋았습니다. 보여지지 않는 곳까지 신경쓰시면서 팀을 이끌어 주셨습니다. </td>
    </tr>
  </tbody>
</table>
