# 쏘카 보험 사기 탐지 머신러닝 프로젝트
![image](https://user-images.githubusercontent.com/72847093/104838734-3476b900-5900-11eb-9428-96d19d7840d8.png)

###### 출처 : 유튜브, ㄷㅋ(뒷쿵) 당했습니다... 먹고살기 팍팍해서? 보험사기 역대 최고를 기록 [온마이크] (https://www.youtube.com/watch?v=hC1V-9eRTVc)

## 개요 

### 주제
- 보험금을 목적으로 한 렌터카 사고 사기 건수가 증가
- 쏘카의 사고 데이터를 통해 Fraud 유저를 사전에 예측 및 예방 

### 진행 순서
1. EDA 
2. Preprocessing 
3. Modulization 
4. Modeling 
5. Model Evaluation

### 일정
기간 : 20/12/28~21/1/18

1주차(12/28 ~ 1/4) - 렌터카 보험 사기 관련 정보 검색, EDA 및 전처리, 간단한 모델링

2주차(1/5 ~ 1/11) - 다양한 전처리 기법들 활용, Hyper Parameter 튜닝을 통한 모델링

3주차(1/12 ~ 1/18) - 모델 평가 성능 정리, 모델링 과정 모듈화 진행, 최종 발표 및 PPT 작성, Github 정리

### 목표 설정
- 1차 목표 : 사전에 전달받은 모델 평가 점수표보다 높은 성적 달성

<img src="https://user-images.githubusercontent.com/71831714/105158927-de00b900-5b51-11eb-89cd-5992f90909cb.jpg" width='800'></img>

- 최종 목표 : 데이터 불균형으로 인한 과적합을 최소화한 모델 구축

### 역할
공통 : 데이터 관찰, 다양한 전처리 및 모델링 조사 및 시도 후 의견 공유

성준 : 분석 과정 모듈화, 작업물 취합 후 최종 노트북 파일 작성

미정, 정려 : 발표 자료 제작

예나 : 발표, 일정 조율 및 회의 내용 정리

### 데이터
- 본 프로젝트는 쏘카로부터 데이터를 제공받아 진행된 프로젝트입니다. 

## 1. EDA

### 1-1. SweetViz

<img src="https://user-images.githubusercontent.com/71831714/104716672-97831700-576b-11eb-80e5-867e81d60082.png" width='800'></img>

### 1-2. Seaborn

#### 1) 불균형한 데이터 분포
- 16,000건의 사고 데이터 중 사기건는 단 41건으로 극심한 데이터 불균형 문제

<img src="https://user-images.githubusercontent.com/71831714/105040354-16968900-5aa5-11eb-90bc-08845657fa94.png" width='400'></img>

#### 2) 컬럼별 분포도 확인

<img src="https://user-images.githubusercontent.com/71831714/104717879-5b50b600-576d-11eb-9417-b8a123987454.png" width='600'></img>

#### 3) 상관관계 히트맵

<img src="https://user-images.githubusercontent.com/71831714/104718021-9652e980-576d-11eb-868f-03c3c7843e5e.png" width='600'></img>

#### 4) 다중공선성

<img src="https://user-images.githubusercontent.com/71831714/104718280-fea1cb00-576d-11eb-9ed3-d63b4d36eec4.png" width='200'></img>

#### 5) 변수 관찰

<img src="https://user-images.githubusercontent.com/71831714/105041042-dedc1100-5aa5-11eb-98f2-f05fed413e7a.png" width='600'></img>

## 2. Preprocessing 

#### 1) 특징 선택(Feature Selection)
- 불필요한 변수 제거

#### 1) 결측치처리 & 이상치 제거 
- 평균값/중앙값/최빈값/KNN imputer 를 활용한 결측치 보간 진행 

#### 2) 원핫인코딩(OneHotEncoding)
- 적용 안 함 
- 모든 카테고리 변수에 적용

#### 3) 스케일링(Scaling)
- StandardScaler
- MinMaxScaler 
- RobustScaler
- Log Scailing 

#### 4) 샘플링(Sampling)
Imbalanced Data 처리를 위한 다양한 샘플링 기법 시도 

<img src="https://user-images.githubusercontent.com/71831714/105041213-0d59ec00-5aa6-11eb-93e4-5d3eaedb94c2.png" width='500'></img>

- OverSampling (RandomOverSampler, SMOTE, ADASYN)
- UnderSampling (RandomUnderSampler, TomekLinks)
- CombinedSampling (SMOTETomek, SMOTEENN)

#### 5) 주성분 분석(PCA)
- 차원 축소 기법을 통한 데이터 노이즈 제거 

## 3. Modulization
 - 코드의 간결성을 위해 모듈화 진행
 
<img src="https://user-images.githubusercontent.com/71831714/105041949-01baf500-5aa7-11eb-98de-67aeb1a13db2.png" width='370'></img>
<img src="https://user-images.githubusercontent.com/71831714/105041951-02ec2200-5aa7-11eb-9732-d91191eb0f26.png" width='400'></img>

## 4. Modeling  
#### 분류기(Classifier)
- LogisticRegression
- DecisionTree
- RandomForest
- LGBM
- LinearSVC 

#### 하이퍼 파라미터 튜닝(Hyper Parameter Tuning)
 - 최적의 하이퍼 파라미터 값을 찾기 위해 교차 검증 사용 
 - 데이터 불균형으로 인해 모델 성능이 불안정하여 2차례 검증 후 성능이 가장 안정적인 모델을 선정

<img src="https://user-images.githubusercontent.com/71831714/105041678-9ffa8b00-5aa6-11eb-9bd0-59cef68e42c6.png" width='500'></img>

## 5. Model Evaluation 
### 모델 성능 평가
- 재현률(Recall)과 정밀도(Accuracy)를 기준으로 성능 평가 진행 

<img src="https://user-images.githubusercontent.com/71831714/105040231-ed75f880-5aa4-11eb-83f9-d94772f72028.png" width='400'></img>
<img src="https://user-images.githubusercontent.com/71831714/105040236-ef3fbc00-5aa4-11eb-9c02-7715142bcffb.png" width='400'></img>

###### 출처 : 패스트 캠퍼스 민형기 강사님 학습자료 020. 모델평가.pdf

### 최고의 모델(Best Model)

- 모델 1

<img src="https://user-images.githubusercontent.com/71831714/105040398-24e4a500-5aa5-11eb-95a7-9a0a2e107fb4.png" width='400'></img>
<img src="https://user-images.githubusercontent.com/71831714/105040406-2615d200-5aa5-11eb-9bbd-9c9e80854f8c.png" width='400'></img>

    acc_type1, b2b, repair_cost, car_part1, car_part2, repair_cnt, insurance_site_aid_YN, police_site_aid_YN 컬럼 제거
    원핫인코딩
    StandardScaling
    RandomUnderSampling
    주성분 분석으로 데이터를 4차원으로 축소
    DecisionTree max_depth를 4로 지정
 
 
 1) validation set과 test set 모두에서 비슷한 성적을 보여줘 안정성이 높음
 2) Fraud 데이터 7건 중 5건을 잡아내 높은 recall 기록
 3) accuracy가 낮다는 한계점 존재

