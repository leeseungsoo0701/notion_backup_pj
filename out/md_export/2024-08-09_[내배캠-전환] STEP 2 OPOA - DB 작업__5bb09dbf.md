---
created_date: 2024-08-09
id: 5bb09dbf-9540-4010-84ef-1ea19f79086e
url: https://www.notion.so/STEP-2-OPOA-DB-5bb09dbf9540401084ef1ea19f79086e
perf_flag: yes
importance: 5
summary_5lines:
  - DB저장 및 지원 중 퍼널을 OPOA 구조에 적용하게 되면 지원시작 to 제출완료 전환율이 20%이상 증가할 것이다. (2차 view to 2차완료 10%이상 증가)
  - 1. 문제 상황 해석 및 문제 정의
  - 배포해도 되지만 이후 챙겨야하는 사항 P1
  - [문제 정의]
  - 배포 전 진행하는 QA
---

# 2024-08-09_[내배캠-전환] STEP 2 OPOA - DB 작업

| Property | Value |
| --- | --- |
| created_date | 2024-08-09 |
| id | 5bb09dbf-9540-4010-84ef-1ea19f79086e |
| url | https://www.notion.so/STEP-2-OPOA-DB-5bb09dbf9540401084ef1ea19f79086e |
| perf_flag | yes |
| importance | 5 |
| summary_5lines | |
|  | - DB저장 및 지원 중 퍼널을 OPOA 구조에 적용하게 되면 지원시작 to 제출완료 전환율이 20%이상 증가할 것이다. (2차 view to 2차완료 10%이상 증가) |
|  | - 1. 문제 상황 해석 및 문제 정의 |
|  | - 배포해도 되지만 이후 챙겨야하는 사항 P1 |
|  | - [문제 정의] |
|  | - 배포 전 진행하는 QA |

Original: https://www.notion.so/STEP-2-OPOA-DB-5bb09dbf9540401084ef1ea19f79086e

- ▶ 목차 리스트

#  문제 정의 및 서술. Problem Statement
> 💡 1. 문제 상황 해석 및 문제 정의
2. 타겟(고객)이 가진 문제를 해결해줄 수 있는 가설
3. 목표 지표와 위 일을 통해 배울 수 있는 점

  ---
  **[문제 상황 해석]**
  - 1차 완료 퍼널 제거됨
    - 현재 OPOA(원페이지 원액션)으로 구조를 변경하며, 지원 중 퍼널이 사라지고 해당 퍼널상태에 연결된 지면들도 함께 노출되지 못하는 상태입니다.
  - 브라우저 로컬 임시 저장
    - 기기가 변경되는 경우 작성 중인 지원서가 날아가는 경우 존재 (현재 핵클 지면 상 B안의 2차 view to 2차 완료 지표가 깨지는 이유 중 하나로도 영향이 있을 수 있음)
  **[문제 정의]**
  - DB 저장이 되지 않아, 기기변경시 작성 중인 과정이 모두 날라갈 수 있음
  - 지원 중이 아닌 지원 시작 퍼널을 임시로 씀에 따라, 지원 중에 해당하는 플레이들을 할 수 없음
    - 지원 중 to 지원완료의 `2차 view to 2차 완료`
  **[가설]**
  - ▶ 참고자료: [아이디어 불패의 법칙] 정리
    - XYZ가설.
    - [아이디어 → 시장 호응 가설 → XYZ가설 → xyz가설] 순으로 점점 구체화.
    - 시장 호응 가설: 시장이 아이디어를 어떻게 받아들일지에 관한 핵심 신념, 가설, 상상. 
    - XYZ가설: 적어도 X퍼센트의 Y는 Z할 것이다. 
    - `xyz가설`: 보통 y를 줄임. 범위를 축소하여, ‘지금 당장 실행 가능하고 검증 가능한’ 가설을 얻는 것. 과감하게 축소해야 하지만, 표적시장에 대한 대표성을 갖도록 유의.
    - 예시
  - DB저장 및 지원 중 퍼널을 OPOA 구조에 적용하게 되면 지원시작 to 제출완료 전환율이 20%이상 증가할 것이다. (2차 view to 2차완료 10%이상 증가)
  **[목표 지표 & 기간] **
  *타겟 기반의 지표 설정을 통해 성공 지표와 가드레일 지표를 설정합니다. 
