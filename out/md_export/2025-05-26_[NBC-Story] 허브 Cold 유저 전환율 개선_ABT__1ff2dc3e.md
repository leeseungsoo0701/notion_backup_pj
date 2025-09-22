---
created_date: 2025-05-26
id: 1ff2dc3e-f514-8052-875d-d05fa3c65d8d
url: https://www.notion.so/NBC-Story-Cold-_ABT-1ff2dc3ef5148052875dd05fa3c65d8d
perf_flag: yes
importance: 5
summary_5lines:
  - A/B 실험군 분기 기능 적용
  - A/B 실험군 분기 정확성 검토
  - 실험 결과 요약
  - 현재 허브페이지는 트랙 리스트업 중심으로 cold 유저가 필요한 개념 설명, 수강 절차 안내, 취업 사례 중심 콘텐츠가 부족함. 내일배움캠프가 무엇인지, 어떤 것을 살펴봐야하는지도 알 수 없음 ⇒ 3,4유형의 트랙 탐색 전환율 저조
  - 문제 정의
---

# 2025-05-26_[NBC-Story] 허브 Cold 유저 전환율 개선_ABT

| Property | Value |
| --- | --- |
| created_date | 2025-05-26 |
| id | 1ff2dc3e-f514-8052-875d-d05fa3c65d8d |
| url | https://www.notion.so/NBC-Story-Cold-_ABT-1ff2dc3ef5148052875dd05fa3c65d8d |
| perf_flag | yes |
| importance | 5 |
| summary_5lines | |
|  | - A/B 실험군 분기 기능 적용 |
|  | - A/B 실험군 분기 정확성 검토 |
|  | - 실험 결과 요약 |
|  | - 현재 허브페이지는 트랙 리스트업 중심으로 cold 유저가 필요한 개념 설명, 수강 절차 안내, 취업 사례 중심 콘텐츠가 부족함. 내일배움캠프가 무엇인지, 어떤 것을 살펴봐야하는지도 알 수 없음 ⇒ 3,4유형의 트랙 탐색 전환율 저조 |
|  | - 문제 정의 |

Original: https://www.notion.so/NBC-Story-Cold-_ABT-1ff2dc3ef5148052875dd05fa3c65d8d

- ▶ 목차

# [0] WHY & CONTEXT

### 배경 (background): 이 일을 왜 하는 것인지?
- 문제를 겪는 유저
  - 검색광고 유입 분석 (허브)
| 유형 | 검색어 | 분모 | 유입 비중 | 전환율 | 분자 | 전환 비중 
(트랙 PV) |
| --- | --- | --- | --- | --- | --- | --- |
| 1유형 | 내일배움부트캠프 | 80 | 1% | 56.30% | 45 | 3% |
|  | 스파르타코딩클럽 |  |  | 49.6% |  |  |
|  | 스파르타내일배움캠프 |  |  |  |  |  |
| 2유형 | 부트캠프 | 1094 | 18% | 49.20% | 538 | 34% |
|  | 코딩 강의 | 312 | 5% | 55.10% | 172 | 11% |
|  | 개발자 부트캠프 | 270 | 5% | 35.90% | 97 | 6% |
|  | it 교육학원 | 261 | 4% | 33.70% | 88 | 6% |
|  | 소계 | 1937 | **33%** |  | 895 | **56%** |
| 3유형 | 내일배움캠프 |  |  | 15.6% |  |  |
|  | 내일배움카드 | 1059 | 18% | 19.40% | 205 | 13% |
|  | 내일배움카드 국비지원 | 346 | 6% | 9.54% | 33 | 2% |
|  | 국비지원교육 | 880 | 15% | 13.00% | 114 | 7% |
|  | 국비 교육 | 806 | 14% | 10.00% | 81 | 5% |
|  | 소계 | 3091 | **52%** |  | 433 | **27%** |
| 4유형 | 고졸취업 | 248 | 4% | 20.00% | 50 | 3% |
|  | 취업 사이트 | 209 | 4% | 9.00% | 19 | 1% |
|  | 직업 전문 학교 | 130 | 2% | 17.00% | 22 | 1% |
|  | 소계 | 587 | 10% |  | 91 | 6% |
| 전체 |  | 5935 | 100% |  | 1599 | 100% |
  - 내일배움캠프 허브페이지에 유입한 신규 유저 (특히 검색광고/콘텐츠광고 유입 초기 사용자)
  - 검색 키워드 상으로는 ‘내일배움카드’, ‘국비지원교육’, ‘취업’, ‘부트캠프’ 등 비교적 명확한 니즈를 보이는 것처럼 보이지만
