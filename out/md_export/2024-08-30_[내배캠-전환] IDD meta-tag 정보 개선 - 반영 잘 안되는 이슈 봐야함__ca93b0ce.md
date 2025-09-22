---
created_date: 2024-08-30
id: ca93b0ce-21cf-43cc-8448-3790de2279e3
url: https://www.notion.so/IDD-meta-tag-ca93b0ce21cf43cc84483790de2279e3
perf_flag: yes
importance: 5
summary_5lines:
  - 1. 문제 상황 해석 및 문제 정의
  - 배포해도 되지만 이후 챙겨야하는 사항 P1
  - [문제 정의]
  - 배포 전 진행하는 QA
  - 일반적으로는 BAU 퍼널 데이터를 기준으로
---

# 2024-08-30_[내배캠-전환] IDD meta-tag 정보 개선 - 반영 잘 안되는 이슈 봐야함

| Property | Value |
| --- | --- |
| created_date | 2024-08-30 |
| id | ca93b0ce-21cf-43cc-8448-3790de2279e3 |
| url | https://www.notion.so/IDD-meta-tag-ca93b0ce21cf43cc84483790de2279e3 |
| perf_flag | yes |
| importance | 5 |
| summary_5lines | |
|  | - 1. 문제 상황 해석 및 문제 정의 |
|  | - 배포해도 되지만 이후 챙겨야하는 사항 P1 |
|  | - [문제 정의] |
|  | - 배포 전 진행하는 QA |
|  | - 일반적으로는 BAU 퍼널 데이터를 기준으로 |

Original: https://www.notion.so/IDD-meta-tag-ca93b0ce21cf43cc84483790de2279e3

- ▶ 목차 리스트

#  문제 정의 및 서술. Problem Statement
> 💡 1. 문제 상황 해석 및 문제 정의
2. 타겟(고객)이 가진 문제를 해결해줄 수 있는 가설
3. 목표 지표와 위 일을 통해 배울 수 있는 점

  ---
  **[문제 상황 해석]**
  *일반적으로는 BAU 퍼널 데이터를 기준으로
그 외에도 데이터 포인트, 정성 인터뷰 등. 즉 기획 배경을 숫자로 나타내주세요.*
  - 
  **[문제 정의]**
  *문제 상황에 대한 정성, 정량 데이터를 활용하여 다각적으로 해석한 문제를 하나로 정의해주세요.*
  - 
  **[가설]**
  *목표하는 타겟과 가설의 액션에 문제가 해결될 %를 예상합니다. *
  *ex. 적어도 X퍼센트의 Y(타겟)는 Z할 것이다.*
  - ▶ 참고자료: [아이디어 불패의 법칙] 정리
    - XYZ가설.
    - [아이디어 → 시장 호응 가설 → XYZ가설 → xyz가설] 순으로 점점 구체화.
    - 시장 호응 가설: 시장이 아이디어를 어떻게 받아들일지에 관한 핵심 신념, 가설, 상상. 
    - XYZ가설: 적어도 X퍼센트의 Y는 Z할 것이다. 
    - `xyz가설`: 보통 y를 줄임. 범위를 축소하여, ‘지금 당장 실행 가능하고 검증 가능한’ 가설을 얻는 것. 과감하게 축소해야 하지만, 표적시장에 대한 대표성을 갖도록 유의.
    - 예시
  - 
  **[목표 지표 & 기간] **
  *타겟 기반의 지표 설정을 통해 성공 지표와 가드레일 지표를 설정합니다. 
액션의 기간을 미리 설정하고 성공/실패에 따른 배운 점*
  - 액션 효율 측정 기간: 
  - 현재 지표
    - 
  - 성공 지표
    - 
    - ▶ 성공 목표에 달성하게 된다면 우리는 무엇을 배웠고 앞으로 방향성이 어떻게 될까요?
  - 가드레일 지표
    - 
    - ▶ 목표에 달성하지 못했다면 우리는 무엇을 배웠고 앞으로 방향성이 어떻게 될까요?

  ---

#  기획안 (executive summary)
> 💡 요구 사항: 문제 상황을 아래 기획으로 해결하고자합니다.

  ---

### 임팩트 예측
  - ▶ *제품을 통해 사용자가 얻게 될 가치나 경제-사회적 가치를 요약합니다.*
    ex)
    튜토리얼 비디오를 제공해 등록률을 00% 향상시킵니다.
    결제 페이지 개선과 결제 시기별 할인 혜택 도입으로 최종 결제 완료율을 00% 증가시킵니다.

### 개발 원칙
  - ▶ 의사소통이 어려울 때, Maker가 스스로 우선순위를 판단할 수 있게 메모합니다.