액션의 기간을 미리 설정하고 성공/실패에 따른 배운 점*
  - 액션 효율 측정 기간: 2024-08-19~2024-08/26
  - 현재 지표
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
  **DB 저장**
  - 입력한 내용이 **브라우저 로컬 임시저장이 아닌 DB에 저장**되었으면 좋겠어요.
    - 지원자가 제출을 하지 않아도/기기가 변경되어도 입력한 값이 남아있도록
  **지원 중 퍼널**
  - 지원 중 퍼널이 생겼으면 좋겠어요
    - 지원시작 당시 트랙 + 기수값을 받아오고 싶어요.
    - 이어서 지원하기 > 지면을 복구하고 싶어요. (STEP 1에서 논의되었던 내용)
  - context 변경
    https://prod-files-secure.s3.us-west-2.amazonaws.com/83c75a39-3aba-4ba4-a792-7aefe4b07895/5daf931f-029c-44af-82b4-3aad3a4b5569/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVBKU6M2%2F20250911%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250911T142718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCjFtJkPG1u4%2Btk7d%2BbwQdV0PZHQpAlDADhkPWBJuPw9QIhAMqNw7BTVB%2FIhbA7K8YYr1hi9yDoFB00FZ0ZceACD1TpKv8DCBcQABoMNjM3NDIzMTgzODA1IgwNIHC%2BBYhrCm%2Bjyowq3AMA5lOYC4Uz6OcogPYokaHCTohATrcJNP289CUaLNfl4EcjnzmuYvHjSeczUxyx4YHxZxE5%2B3CT95ii8BjPzSkbaPs%2BXoO7nFW0A1D4ghy78VuBdpwSGxoTHxMmsQ0OkMgWmiky1bj4I5VpfOTDpwbPfEhMIA43DNo6t53m8mq0y5sNGpIO55WYaK6CRtFfEWekeNvYn1Jast9khJ5LdsLTrq%2Bfx1EVMd84ohQ5EV4X00aSuqvleafh%2BthRFm0qFTipqiqozlw1TRKe8fWPPq7AoRdtDDygTAQw4aGTOmsogSO11uaJaLgTvD4OlTRtNkivkB2YRN31dnHF510NJn4RLXRQmOjB0qLdVjkk2Tn%2ByO9Y4uq4hlE046FeJ6OuxX%2BLKWwy%2BbkcHZsllRXYf9T7Vg%2FkDApKLfvGaz9qW7GSUFOc5rXqPEZasbQK7sx1MsnCeCBablo8hQG2Qy%2FkFbZQYW6LdqwGgVT2ot2pb2SEYA0tomss2q7IQcqzhKUZa9uUVG8WbbR0O39W9YxRQe9MLZGP1FkUM98MOe5T6lSwGRCAY9slqO8hLMmxH6Esjo%2Ft94RFQUHKCieXI27S5WsiPfIFFsTwHD1RzSVF0IUT54qp1VWO%2BJRG%2BAAMnDCoqYvGBjqkAXNj%2FCs4Z3g5FwtbG1qJ3Kiy2VS5UEGexnItRah0rN6LA8WqZDhe%2B627x%2F0eflL3hx0LR8cgcPP5YpbhzBpabM7%2Bz87WLB8cgdFEPABHCXnHDYM4IYaXnkWMwdb5IqsJwoIBOwol9cbNNIPtaiSAfLqulPcJRuNeOu%2BJcJPQpZSteNstywW6r%2FwQStKYjKJNxY9CPRmcPHVatbxqvLhuasc8QbYy&X-Amz-Signature=ae7b8cf6ba06f1858603772368e22f798819c4901bffb482a40733c71f5778ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
    - `context 변경` 1차 서류완료 ⇒ 지원서 작성 중
    - 퍼널명
  [필수 사항] 
  *기획 방향성에서 필수적으로 디자인/개발이 필요한 내용 작성*
  - [ ] **로그 기존 내용으로 남기기 **
    - 신규 로그 X, 기존 ap1, ap2 로그들로 유지
  - [ ] (QA)마케팅 머신 연결 확인
    - [ ] @mention
  [선택 사항]
  *기획 방향성에 가장 영향이 있진 않지만 디자인/개발적으로 챙겨져야할 내용 작성*
  - [ ] 
  [고민 사항]
  *기획 방향성에 고민이 되는 부분에 대한 내용 작성*
  - [ ] 

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
  @이승수(PM팀) @박지영(PM팀) @정수정(CX팀) 
  TC 작성 위한 QA 체크리스트 
  - 현황
    - ▶ OPOA ABT로 테스트 기간 중, 유저는 2가지 케이스가 존재
  - to-be
    - ▶ OPOA 테스트 승리로 `“지원서 작성 중”`이라는 큰 범위의 context 생성 및 기존 1차서류완료,2차 미지원~~가 지원서 작성 중 context 하위 퍼널로 이동
    [체크해야할 점]
    - OPOA 기간 중 A안의 1차서류완료 context에 체류하는 인원들이 “지원서 작성 중” context하위로 이동하였을 때, 자기소개서 페이지로 잘 이동되고 제출까지 되는가
    - OPOA 기간 중 B안의 지원시작 context에 체류하는 인원들(2차까지 서류를 제출하지 않은 인원들)이 이어서 지원하였을 때, 지원서 작성 중이라는 context로 잘 변경되는가(?)
    - 마이페이지 및 허브에서의 정책 (이어서 지원하기)상 문제 상황이 없는가
    - 데이터 정합성에 문제가 없는가 → 퍼널 title이 정확해야 대시보드상 문제가 없다.
    - `질문` to @오유진(개발팀) 
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