- 겪는 어려움
  - 실제로는 탐색을 이제 막 시작한 cold 유저에 가까움
  - 현재 허브페이지는 트랙 리스트업 중심으로 cold 유저가 필요한 개념 설명, 수강 절차 안내, 취업 사례 중심 콘텐츠가 부족함. 내일배움캠프가 무엇인지, 어떤 것을 살펴봐야하는지도 알 수 없음 ⇒ 3,4유형의 트랙 탐색 전환율 저조
- 문제 정의
  - 트랙 나열 중심의 허브 구조는 cold 유저의 초기 탐색 니즈(정보 습득, 방향 탐색)를 충족시키지 못하고 빠른 이탈로 이어짐

### 가설
**허브페이지 상단에** **유저 유형별 주요 니즈**(입문자 가이드, 국비지원 여부, 취업 연계 정보)**를 간결하게 배치**하면,
정보 부족이나 불확실성으로 이탈하는 3·4유형 사용자가 **필요한 콘텐츠를 이탈 전 습득하게 되어 트랙 탐색률(PV)이 증가**할 것이다.
- ▶ 이전 ver
  - 탐색 초기 단계에 있는 cold 유저(3,4유형)에게 정보 습득 흐름을 제공하는 요약형 탐색 메뉴와 입문 콘텐츠 카드 블록을 허브에 노출하면
  - 유저는 자신의 탐색 목적에 맞는 콘텐츠를 습득하여 트랙 PV로 탐색하고 참가 신청하기를 누르는 비율이 늘어날 것이다.

# [1] GOAL & METRICS

### 성공 지표와 측정 설계
| 항목 | 값 또는 설명 |
| --- | --- |
| 액션 측정 기간 | 실험 배포 후 7-10일 |
| 현재 지표 | 허브 → 트랙 PV  / 보조 3유형 14%, 4유형 10% |
| 성공 지표 | 허브 → 트랙 PV +10% 증가 / 3유형 16%, 4유형 12%
보조 지표 : 카드 클릭률 1% |
| 가드레일 지표 | 이탈률 증가 없음, 체류시간 유지 또는 증가 |

### 학습 포인트 정의
| 결과 유형 | 얻을 수 있는 인사이트 방향성 |
| --- | --- |
| 성공 시 | cold 유저 대상 정보 설계가 탐색 흐름을 돕고 전환을 유도할 수 있음을 검증 |
| 무승부 시 | 콘텐츠/메뉴 위치나 UI 구성 방식의 조정 필요 |
| 실패 시 | cold 유저 비중이 예상을 넘어서 탐색 진입조차 어려운 상태일 가능성 |

# [2] SOLUTION DESIGN

### 정책 및 조건 정의 (Policy & Conditions)
- 유입 유형에 따라 분기하지 않고, 전 유저에게 동일한 개선된 UI 구성 제공
  - ⇒ 대신 트랙 선택을 결정하고 들어온 유저가 트랙 탐색에 방해되지 않도록
- 탐색 목적 유도를 위한 요약형 탐색 메뉴 + cold 유저용 입문 콘텐츠 카드 블록 삽입
> 💡 To. 여주님
  1. 허브페이지를 이탈하지 않는 (아웃링크 등 X)
  1. 정보를 바로 탐색할 수 있는
  1. 고객이 어떤 정보에 반응하는지 구분가능한 
  (..!) 클리커블

