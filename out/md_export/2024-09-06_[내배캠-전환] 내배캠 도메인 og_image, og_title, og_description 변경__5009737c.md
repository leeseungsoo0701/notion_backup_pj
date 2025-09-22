---
created_date: 2024-09-06
id: 5009737c-46e2-406d-93fd-323d2b4a7c2f
url: https://www.notion.so/og-image-og-title-og-description-5009737c46e2406d93fd323d2b4a7c2f
perf_flag: yes
importance: 4
summary_5lines:
  - 요구 사항: 문제 상황을 아래 기획으로 해결하고자합니다.
  - 개발 우선순위
  - 디자인 우선순위
  - 필수적으로 드러났으면 하는 포인트, 카피와 선택적으로 녹였으면 하는 부분을 구분하여 작성하고 디자이너와 논의하여 합의합니다.
  - [추가 고민 포인트]
---

# 2024-09-06_[내배캠-전환] 내배캠 도메인 og:image, og:title, og:description 변경

| Property | Value |
| --- | --- |
| created_date | 2024-09-06 |
| id | 5009737c-46e2-406d-93fd-323d2b4a7c2f |
| url | https://www.notion.so/og-image-og-title-og-description-5009737c46e2406d93fd323d2b4a7c2f |
| perf_flag | yes |
| importance | 4 |
| summary_5lines | |
|  | - 요구 사항: 문제 상황을 아래 기획으로 해결하고자합니다. |
|  | - 개발 우선순위 |
|  | - 디자인 우선순위 |
|  | - 필수적으로 드러났으면 하는 포인트, 카피와 선택적으로 녹였으면 하는 부분을 구분하여 작성하고 디자이너와 논의하여 합의합니다. |
|  | - [추가 고민 포인트] |

Original: https://www.notion.so/og-image-og-title-og-description-5009737c46e2406d93fd323d2b4a7c2f

#  기획안 (executive summary)
> 💡 요구 사항: 문제 상황을 아래 기획으로 해결하고자합니다.

  ---

### 디자인 우선순위
  > 💡 필수적으로 드러났으면 하는 포인트, 카피와 선택적으로 녹였으면 하는 부분을 구분하여 작성하고 디자이너와 논의하여 합의합니다.
  **[필수]**
  - 
  **[선택]**
  [추가 고민 포인트]
  - PM:
  - 디자이너: 

  ---

### 개발 우선순위
  - ▶ 의사소통이 어려울 때, Maker가 개발적 우선순위를 판단할 수 있게 메모합니다.
기획 중요도가 높은 항목부터 내림차순으로 정리합니다.
미리 발전 방향을 제시해, 초반 설계에 도움을 줄 수도 있습니다.
    ex)
    1. APM이 강의를 직접 제공할 수 있는 기능 구현 자체를 최우선으로 합니다.
    1. 강의 지급에 실수가 일어나지 않도록, 한번 더 확인하는 과정이 필수적입니다.
    1. Alert 대화 상자에서, 지급 내역이 맞는지 확인할 수 있으면 좋습니다.
    1. 추후, 어떤 APM이 어떤 예비 수강생에게 어떤 강의를 줬는지 확인할 수 있는 슬랙봇이 구현되어야 합니다.
  **[기능 명세서 작성]**
  - ▶ 예시

## Databases

### Database: 기능 명세서