중요도가 높은 항목부터 내림차순으로 정리합니다.
미리 발전 방향을 제시해, 초반 설계에 도움을 줄 수도 있습니다.
    ex)
    1. APM이 강의를 직접 제공할 수 있는 기능 구현 자체를 최우선으로 합니다.
    1. 강의 지급에 실수가 일어나지 않도록, 한번 더 확인하는 과정이 필수적입니다.
    1. Alert 대화 상자에서, 지급 내역이 맞는지 확인할 수 있으면 좋습니다.
    1. 추후, 어떤 APM이 어떤 예비 수강생에게 어떤 강의를 줬는지 확인할 수 있는 슬랙봇이 구현되어야 합니다.
  - [ ] 
  **[기능 명세서 작성]**
  - ▶ 예시

#  프로덕트 디자인
> 💡 요구사항 및 고민사항 논의

  ---
  [프로덕트 디자이너가 업무 진행에 추가로 필요한 정보]
  *디자인 진행하며 추가적인 정보나 맥락이 필요하다면 작성한 뒤 슬랙에 태그해주세요.*
  - [ ] 
  [추가 고민 포인트]
  - PM:
  - 디자이너: 
  - [ ] 해당 문서에 피그마 링크를 올린 뒤, 프로덕트 디자이너가 #개발_디자인완료 채널에 공유해주세요.

---

#  최종 QA
> 💡 배포 전 진행하는 QA
크리티컬한 사항 P0
배포해도 되지만 이후 챙겨야하는 사항 P1
백로그 P2

  ---
  [디자인 QA사항]
  - [ ] 
  [PM QA사항]
  - [ ] 
  [개발 QA사항]
  - ▶ warning 없는지 체크
    - [ ] key 에러
  - ▶ swiper & overflow UI 사용 시 
    - [ ] overflow : hidden 체크 
    - [ ] 테블릿 사이즈에서 양 옆으로 밀어보기 
  - ▶ 모바일 & 테블릿
    - [ ] iOS
    - [ ] Android
    - [ ] 테블릿 사이즈
    - [ ] height 짧은 경우 
    - [ ] width 360px 
  - ▶ 브라우저 별 엣지케이스 확인
    - [ ] safari 브라우저
    - [ ] 삼성 브라우저
  - ▶ 용량 체크
    - [ ] 영상 소스 총 용량 5mb 이하 체크 
  - [ ] 2차 QA가 필요한 경우, 미리 캘린더상 일정을 확보해주세요.

## Databases

### Database: 기능 명세서