### 고객 흐름 구조화 (Funnel Design)
허브 유입 → 탐색 메뉴 or 콘텐츠 클릭 → 정보 확인 → 트랙 상세 → 지원서 작성

### UI/UX 설계 흐름
*참고 UI 예시 - 처음이라 막막하신가요? div*

---
**cold 유저용 입문 콘텐츠 카드**
처음이라 막막하신가요?
국비지원부터 취업까지, 단계별로 안내해드릴게요.
| 질문 | 서브타이틀 | 모달 답변 |
| --- | --- | --- |
| 국비지원, 왜 0원인가요?  | 내일배움카드 사용법부터 수강 신청까지의 전체 과정을 알려드릴게요 | 교육비가 0원이라니, 처음엔 낯설 수 있어요. 내일배움카드는 정부가 발급하는 지원카드로, 자격만 충족되면 교육비 전액이 국비로 지원돼요. 내일배움캠프 서류 합격 후 내일배움카드 자격 대상과 발급 가이드를 안내해드리고 있어요. 발급 이후 고용24에서 수강신청하며 내일배움카드를 사용할 수 있어요.

*내일배움캠프는 카드 발급 전에도 참가 신청이 가능하니 지금 트랙을 살펴보세요!
CTA : 전체 과정 보러가기 / 닫기 |
| 국비교육으로 취업이 진짜 되나요? | 취업 1위 내일배움캠프의 노하우부터 지금의 결과까지 숫자로 확인하세요. | 내일배움캠프는 단순한 이론식 교육이 아니라, 취업까지 설계된 철저한 실무 중심 과정이에요. 1820명이라는 가장 많은 취업생을 배출했고 이 중 573명은 2025년 취업에 성공했습니다. 내일배움캠프만의 스파르타식 몰입 교육으로 전공, 경험, 배경 관계없이 누구든 도전하고 성장할 수 있어요.

CTA : 전체 과정 보러가기 / 닫기 |
| 내일배움캠프, 나에게 맞을까요? | 팀스파르타만의 차별화된 교육 방식으로 비전공자는 물론 직무 전환으로도 취업에 성공하고 있습니다. | IT 취업, 처음이거나 독학으로 준비하고 있나요? 내일배움캠프는 단 하루도 낭비하지 않는 효율적인 성장 공식을 제공하고 있어요. 이 과정으로 사회 초년생부터 직무전환을 희망하는 분들도 취업에 성공하고 있어요. 나와 비슷한 수료생들의 사례가 궁금하다면, 각 트랙에서 실제 후기를 직접 확인해보세요.