- 모델 2

<img src="https://user-images.githubusercontent.com/71831714/105126964-2e145700-5b23-11eb-9f6a-1958c4c2d7a1.png" width='400'></img>
<img src="https://user-images.githubusercontent.com/71831714/105126966-2f458400-5b23-11eb-8fab-e007a6317366.png" width='400'></img>

    b2b, repair_cost, car_part1, car_part2, repair_cnt, insurance_site_aid_YN, police_site_aid_YN 컬럼 제거
    원핫인코딩
    StandardScaling
    RandomUnderSampling
    주성분 분석으로 데이터를 2차원으로 축소
    DecisionTree max_depth를 6으로 지정
    
 1) validation set과 test set에서의 성능이 다소 차이가 생겨 안정성이 떨어짐
 2) Fraud 데이터 7건 중 7건을 잡아내  recall 기록
 3) accuracy가 0.32로 실전에서 활용하기 힘든 모델
 
 #### Why?
 
  1. 변수 선택(Feature Selection)
 - police_site_aid_YN는 다중 공선성(Multicollinearity)이 26으로 나타나 제거
 - repair_cost, insurance_site_aid_YN는 결측치가 과반수 이상을 차지하여 제거
 - DecisionTree의 Feature importance가 0인 컬럼들을 랜덤하게 제거
 
  2. 표준화(Standardization)
 - 정규 분포를 따르지 않는 데이터에 효과적
 - 이상치(Outlier)의 영향을 적게 받음
 
 <img src="https://user-images.githubusercontent.com/71831714/105138963-f912ff00-5b38-11eb-9935-0e1bdaf1f2f8.png" width='400'></img>
 
 ###### 출처 : ANIRUDDHA BHANDARI, https://www.analyticsvidhya.com/blog/2020/04/feature-scaling-machine-learning-normalization-standardization/
 
  3. Random UnderSampling 
 - 높은 비중의 클래스 데이터를 랜덤하게 제거하는 방식으로 다른 방식들보다 안정적으로 높은 성능을 보임
 
  4. 차원 축소와 하이퍼 파라미터의 값
 - 반복문과 GridSearchCV를 통해 최적의 값 찾기
 
## Conclusion
- Random Under Sampling이 다른 샘플링 기법들보다 좋은 Recall 성능을 보여준 이유에 대해 추가 학습 예정
- 차원을 축소함으로서 속도(약 10% 차이) 뿐만 아니라 성능이 다소 향상됨(약 5% 차이)
- 사용해보지 못 한 다양한 Hyper Parameters(class_weight, max_features, etc...)에 대해 추가 학습 후 적용해보려고 함
