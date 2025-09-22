---
created_date: 2025-06-30
id: 2222dc3e-f514-808f-8938-faa67dc150e9
url: https://www.notion.so/NBC-Story-KDT-URL-2222dc3ef514808f8938faa67dc150e9
perf_flag: yes
importance: 5
summary_5lines:
  - 가설: 문제 정의를 해결할 해결책은 무엇인지
  - 실험 결과 요약 (Result Summary)
  - 실험 설계 관점에서 얻은 교훈과 고객 행동 인사이트를 간단히 요약하고 다음과 같이 연결합니다
  - 문제 정의
  - 정량 데이터 기반 변화량 정리 (전환율, 클릭률 등)
---

# 2025-06-30_[NBC-Story] KDT 슬랙봇 - 리드 상세 URL 추가

| Property | Value |
| --- | --- |
| created_date | 2025-06-30 |
| id | 2222dc3e-f514-808f-8938-faa67dc150e9 |
| url | https://www.notion.so/NBC-Story-KDT-URL-2222dc3ef514808f8938faa67dc150e9 |
| perf_flag | yes |
| importance | 5 |
| summary_5lines | |
|  | - 가설: 문제 정의를 해결할 해결책은 무엇인지 |
|  | - 실험 결과 요약 (Result Summary) |
|  | - 실험 설계 관점에서 얻은 교훈과 고객 행동 인사이트를 간단히 요약하고 다음과 같이 연결합니다 |
|  | - 문제 정의 |
|  | - 정량 데이터 기반 변화량 정리 (전환율, 클릭률 등) |

Original: https://www.notion.so/NBC-Story-KDT-URL-2222dc3ef514808f8938faa67dc150e9

- ▶ 목차

# [0] WHY & CONTEXT

###  배경 (background): 이 일을 왜 하는 것인지?
- 문제를 겪는 유저
  - 채널톡을 통해 들어오는 실시간 고객 문의를 응대하는 **CX팀**
- 겪는 어려움
  - 고객이 남긴 전화번호 또는 이름만 가지고는, 어떤 리드인지 파악이 어려움
  - 현재는 Slack 채널을 열고, 이름/전화번호로 과거 메시지를 검색 → 다시 applicants URL을 찾아 CRM/백오피스로 진입해야 하는 불편한 구조
  - applicants 상세 페이지는 실시간 커뮤니케이션에 최적화되어 있지 않으며, 세일즈 리드를 기준으로 문의를 파악해야 할 필요가 커짐
- 문제 정의
  - CX팀이 세일즈 리드 기반으로 실시간 대응을 원하나, Slack 메시지에 리드 상세 URL이 없어 불필요한 탐색/검색 시간이 발생하고 있음
  - 특히, **세일즈 리드가 아닌 경우에도 동일한 메시지 포맷**으로 인해 오해/혼선이 발생할 수 있음

###  가설: 문제 정의를 해결할 해결책은 무엇인지
- 가설
  - Slack 메시지 하단에 `sales_url`이 자동 노출되면, CX팀은 채널톡 문의 → Slack 메시지 클릭만으로 바로 리드 상세 정보를 확인할 수 있으며, 반복 탐색 없이 실시간 대응이 가능해질 것이다.
  - 또한 `phone` 필드를 기준으로 세일즈 리드 여부를 명확히 구분하면, 오탐이나 불필요한 응대 시도를 줄일 수 있을 것이다.

# **[2] SOLUTION DESIGN (해결방안 설계)**

### **정책 및 조건 정의 (Policy & Conditions)**
- 해당 해결 방안에 대한 설계를 고려하기 전, 알아야하는 정책 및 조건

---
- 현재는 **KDT 워크스페이스 한정 적용**
- `phone`이 존재하는 경우에만 세일즈 리드로 간주하고, Slack 메시지 하단에 `sales_url`을 노출
- `phone` 미존재 시 → "세일즈 리드 아님" 표시로 대체
- sales_url 포맷: https://h99backoffice.spartacodingclub.kr/nbcamp/salesman/lead/{리드_id}

### **고객 흐름 구조화 (Funnel Design)**
- ▶ 고객 행동 흐름 (Input → Output)
  - 예: 탐색 → 장바구니 → 최소주문충족 → 결제 시도 → 결제 완료
- 채널톡 문의 → Slack 메시지 확인 → `sales_url` 클릭 → 백오피스 리드 상세 확인 및 대응

### **UI/UX 설계 흐름 (Flow & Response)**

### **1️⃣ 플로우 1: Slack 메시지 자동 구성 흐름**
| step | 액션 | 시스템 응답 |
| --- | --- | --- |
| 1 | 유저가 채널톡 문의 또는 지원 시 리드 생성 | Slack 메시지 자동 발송 |
| 2 | 시스템이 phone 존재 여부 확인 | 존재 시 → sales_url 생성 |
| 3 | Slack 메시지 하단에 sales_url 삽입 | “- sales_url: [링크]” |
| 4 | 세일즈 리드에 phone이 없는 경우 | “- sales_url: [세일즈 리드 아님]” 메시지 삽입 |
  **예시 메시지 (Slack):**
  ```plain text
  이승수 / 010-1234-5678
  상담 신청 완료되었습니다.
  - sales_url: <https://h99backoffice.spartacodingclub.kr/nbcamp/salesman/lead/b4ecab83-a9ec-4e45-a3b8-bf78e961cdf4>
  ```

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