CTA : 전체 과정 보러가기 / 닫기 |
고민) 허브에 CTA 2개는 어떨까요!!! 전체 유저 플로우상 트랙 카드 하단에 위치했지만, 상단에서 이탈이 잦은 저관여자에게도 노출시키기 위함 → 다음에 진행
https://prod-files-secure.s3.us-west-2.amazonaws.com/83c75a39-3aba-4ba4-a792-7aefe4b07895/d8336c95-cd70-4d9b-af57-ec8aab355747/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMEZTPWR%2F20250912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250912T015114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG9VRi%2B0rdFHV2WQ4HOrg8G%2BZm5g5O%2FGefuQvwgtO20AAiA%2BIf83g0v5PU0xyy1o5Tc%2BnqGGoMx24hhS1Z5WScRm1Cr%2FAwgjEAAaDDYzNzQyMzE4MzgwNSIMGQxxtT1%2Bp6GjIn9mKtwDNLRbgsDw5SfRFhkYC3KouMldjPAZeanunk6%2B8O%2F1RRk%2FZ8SIXOT5El8NzFwl2iQArVfwCvvjms9ZMrfn716LSoxzndENN%2F0LDYH%2Fr87ZIEuF2LVfAySsYBXKgNXFTct0HoDT%2BAeALpvpaw6jET755I1sHqfXxEegmxfOa2Ei7fqmJKG3Wjl95309V0xJbjE2IVHnN9GM0k%2FHL%2FkJho5sqe20LAFyVIEtzC8%2FpRyZ9OBLPbpBxOEZh8ct%2F%2BHEoqDdMl478OC3pNgjFZhCxjou25MAIylcngDReHq5rsaNUpsygu7ZaQT3bwpFYAE7AAJvUyzRIjygHN%2FWcge9MvzACQOGdnFnkQn4KHZ1NU4wmk06FfG1Y8wOs6%2BW1%2BmKy%2Bu%2FaaJ29xlX0Ie2qdOtsbVx8L5oMyg81SuL6AUgQ7uta01L3OWmGt7KukoI6236bhxoGNwSwR1k7V3C8cVh1Tmi9UyKaXGI8SlrVev8WkEDbmgsGn2mm6kWjOto6aJkpqQRtZxGRvo2jnNHyktjsZz06zHGzBgfo6rY%2FTIjn34eIEHdR%2FxqEl7oh23hpR0kvhc93rO3XoVYLgDXeANQRU%2BItDIoBatA%2Fpn%2FKJ0%2Fk9Nf0jse%2B42tMq0PpnCMedQwoe%2BNxgY6pgFaf7hwff6VC9YkC8JqvibfMl2uw%2B6pZzn2pc9oQuG2P6q%2Br8kxF0Qv7ics0SYfRg6137WwtjFS54uK%2Fd%2BG8VqLjQF06O8FL%2BVNtxsKikWwNxPwIUMIXOxH8A%2F9y10GrM56t2iO8FfJQ3F4I%2BiDHgjQH1%2FFnkJVYHDRtO0hq4SCM5qFa8iJCnnocDIoNnOyl6oaBG1Ovz9MS8mF1t%2FakYCs1WMFjtrs&X-Amz-Signature=4fd0d4b553764ff76dc9c3ea355e6f38c330041caa903de579bfd83b89ba07fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
- ▶ (보류) 요약형 탐색 메뉴
| step | 액션 | 시스템 응답 |
| --- | --- | --- |
| 1 | 허브 진입 | 상단에 탐색 메뉴 노출 (예: 혜택 / 지원 방법 / 취업 상담 / 이벤트 등) |
| 2 | 클릭 | 해당 콘텐츠로 앵커 이동 |
| 3 | 전환 | 트랙 상세 또는 지원서 작성 흐름 연결 |

# [3] PRD (Product Requirements Document)

### Task 모음집

# **[3] PRD (Product Requirements Document)**

### **요구 기능 요약 (Core Features)**

### **QA 체크리스트**

### 요구 기능 요약
- [ ] 요약형 탐색 메뉴 UI 삽입
- [ ] 입문 콘텐츠 카드 블록 구성 및 노출
- [ ] 클릭 시 정보 콘텐츠 또는 트랙 상세 연결
- [ ] 클릭/전환 이벤트 GA/Amplitude 트래킹
- [ ] A/B 실험군 분기 기능 적용

### QA 체크리스트
- [ ] 각 메뉴/카드 클릭 시 연결 정확성 확인
- [ ] 반응형 대응 여부 확인 (PC/Mobile)
- [ ] 클릭 이벤트 및 트래킹 정상 수집 여부
- [ ] A/B 실험군 분기 정확성 검토

# [4] Review & Learning