| 개발 상태 | 로그  | 메모 및 질문 사항 | 상세 기능 | 생성자 | 예상 개발 소요 시간 | 주 기능 | 중요도 | 페이지 이름 | notion_url |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | 300자 이상 작성을 넛징하는 메시지 수정
• As-is 300자 이상 작성하면 합격할 확률이 62% 올라요.
• To-be 300자 이상 작성한 분들의 평균 합격률은 91.4% 에요! | {'object': 'user', 'id': '8a032ebc-6a64-4d3d-9dc1-8c93f4ad7763', 'name': '이승수(PM팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/9b2954cd-91cd-40f5-95e7-34e205b1d5da/KakaoTalk_Photo_2024-03-12-19-51-41.jpeg', 'type': 'person', 'person': {'email': 'ss.lee@teamsparta.co'}} |  |  | 필수 |  | https://www.notion.so/300-As-is-300-62-To-be-300-91-4-1ac4e0cdb7524ee695352f0d02c71e90 |
|  |  |  | 40세 이상 불합격 처리 | {'object': 'user', 'id': '8a032ebc-6a64-4d3d-9dc1-8c93f4ad7763', 'name': '이승수(PM팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/9b2954cd-91cd-40f5-95e7-34e205b1d5da/KakaoTalk_Photo_2024-03-12-19-51-41.jpeg', 'type': 'person', 'person': {'email': 'ss.lee@teamsparta.co'}} |  |  | 필수 |  | https://www.notion.so/40-234b1f1600df4192a4e1f79c7cbf98d7 |
|  |  |  | 19세 미만 불합격 처리 | {'object': 'user', 'id': '8a032ebc-6a64-4d3d-9dc1-8c93f4ad7763', 'name': '이승수(PM팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/9b2954cd-91cd-40f5-95e7-34e205b1d5da/KakaoTalk_Photo_2024-03-12-19-51-41.jpeg', 'type': 'person', 'person': {'email': 'ss.lee@teamsparta.co'}} |  | 서류 불합격 정책 기준 수정 | 필수 |  | https://www.notion.so/19-26af80e796a443f4b2d3c6d9286ee54f |
|  |  |  | 지원동기 200자 미만 보류 처리 | {'object': 'user', 'id': '8a032ebc-6a64-4d3d-9dc1-8c93f4ad7763', 'name': '이승수(PM팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/9b2954cd-91cd-40f5-95e7-34e205b1d5da/KakaoTalk_Photo_2024-03-12-19-51-41.jpeg', 'type': 'person', 'person': {'email': 'ss.lee@teamsparta.co'}} |  | 서류 보류 정책 기준 수정 | 필수 | 지원서 | https://www.notion.so/200-333f2a63394e40968ca6c4f7ee6dabde |
|  |  |  | • As-is 100자 이상 작성하면 합격할 확률이 36% 올라요.
• To-be 최소 100자 이상 작성해주세요! | {'object': 'user', 'id': '8a032ebc-6a64-4d3d-9dc1-8c93f4ad7763', 'name': '이승수(PM팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/9b2954cd-91cd-40f5-95e7-34e205b1d5da/KakaoTalk_Photo_2024-03-12-19-51-41.jpeg', 'type': 'person', 'person': {'email': 'ss.lee@teamsparta.co'}} |  | 지원서 글자 수에 대한 UI / UX 변경 | 필수 |  | https://www.notion.so/As-is-100-36-To-be-100-40a00451f18a4365a6779389fd05dd57 |
|  |  |  | 특정 글자 연속 4번 이상 반복 시 보류 처리 | {'object': 'user', 'id': '8a032ebc-6a64-4d3d-9dc1-8c93f4ad7763', 'name': '이승수(PM팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/9b2954cd-91cd-40f5-95e7-34e205b1d5da/KakaoTalk_Photo_2024-03-12-19-51-41.jpeg', 'type': 'person', 'person': {'email': 'ss.lee@teamsparta.co'}} |  |  | 선택 |  | https://www.notion.so/4-48cf8ce321eb49b1a4042fa1e7a0712c |
|  |  |  |  | {'object': 'user', 'id': '8a032ebc-6a64-4d3d-9dc1-8c93f4ad7763', 'name': '이승수(PM팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/9b2954cd-91cd-40f5-95e7-34e205b1d5da/KakaoTalk_Photo_2024-03-12-19-51-41.jpeg', 'type': 'person', 'person': {'email': 'ss.lee@teamsparta.co'}} |  |  |  |  | https://www.notion.so/6a1f53c4932040968a8ac3c2204cc4f9 |
|  |  |  | 욕설, 비방 문자 포함
- 욕설, 비방으로 판단되어야 하는 문자들 예시: ㅅㅂ, 바보
- 개발적으로 이런 문자들을 필터링 해주는 로직이 있다면 공유 필요 | {'object': 'user', 'id': '8a032ebc-6a64-4d3d-9dc1-8c93f4ad7763', 'name': '이승수(PM팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/9b2954cd-91cd-40f5-95e7-34e205b1d5da/KakaoTalk_Photo_2024-03-12-19-51-41.jpeg', 'type': 'person', 'person': {'email': 'ss.lee@teamsparta.co'}} |  |  | 선택 |  | https://www.notion.so/75d409a6c9914b36b5ad29895ae7e63c |
|  | nbc_apply2_essay_length_300 (로그에 어떤 내용이 들어가야 하는 지는 로그 정리 노션 링크 걸기) |  | 글자수가 300자 넘은 상태에서 1차 지원 제출 시 로그 추가 | {'object': 'user', 'id': '8a032ebc-6a64-4d3d-9dc1-8c93f4ad7763', 'name': '이승수(PM팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/9b2954cd-91cd-40f5-95e7-34e205b1d5da/KakaoTalk_Photo_2024-03-12-19-51-41.jpeg', 'type': 'person', 'person': {'email': 'ss.lee@teamsparta.co'}} |  |  | 선택 |  | https://www.notion.so/300-1-a213d0e45ffc41a186650f9e9f261be2 |
|  |  |  | 지원동기 예시 30자 이상 동일 시 보류 처리 | {'object': 'user', 'id': '8a032ebc-6a64-4d3d-9dc1-8c93f4ad7763', 'name': '이승수(PM팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/9b2954cd-91cd-40f5-95e7-34e205b1d5da/KakaoTalk_Photo_2024-03-12-19-51-41.jpeg', 'type': 'person', 'person': {'email': 'ss.lee@teamsparta.co'}} |  |  | 선택 |  | https://www.notion.so/30-cefe4b8f2fed46f69e57a67b94e3a3dd |
|  |  |  | 100자 미만 동안은 제출하기 버튼이 비활성화 상태 | {'object': 'user', 'id': '8a032ebc-6a64-4d3d-9dc1-8c93f4ad7763', 'name': '이승수(PM팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/9b2954cd-91cd-40f5-95e7-34e205b1d5da/KakaoTalk_Photo_2024-03-12-19-51-41.jpeg', 'type': 'person', 'person': {'email': 'ss.lee@teamsparta.co'}} |  |  | 필수 |  | https://www.notion.so/100-fd5b6ff7ab2046f88b30cbf6618610eb |


### Database: 기능 명세서

| 개발 상태 | 로그  | 메모 및 질문 사항 | 상세 기능 | 생성자 | 예상 개발 소요 시간 | 주 기능 | 중요도 | 페이지 이름 | notion_url |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | {'object': 'user', 'id': '8a032ebc-6a64-4d3d-9dc1-8c93f4ad7763', 'name': '이승수(PM팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/9b2954cd-91cd-40f5-95e7-34e205b1d5da/KakaoTalk_Photo_2024-03-12-19-51-41.jpeg', 'type': 'person', 'person': {'email': 'ss.lee@teamsparta.co'}} |  |  |  |  | https://www.notion.so/6b649c99a2304b86bc88c06f49b6f41a |