| 개발 상태 | 로그  | 메모 및 질문 사항 | 상세 기능 | 생성자 | 예상 개발 소요 시간 | 주 기능 | 중요도 | 페이지 이름 | notion_url |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | 욕설, 비방 문자 포함
- 욕설, 비방으로 판단되어야 하는 문자들 예시: ㅅㅂ, 바보
- 개발적으로 이런 문자들을 필터링 해주는 로직이 있다면 공유 필요 | {'object': 'user', 'id': '8a032ebc-6a64-4d3d-9dc1-8c93f4ad7763', 'name': '이승수(PM팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/9b2954cd-91cd-40f5-95e7-34e205b1d5da/KakaoTalk_Photo_2024-03-12-19-51-41.jpeg', 'type': 'person', 'person': {'email': 'ss.lee@teamsparta.co'}} |  |  | 선택 |  | https://www.notion.so/1c126ed08f504eaeb86b82a0b4e5d1f7 |
|  |  |  | • As-is 100자 이상 작성하면 합격할 확률이 36% 올라요.
• To-be 최소 100자 이상 작성해주세요! | {'object': 'user', 'id': '8a032ebc-6a64-4d3d-9dc1-8c93f4ad7763', 'name': '이승수(PM팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/9b2954cd-91cd-40f5-95e7-34e205b1d5da/KakaoTalk_Photo_2024-03-12-19-51-41.jpeg', 'type': 'person', 'person': {'email': 'ss.lee@teamsparta.co'}} |  | 지원서 글자 수에 대한 UI / UX 변경 | 필수 |  | https://www.notion.so/As-is-100-36-To-be-100-5470c9b9429d42a48f3661a6bb88b985 |
|  |  |  | 특정 글자 연속 4번 이상 반복 시 보류 처리 | {'object': 'user', 'id': '8a032ebc-6a64-4d3d-9dc1-8c93f4ad7763', 'name': '이승수(PM팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/9b2954cd-91cd-40f5-95e7-34e205b1d5da/KakaoTalk_Photo_2024-03-12-19-51-41.jpeg', 'type': 'person', 'person': {'email': 'ss.lee@teamsparta.co'}} |  |  | 선택 |  | https://www.notion.so/4-5ad8292318be484185b905d8446de730 |
|  |  |  | 300자 이상 작성을 넛징하는 메시지 수정
• As-is 300자 이상 작성하면 합격할 확률이 62% 올라요.
• To-be 300자 이상 작성한 분들의 평균 합격률은 91.4% 에요! | {'object': 'user', 'id': '8a032ebc-6a64-4d3d-9dc1-8c93f4ad7763', 'name': '이승수(PM팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/9b2954cd-91cd-40f5-95e7-34e205b1d5da/KakaoTalk_Photo_2024-03-12-19-51-41.jpeg', 'type': 'person', 'person': {'email': 'ss.lee@teamsparta.co'}} |  |  | 필수 |  | https://www.notion.so/300-As-is-300-62-To-be-300-91-4-20cbf222a3544ef79f139f82bbabfc21 |
|  |  |  | 지원동기 200자 미만 보류 처리 | {'object': 'user', 'id': '8a032ebc-6a64-4d3d-9dc1-8c93f4ad7763', 'name': '이승수(PM팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/9b2954cd-91cd-40f5-95e7-34e205b1d5da/KakaoTalk_Photo_2024-03-12-19-51-41.jpeg', 'type': 'person', 'person': {'email': 'ss.lee@teamsparta.co'}} |  | 서류 보류 정책 기준 수정 | 필수 | 지원서 | https://www.notion.so/200-2492e4da1e0447a89474c5c657ea216c |
|  |  |  | 40세 이상 불합격 처리 | {'object': 'user', 'id': '8a032ebc-6a64-4d3d-9dc1-8c93f4ad7763', 'name': '이승수(PM팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/9b2954cd-91cd-40f5-95e7-34e205b1d5da/KakaoTalk_Photo_2024-03-12-19-51-41.jpeg', 'type': 'person', 'person': {'email': 'ss.lee@teamsparta.co'}} |  |  | 필수 |  | https://www.notion.so/40-39b03bdf3b5d4e66af2136d43cd2696f |
|  | nbc_apply2_essay_length_300 (로그에 어떤 내용이 들어가야 하는 지는 로그 정리 노션 링크 걸기) |  | 글자수가 300자 넘은 상태에서 1차 지원 제출 시 로그 추가 | {'object': 'user', 'id': '8a032ebc-6a64-4d3d-9dc1-8c93f4ad7763', 'name': '이승수(PM팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/9b2954cd-91cd-40f5-95e7-34e205b1d5da/KakaoTalk_Photo_2024-03-12-19-51-41.jpeg', 'type': 'person', 'person': {'email': 'ss.lee@teamsparta.co'}} |  |  | 선택 |  | https://www.notion.so/300-1-9934054b4f184e8eaa27a26886d80a2b |
|  |  |  |  | {'object': 'user', 'id': '8a032ebc-6a64-4d3d-9dc1-8c93f4ad7763', 'name': '이승수(PM팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/9b2954cd-91cd-40f5-95e7-34e205b1d5da/KakaoTalk_Photo_2024-03-12-19-51-41.jpeg', 'type': 'person', 'person': {'email': 'ss.lee@teamsparta.co'}} |  |  |  |  | https://www.notion.so/b20208d4e91c43caaf8f88e3dcfec780 |
|  |  |  | 지원동기 예시 30자 이상 동일 시 보류 처리 | {'object': 'user', 'id': '8a032ebc-6a64-4d3d-9dc1-8c93f4ad7763', 'name': '이승수(PM팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/9b2954cd-91cd-40f5-95e7-34e205b1d5da/KakaoTalk_Photo_2024-03-12-19-51-41.jpeg', 'type': 'person', 'person': {'email': 'ss.lee@teamsparta.co'}} |  |  | 선택 |  | https://www.notion.so/30-b80ff32f3d504350b54b2637f6030038 |
|  |  |  | 19세 미만 불합격 처리 | {'object': 'user', 'id': '8a032ebc-6a64-4d3d-9dc1-8c93f4ad7763', 'name': '이승수(PM팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/9b2954cd-91cd-40f5-95e7-34e205b1d5da/KakaoTalk_Photo_2024-03-12-19-51-41.jpeg', 'type': 'person', 'person': {'email': 'ss.lee@teamsparta.co'}} |  | 서류 불합격 정책 기준 수정 | 필수 |  | https://www.notion.so/19-e2c9212d72a14d0aa91959c7bce990bf |
|  |  |  | 100자 미만 동안은 제출하기 버튼이 비활성화 상태 | {'object': 'user', 'id': '8a032ebc-6a64-4d3d-9dc1-8c93f4ad7763', 'name': '이승수(PM팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/9b2954cd-91cd-40f5-95e7-34e205b1d5da/KakaoTalk_Photo_2024-03-12-19-51-41.jpeg', 'type': 'person', 'person': {'email': 'ss.lee@teamsparta.co'}} |  |  | 필수 |  | https://www.notion.so/100-ee8bc8e4ac1e4aef84f9a8a146a3a255 |


### Database: 기능 명세서

| 개발 상태 | 로그  | 메모 및 질문 사항 | 상세 기능 | 생성자 | 예상 개발 소요 시간 | 주 기능 | 중요도 | 페이지 이름 | notion_url |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | 노션 내, 상세 기제 | {'object': 'user', 'id': '8a032ebc-6a64-4d3d-9dc1-8c93f4ad7763', 'name': '이승수(PM팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/9b2954cd-91cd-40f5-95e7-34e205b1d5da/KakaoTalk_Photo_2024-03-12-19-51-41.jpeg', 'type': 'person', 'person': {'email': 'ss.lee@teamsparta.co'}} |  | og:image, og:title, og:description 변경 |  | 전체 | https://www.notion.so/a15d02a485c8491c99abba753cb438b4 |
