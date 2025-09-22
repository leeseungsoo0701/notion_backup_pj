---
created_date: 2025-08-08
id: 2492dc3e-f514-8063-af78-ddbf5e54fc76
url: https://www.notion.so/KDT-Story-applicants-sales_leads-FK-2492dc3ef5148063af78ddbf5e54fc76
perf_flag: yes
importance: 5
summary_5lines:
  - 담당 세일즈 매니저의 성과를 퍼널별·기간별로 확인하려는 세일즈 리더
  - 가설: 문제 정의를 해결할 해결책은 무엇인지
  - 실험 결과 요약 (Result Summary)
  - 실험 설계 관점에서 얻은 교훈과 고객 행동 인사이트를 간단히 요약하고 다음과 같이 연결합니다
  - 이를 통해 세일즈 매니저·배정일·회신 여부를 데이터 마트에 반영하여 성과 분석의 정확도가 높아진다.
---

# 2025-08-08_[KDT-Story] applicants–sales_leads FK 연동

| Property | Value |
| --- | --- |
| created_date | 2025-08-08 |
| id | 2492dc3e-f514-8063-af78-ddbf5e54fc76 |
| url | https://www.notion.so/KDT-Story-applicants-sales_leads-FK-2492dc3ef5148063af78ddbf5e54fc76 |
| perf_flag | yes |
| importance | 5 |
| summary_5lines | |
|  | - 담당 세일즈 매니저의 성과를 퍼널별·기간별로 확인하려는 세일즈 리더 |
|  | - 가설: 문제 정의를 해결할 해결책은 무엇인지 |
|  | - 실험 결과 요약 (Result Summary) |
|  | - 실험 설계 관점에서 얻은 교훈과 고객 행동 인사이트를 간단히 요약하고 다음과 같이 연결합니다 |
|  | - 이를 통해 세일즈 매니저·배정일·회신 여부를 데이터 마트에 반영하여 성과 분석의 정확도가 높아진다. |

Original: https://www.notion.so/KDT-Story-applicants-sales_leads-FK-2492dc3ef5148063af78ddbf5e54fc76

- ▶ 목차

# [0] WHY & CONTEXT

###  배경 (background): 이 일을 왜 하는 것인지?
- 문제를 겪는 유저
  - 세일즈 대시보드에서 리드 → 매니저 배정 → 퍼널 변화까지 한 번에 보고 싶은 세일즈 운영자 및 분석자
  - 담당 세일즈 매니저의 성과를 퍼널별·기간별로 확인하려는 세일즈 리더
- 겪는 어려움
  - 현재 applicants 테이블에는 sales_lead_id가 없어 세일즈 매니저 정보·배정 시간·회신 여부를 조인할 수 없음
  - 기존 조인은 연락처 기반이라, 연락처 변경 시 조인 불일치 및 CX 혼선 발생
- 문제 정의
  - 세일즈 리드와 applicants를 안정적으로 연결할 수 있는 PK(FK)가 없어, 데이터 마트 및 대시보드에서 분석이 부정확
  - 신규 데이터와 기존 데이터 모두 연결되도록 sales_lead_id를 컬럼으로 추가하고, 기존 데이터도 일괄 백필해야 함

###  가설: 문제 정의를 해결할 해결책은 무엇인지
- 가설
  - applicants에 sales_lead_id를 추가하고, 기존 데이터까지 백필하면 연락처 변경에도 영향받지 않는 안정적인 데이터 연결 구조가 가능해진다.
  - 이를 통해 세일즈 매니저·배정일·회신 여부를 데이터 마트에 반영하여 성과 분석의 정확도가 높아진다.

# **[2] SOLUTION DESIGN (해결방안 설계)**

### **정책 및 조건 정의 (Policy & Conditions)**
- 해당 해결 방안에 대한 설계를 고려하기 전, 알아야하는 정책 및 조건

---
- applicants 테이블에 `sales_lead_id` 신규 컬럼 추가 (nullable)
- 신규 applicants 생성 시:
  - 해당 online_user_id에 매칭되는 최신 sales_lead_id를 자동 삽입
  - sales_lead_id 없음 → null 처리
- 기존 applicants 데이터:
  - phone 기준으로 sales_leads 테이블 매칭
  - 매칭 불가 시 null 유지
- `참고` 데이터 마트 반영 필드:
  1. 담당 세일즈 매니저명
  1. 세일즈 배정 날짜
  1. 회신 여부
  1. 세일즈 퍼널 상태

### Task 모음집

# **[3] PRD (Product Requirements Document)**

### **요구 기능 요약 (Core Features)**

### **QA 체크리스트**

# [4] Review & Learning

### 실험 결과 요약 (Result Summary)
- **Before → After 지표 변화**:
  - 정량 데이터 기반 변화량 정리 (전환율, 클릭률 등)
  - 
- **고객 반응 및 VOC 요약**:
  - 인터뷰/설문/채팅 기반 주요 피드백 정리
  - 

### 학습 정리 및 인사이트 (Key Learnings)
- 이번 실험 결과를 기반으로 다음 실험을 어떻게 설계할 수 있을지에 초점을 맞춥니다.
- 실험 설계 관점에서 얻은 교훈과 고객 행동 인사이트를 간단히 요약하고 다음과 같이 연결합니다
- 고객의 행동 변화로부터 무엇을 도출할 수 있었는가?
  - 
- 배운 점을 기반으로 어떤 추가 기회를 실험해볼 것인가?
  -

## Databases