### 실험 결과 요약
- Before → After 지표 변화:
  - B안 종료
    - 전체 트랙 PV까지의 전환은 해당 타겟의 모수가 점점 적어지며 유의미한 차이를 보이지 않았음
    - 그러나 허브 내 다른 CTA 대비 Cold 유저에 대한 반응을 이끌어내고 트랙 PV로의 전환을 기대하는 첫 삽으로서의 목표는 달성한 것으로 판단 → 후속 그로스
    https://prod-files-secure.s3.us-west-2.amazonaws.com/83c75a39-3aba-4ba4-a792-7aefe4b07895/01c23949-453a-4ff4-98e1-c8f4f4067f14/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677HFQOFH%2F20250912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250912T015134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCULZk3u43sERuSQYwI%2B8H0CaL%2F93ahje49s%2FRNhPD9%2FQIgaLX1OgPDC6pYM0WcT8CiBVi1Ome%2BdSb4rqJ7IVvg3V8q%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDHVli0CbvVyu2Q7JoSrcAwb06ktwGUKjjI8NWK3GPLWSyVg4by7mnnF1%2Bi5VOmWK%2FqxdRf%2B5NTmhhauuoyisthVuamOq9Po3MUpHo95oMB9PYMPgBXwE6hxMAeBvVW1ltyUSCN5qdkMJmET3C2qj92dmOZQ6D%2FIURKREXgBuwIq05qozD8JIeYmLH0qWTtolwfaaC3tiE6DbL5YPHiN0TCOR%2BSGGXFOBHSsOpRy3gEnqkEu4qRhFtNuMUim8gcPNJeTV9kpXkjDY8C%2F%2FLfrbyGyTjAWqQqpU6SZTtoa40RvOMOcQFG0lfvUiFAvDJERR1Xyf2OTzO8ulsU4epTJN8LMtuCO7ZbcG4URbTZigkZqxhIwmtH69B2ayhCQ98Z4SFyuCgPz3XCt44ja8MSCEKquERYTXQzxlpt1C0NBlIvxLgOZNps7HX4VeWfatwWgeL5WvtDdVr7hqAPFwIgRhIM1x3C4ADgkYVcwYCFMPAUO5bJoCeZkb0vq06sGfyX%2FYJUvdPMrPbIUjWzN5kBkHdajPUgme%2BTh0YdiKWqLGLH1TPgXkPWbPO5bLvxizXeKM7d5Lz0gUweTZEhSn9l4fLJm5VAgkIAyH63Z%2FfOMDBzzNZ0RzGtH1XSCmAfh6RJO8CUiNIpEyZGGX2HcFMIDwjcYGOqUBcVW2TWPTtom7uHqVdOLqVlYoQ9m%2FFHmgByc8g2ELECgimSjoVMrc5AJaXNzJPVk4kcnX5qk%2FCTpGYKZjNYUugYnEhXfPV%2BeE3GbVegLTSyFl4msl9L2ylzajgd8KsRmyMVuMRFsXYLnZ1TFtbnSt2kvR26fXsKeHxqDLUyxTfSLYtJT08gC3LaBdbscv7BOEnDdUF%2FpF91k%2ByO7alOitKRHIzjzn&X-Amz-Signature=cd81e01d7808bd46b8834b507ca821fc2a542370d71d6e27656a7bebf7e5bd43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
- 고객 반응 및 VOC 요약:
  - 

### 학습 정리 및 인사이트
- 고객의 행동 변화로부터 무엇을 도출할 수 있었는가?
  - 
- 배운 점을 기반으로 어떤 추가 기회를 실험해볼 것인가?
  - 

---

### 2025.05.27 미팅
@mention
참석자 : 박지영, 이은수, 이어진
- 허브페이지 유입 비중 질문
  - 맞다. none 네이버 브랜드 검색이 많은편 까봐야됨
- 허브페이즈 검색어 = term으로 봐도 되는지
  - 1,2,3,4 유형 나눈 것 예시
  - 맞음
- 허브페이지 유입 트렌드 궁금증
  - 원래 허브로 떨구는 광고도 많이 한다.
  - 지금은 IMC나 대형 캠페인은 없고 자잘하게 들어가서 전체 예산이 줄어든 상황
  - 국비지원 교육 키워드가 볼륨이 줄어든 상황
- 허브페이지 앞으로 전략
  - 별도 마케팅 캠페인 진행여부에 따라 달라질 수 있으나, 지금과 비슷한 수준
    - 검색어가 변경될 예정은 없고 예산 감액은 하진 않을듯
- 허브페이지 Facebook 매체 유입 소재 or 검색광고 외 유입 소재를 확인할 수 있는 곳
  -

## Databases
