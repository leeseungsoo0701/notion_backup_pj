---
created_date: 2024-09-09
id: d9d5e642-20e2-41cd-8958-f73b69bbe648
url: https://www.notion.so/enrollment-LMS-d9d5e64220e241cd8958f73b69bbe648
perf_flag: yes
importance: 5
summary_5lines:
  - 1. 문제 상황 해석 및 문제 정의
  - (2) 목표 성과(Outcome)
  - [문제 정의]
  - 최초 프로젝트 시작 당시 설정한 기대효과 대비 실제 성과가 어땠는지 기술해주세요
  - 일반적으로는 BAU 퍼널 데이터를 기준으로
---

# 2024-09-09_[내배캠-전환] 사전캠프 참석 응답 페이지(/enrollment) 개선 → LMS 접근성 고도화

| Property | Value |
| --- | --- |
| created_date | 2024-09-09 |
| id | d9d5e642-20e2-41cd-8958-f73b69bbe648 |
| url | https://www.notion.so/enrollment-LMS-d9d5e64220e241cd8958f73b69bbe648 |
| perf_flag | yes |
| importance | 5 |
| summary_5lines | |
|  | - 1. 문제 상황 해석 및 문제 정의 |
|  | - (2) 목표 성과(Outcome) |
|  | - [문제 정의] |
|  | - 최초 프로젝트 시작 당시 설정한 기대효과 대비 실제 성과가 어땠는지 기술해주세요 |
|  | - 일반적으로는 BAU 퍼널 데이터를 기준으로 |

Original: https://www.notion.so/enrollment-LMS-d9d5e64220e241cd8958f73b69bbe648

- ▶ 목차 리스트
- ▶ 초기 기획 히스토리

#  문제 정의 및 서술. Problem Statement
  > 💡 1. 문제 상황 해석 및 문제 정의
2. 타겟(고객)이 가진 문제를 해결해줄 수 있는 가설
3. 목표 지표와 위 일을 통해 배울 수 있는 점

    ---
    **[문제 상황 해석]**
    *일반적으로는 BAU 퍼널 데이터를 기준으로
그 외에도 데이터 포인트, 정성 인터뷰 등. 즉 기획 배경을 숫자로 나타내주세요.*
    - 지원자가 사전캠프를 처음으로 인지할 수 있는 `/enrollment` 페이지 내에서 사전캠프가 무엇인지 소구 되어있지 않음
    - 보험가입 동의 페이지 이후 사전캠프 참석 응답하는 페이지가 존재
    - 사전캠프에 대한 정보를 명확하게 줄 수 있는 창구가 사전캠프OT 문서밖에 없는 상황임
    - 사전캠프 참석으로 응답한 지원자들 조차 사전캠프 운영되는 시기에 별다른 일정이 없어서, 필참이기에 참석으로 응답했으며 관여도가 크지 않음
    - 사전캠프가 진행되는 장소인 zep 접근이 어려운 문제
    - ▶ 부분참여에 대한
    **[문제 정의]**
    *문제 상황에 대한 정성, 정량 데이터를 활용하여 다각적으로 해석한 문제를 하나로 정의해주세요.*
    - 지원자가 지원하는 과정에서 사전캠프에 대한 안내 및 인지가 부족한 상황, 이를 휴먼 터치로 대응하고 있어 코스트가 크다. 
    **[가설]**
    *목표하는 타겟과 가설의 액션에 문제가 해결될 %를 예상합니다. *
    *ex. 적어도 X퍼센트의 Y(타겟)는 Z할 것이다.*
    - ▶ 참고자료: [아이디어 불패의 법칙] 정리
    - 
    **[목표 지표 & 기간] **
    *타겟 기반의 지표 설정을 통해 성공 지표와 가드레일 지표를 설정합니다. 
액션의 기간을 미리 설정하고 성공/실패에 따른 배운 점*
    - 액션 효율 측정 기간: 
    - 현재 지표
    - 성공 지표
    - 가드레일 지표

    ---

#  기획안 (executive summary)
  > 💡 요구 사항: 문제 상황을 아래 기획으로 해결하고자합니다.

    ---

### 디자인 우선순위
    > 💡 필수적으로 드러났으면 하는 포인트, 카피와 선택적으로 녹였으면 하는 부분을 구분하여 작성하고 디자이너와 논의하여 합의합니다.
    **[필수]**

    ---

## 사전캠프란? 
    - 온라인 메타버스 zep (이미지)에서 본 캠프를 위한 리허설이에요. 
    - 날짜 : {기수정보  - 사전캠프 일정}
    - 평일 오후2시부터 4시

### 사전캠프에서는 이런걸 해요
    https://prod-files-secure.s3.us-west-2.amazonaws.com/83c75a39-3aba-4ba4-a792-7aefe4b07895/2069d4ab-6fd7-4cb9-8aa5-6821728f4488/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-09-11_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_7.18.12.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WD5IUVG%2F20250911%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250911T151930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCirNWP2zyVBENrz%2FBuf1PKo7kKrzVCuxjqGCNkyV00aQIgQ%2BXQsDfNEnNoOwuLrIfKioxliQOlscgqcilCbTlCzIUq%2FwMIGBAAGgw2Mzc0MjMxODM4MDUiDI322x2nIhg%2Bksbi%2BSrcA%2FBG00rgVDbTi0RnMtlPhm%2B%2BHYiHqXMINEOqi56IyKjabChmJSaK2F%2FfmzqQVLdYXaJFwO7DwlVjsthmXQiFdahYqTsaDu3i63qTxZMAl5l2vkXVfCs9bUs0B51%2B%2BKtvyFmg498Foi7xTsY6Xkj0FKIUSYQlWUQtSODDgUSohe1Oz67E11dDAttkE95Hw7a0ucysZM7tzUNk%2Fctmyunt%2FRcCsUO4Xq5qnLXH2xJdjKuSDnqbMFnwZUAD0Lrecxn4iNWsFR%2F%2FtQZtOgxfg16jUQWowpGQmJE26gI0iDVlFH6Ygekob2freCWhWSWNzGPr0v7v07jDfCANnvoQgARgwPWYdeZ8XnWfGtd1mYcTP1qGoIzPbNw6XSPbjhAXrjqtojo0CxReLX5DA6DwsmuryKYz%2BBX9rUfYw3QaS24yquZuFxcOGP2TKRv0Xs13lgPX0h15%2B%2BJKOQzxF%2FJEsramEQfdhhSOAE6xrhijLbyP1wE0T2Rtk5W0jI8MlDaAv86xtan26uOnMjNmqlnYKn%2F82R%2FeKTxpo8lFdH7M3SxLNObbYeWR6RLMASNiWNbQO%2FLomPfUs7h2bE8F9QWauplbLIfQhHwTZ7e8lO9a%2BArbQNgo6dmbl2gR3XJ0XWdEMN7Ii8YGOqUB4AUXS5oPYtXtyGHKpk0eT2qS01Ek0lY6oJs8ScddchsMPfmIn%2Fuw3hz4x%2FFrjMzYkzjdZmtvwHNhPHA5BiG3hBoJPr2sySn6t17D9FtwxR6x%2F%2BL3HLZlPXyZkptoyBkbvFvNOvg7bpAZtQ9uzjF%2FEe2Q91bjSMmr0FOGn2CDzM85Kw7FXE1yL8PgrVBBHiBRKbDP7HDZ1B5DXFxDKJfJt0S7nfPZ&X-Amz-Signature=71469ed1a27414e9527becac7995893250c2a5a9a710d05ee7c15ab94f5bf182&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject

### 사전캠프 참석여부를 제출해주세요. 
    - [ ] 참석
    - [ ] 미참석
    ⇒ 참석을 눌렀을때, 사전캠프 참석하기 링크로 이동


    ---
    **[선택]**
    - 상기 컴포넌트 재활용 가능할지
    [추가 고민 포인트]
    - PM
    - 디자이너: 

    ---

### 개발 우선순위
    - ▶ 의사소통이 어려울 때, Maker가 개발적 우선순위를 판단할 수 있게 메모합니다.
기획 중요도가 높은 항목부터 내림차순으로 정리합니다.
미리 발전 방향을 제시해, 초반 설계에 도움을 줄 수도 있습니다.
    - 지급강의 연결or 기수정보 내에 zep 링크 삽입가능
    **[기능 명세서 작성]**
    - ▶ 예시

# [0] Why

---
@mention 
@mention 
- 사전캠프 필참하게끔 세일즈하고 있으나 사전캠프에 대한 안내는 트랙별로 상이하게 나가거나 나가지 않고 있음.
  - 사전캠프 참석으로 응답한 인원 `타겟` 
    - 사전캠프에 대해 인지하고 있지 않으나 당일 미입실 한 경우 처음 담임매니저의 연락을 받게 됨 (최초 1회-슬랙DM, 2회-유선연락/문자)
    - 
    - 매니저의 연락을 받고 사전캠프에 왔다면, 슬랙 내 책갈피 내에 있는 링크를 통해 zep 에 참석 해야함
    - 온보딩 완료 지원자의 CTA
  - 사전캠프 미참석 응답한 인원
    - 사유가 있거나, 세일즈매니저가 사전캠프를 이미 세일즈 한 경우
    https://prod-files-secure.s3.us-west-2.amazonaws.com/83c75a39-3aba-4ba4-a792-7aefe4b07895/f68238ee-8b1a-416b-a1e4-95c28bb1590c/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-09-25_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_9.51.14.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZUP6NG4%2F20250911%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250911T151931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHlJcjYzV5bR8btoESsmGG8s8%2BQCT3T7ytyvQ%2BWJSQxWAiA5P5CKnjV2SSDsBIELIME6epdR868BTp5mSFRYplGtSyr%2FAwgYEAAaDDYzNzQyMzE4MzgwNSIMAnDtOciLj0v5DM0mKtwD%2BUZcWkHghpDN5P55DG2fJIzRGxj5jd7U1LilOhrOe%2Bs9iIYlWZEWj22xi7FYY5PU3YdzhfkE1tWlaS4QpD8R7C1HVYmK2s5kR%2BLd%2Bh1pxYb0%2FzdIBri4dZSJDODvbIL3PDi8PYnbrQrHROaATjW%2BNVQdJS6CPgStM5pYQXFX4yQV0n9TEeUOOcatt1hjfgW9NdqvPrL9mlVYT1PVYSjfC1%2BgCaW067o0CEaEluT%2B3BU2%2BZ70cqughKKSWTEahkz5oMnswBGHWR%2BfvaPDfor5MGI5dFsD9xC4lSpAQOAis78Q3ENJqmK%2FMlMNaaXFK%2F8R8iEdnf%2BYytc6yA7pq2EEQUBJyUckKSMh6bjx1MhQ06OO4%2FPzUzhy2bHGzpxbKPuQ4CKCJsVhYpmDJI9WBAvWvLl2wHXKhYa%2BiW%2FgBY6kCt9%2BZHnj%2FhPAEP1ZD0n%2FqF3UUJS6RaCxwWtgS2D5NmHP3S4Hk8G0UOj%2BbCpTcty1p3M77ih2g52kJjyA3ZQDBEM8%2Bvtv%2F%2Fdnl2gFn1LhGZBvVq%2FnMkSAiXWIZWRiTL0tyE%2BhPMvN6J3f1X4VKAyis9KJDKJ5GMAIiZiGdzkIPyLe%2BaEa4ij%2FOZB0IvuiFfhdBfSVlEAqBQSZS5wx3p8wu8eLxgY6pgF3athDJLcUmtFAxTCVIP%2B9vxOJx1E2BTkVyiJioEjAp4TE9KpOU3KsI5c6v9VL6BBWaeih%2FtJl%2F5n%2FdSr1oR3ec3Uq9W0W%2BtHVHfIgPB1I60iLBIpeY31cAbjpAQjbU05eeKwaGcBQkRgYcWFNFCVva0EFBNlWFSsSyDQTcms9lOKHsOB8uy%2Bfo2XEYq5ukek7pYeqAxXRDMPPeINYMrs8aSsxVLma&X-Amz-Signature=0aa70da1f11afc67e2d5758daaefdf966472173ddc2762ab82aca05ce17cab72&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
  ⇒ 사전캠프 미응답/False 응답한 경우에는 세일즈라는 휴먼 터치가 존재, 사전캠프에 빠
  여주님의견) 사전캠프를 신청하고 나면 슬랙에서 워크플로우 작동하고 LMS 로 안내, LMS에 모두 모아 둔다. 
  사전캠프만 대응가능하게 모바일 접속도 가능하게 바꾼다. (CRM 대응시에)
**[문제 상황 해석]**
*일반적으로는 BAU 퍼널 데이터를 기준으로
그 외에도 데이터 포인트, 정성 인터뷰 등. 즉 기획 배경을 숫자로 나타내주세요.*
- 
**[문제 정의]**
*문제 상황에 대한 정성, 정량 데이터를 활용하여 다각적으로 해석한 문제를 하나로 정의해주세요.*
- 

# [1] Goal

---

## (1) 프로젝트 산출물(Output)
*이 프로젝트를 통해 산출되어야 하는 결과물은 구체적으로 어떤 내용인가요?*
- 

## (2) 목표 성과(Outcome)
*이 일을 통해 달성하고자 하는 것은 무엇인가요? *

### **1) 가설**
*목표하는 타겟과 가설의 액션에 문제가 해결될 %를 예상합니다. *
*ex. 적어도 X퍼센트의 Y(타겟)는 Z할 것이다.*
- ▶ 참고자료: [아이디어 불패의 법칙] 정리
  - XYZ가설.
  - [아이디어 → 시장 호응 가설 → XYZ가설 → xyz가설] 순으로 점점 구체화.
  - 시장 호응 가설: 시장이 아이디어를 어떻게 받아들일지에 관한 핵심 신념, 가설, 상상. 
  - XYZ가설: 적어도 X퍼센트의 Y는 Z할 것이다. 
    - X: 우리는 얼마나 큰 조각, 그러니까 표적 시장의 과연 몇 퍼센트를 차지할 수 있을까? 
    - Y: 우리의 표적 시장이 뭘까? 
    - Z: 표적 시장은 우리 제품에 어떤 식으로, 정확히 어느 범위까지 호응할까? 
  - `xyz가설`: 보통 y를 줄임. 범위를 축소하여, ‘지금 당장 실행 가능하고 검증 가능한’ 가설을 얻는 것. 과감하게 축소해야 하지만, 표적시장에 대한 대표성을 갖도록 유의.
  - 예시
    - 아이디어: 대기오염 모니터링, 오염 탐지기 판매. 
    - 시장 호응 가설: 심하게 오염된 도시에 살고 있는 일부 사람은 대기오염을 모니터링해서 피할 수 있게 도와줄 합리적 가격의 장치에 관심을 가질 것이다. 
    - XYZ가설: 적어도 10%의, 대기질지수 100이상인 도시에 사는 사람들은, 120달러짜리 휴대용 오염탐지기를 구매할 것이다. 
    - `xyz가설: 적어도 10%의, 베이징 토드 아카데미 학부모는, 120달러(=800위안)짜리 휴대용 오염 탐지기를 구매할 것이다. `
- 

### **2) 목표 지표 & 측정 기간**
*타겟 기반의 지표 설정을 통해 성공 지표와 가드레일 지표를 설정합니다. 
액션의 기간을 미리 설정하고 성공/실패에 따른 배운 점*
- 액션 효율 측정 기간: 
- 현재 지표
  - 
- 성공 지표
  - 
  - ▶ 성공 목표에 달성하게 된다면 우리는 무엇을 배웠고 앞으로 방향성이 어떻게 될까요?
    - 배운 점:
- 가드레일 지표
  - 
  - ▶ 목표에 달성하지 못했다면 우리는 무엇을 배웠고 앞으로 방향성이 어떻게 될까요?
    - 배운 점:

# [2] 실행 계획

---

# [3] 세부 내용

---
*구체적인 내용을 기록하거나, 관련 문서를 첨부해주세요*

## (1) 기획안 (executive summary)
요구 사항: 문제 상황을 아래 기획으로 해결하고자합니다.

---

### 1) 디자인 우선순위
> 💡 필수적으로 드러났으면 하는 포인트, 카피와 선택적으로 녹였으면 하는 부분을 구분하여 작성하고 디자이너와 논의하여 합의합니다.
**[필수]**
**[선택]**
- 이후 내일배움캠프 워크스페이스 변경을 대비한 추가 기능
  - 기수관리 페이지에서 `슬랙가입가이드 링크` 설정 기능(null 값일 경우 공통 링크 @mention)
  https://prod-files-secure.s3.us-west-2.amazonaws.com/83c75a39-3aba-4ba4-a792-7aefe4b07895/74ee72be-1f87-499e-affb-6c35a6419488/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WEXSNCF%2F20250911%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250911T151936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDXDvLXdzkmZKGhsSlDWUM0EfXa1zhwxHjhTRIxpNhyHQIgfkiFskODcw1uEGPl0LskCGQLBXYSgGFkmMD1BFXx9Toq%2FwMIGBAAGgw2Mzc0MjMxODM4MDUiDDfJ4FUsbexCvcG3%2BCrcA7hDTHwKkhimIHm2xYUHGPx47MIvC8a3UACWkHlSZtV1KxqVAy84MA4oL2u1tEP62OHk1vaNUva2fQ%2FbJ3DjAdOu8DKErfJkZI6PODHmzfmU3W1mR42Gr5cR4CvPdHHu6nXpb6TdrqV1U5yCXdr7DzGGU1K2h4R6R8EM35sGC7mnS9XHklr%2FUnI%2FLYqZ%2BSzo9eJV9qGMr1%2FEcnhfIzEwjjW8c%2BvFzAI4SUha4PoGz%2FKebFuli3ev5IvY42%2BGuq6sI5YodukhVfu42wrbdD96SBoTzei0e5WBrebOX0DLfdyT8%2BGzOkbNEevFFHirgZcVpvWcb%2BnatEBrM4p5RHDgoCr%2B8%2BuVoNSHtS9DlVALOantAfMSI7FJfYrcaMIKsszg5txKMGje3dz14I2hVofT8aDt1YGFv3q%2FEWAEnnfNgS7YxpcIQg42QB1heW%2Fj%2BVgjejyEymaITXCnpnRze9sKy6Q6xLy0fuZPksqenjNSiPhxsxAMByYCKs6E6jlUBPdGspcpo3fs20SwUKmQhDB7Oxod%2FfDxio8QbNF35B9FR%2BGzeGFyhVclcJkhkbWvOGDv7N9qVCcIqzhbR0qGopC3%2Bh%2F4vv8bEFFyR7KDJcRLbypghIqs0wJuJVsc6znUMM%2FIi8YGOqUBEVcDZ0DMXtu1VBpkImmCdJOicEoFVa%2FhgEqOp1UfIeLeUlLD4O6uyqj%2BvA4gqBQF94i7iFcECFtJBlorgY7AwrNC12xu8Xgiar2kmT2dGFq4G7cTIE4fJoxxfx7BK%2BrOyAFDq%2FwrUF6FuUrwCU1vzfAdxFR%2BpYpKfi%2FxN69Hj5rqqznG7ZWt6i71W6iGmJXrtV6Oi9KJQFxRLKdte1m8prQ4ZRgP&X-Amz-Signature=052ac54d76736c64341aeca2bbf3b0a04de09abd1f0fc6072edd79d7af17084a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
**[추가 고민 포인트]**
- PM:
- 디자이너: 

---

### 2) 개발 우선순위
- ▶ 의사소통이 어려울 때, Maker가 개발적 우선순위를 판단할 수 있게 메모합니다.
기획 중요도가 높은 항목부터 내림차순으로 정리합니다.
미리 발전 방향을 제시해, 초반 설계에 도움을 줄 수도 있습니다. `(펼쳐서 예시 확인)`
  ex)
  1. APM이 강의를 직접 제공할 수 있는 기능 구현 자체를 최우선으로 합니다.
  1. 강의 지급에 실수가 일어나지 않도록, 한번 더 확인하는 과정이 필수적입니다.
  1. Alert 대화 상자에서, 지급 내역이 맞는지 확인할 수 있으면 좋습니다.
  1. 추후, 어떤 APM이 어떤 예비 수강생에게 어떤 강의를 줬는지 확인할 수 있는 슬랙봇이 구현되어야 합니다.

### 3) PRD

# [4] 결과

---
*최초 프로젝트 시작 당시 설정한 기대효과 대비 실제 성과가 어땠는지 기술해주세요*

# [5] 회고

---
*“왜 잘 됐을까? 왜 안됐을까?”, “앞으로 어떻게 하면 더 잘 할 수 있을까?”에 대해 깊이 회고해보세요*

## (1) Good: 좋았던 점/배운 점/잘 된 점

## (2) Bad: 안 좋았던 점/잘 안 된 점/개선해야 할 점

# [6] 후속 액션

---
*이 프로젝트의 결과에 따라서 어떤 의사결정이 이루어졌는지, 후속 테스크가 있다면 아래 추가해주세요*

## Databases

### Database: 기능 명세서

| 개발 상태 | 로그  | 메모 및 질문 사항 | 상세 기능 | 생성자 | 예상 개발 소요 시간 | 주 기능 | 중요도 | 페이지 이름 | notion_url |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | {'object': 'user', 'id': 'cc4071e2-a203-4271-a42f-8336081cf383', 'name': '조수진(KDT교육운영팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/a2cebd1d-dda6-41d3-b5fd-67c9692023d8/%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C.jfif', 'type': 'person', 'person': {'email': 'sj.jo@teamsparta.co'}} |  |  |  |  | https://www.notion.so/8af2ec3633524c569e98d87a77d59a03 |


### Database: 기능 명세서

| 개발 상태 | 로그  | 메모 및 질문 사항 | 상세 기능 | 생성자 | 예상 개발 소요 시간 | 주 기능 | 중요도 | 페이지 이름 | notion_url |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | • As-is 100자 이상 작성하면 합격할 확률이 36% 올라요.
• To-be 최소 100자 이상 작성해주세요! | {'object': 'user', 'id': 'cc4071e2-a203-4271-a42f-8336081cf383', 'name': '조수진(KDT교육운영팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/a2cebd1d-dda6-41d3-b5fd-67c9692023d8/%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C.jfif', 'type': 'person', 'person': {'email': 'sj.jo@teamsparta.co'}} |  | 지원서 글자 수에 대한 UI / UX 변경 | 필수 |  | https://www.notion.so/As-is-100-36-To-be-100-d000421b8b364bdbb009926502bde322 |
|  |  |  |  | {'object': 'user', 'id': 'cc4071e2-a203-4271-a42f-8336081cf383', 'name': '조수진(KDT교육운영팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/a2cebd1d-dda6-41d3-b5fd-67c9692023d8/%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C.jfif', 'type': 'person', 'person': {'email': 'sj.jo@teamsparta.co'}} |  |  |  |  | https://www.notion.so/461397e2353f47b5906e74d7d1a50eec |
|  |  |  | 40세 이상 불합격 처리 | {'object': 'user', 'id': 'cc4071e2-a203-4271-a42f-8336081cf383', 'name': '조수진(KDT교육운영팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/a2cebd1d-dda6-41d3-b5fd-67c9692023d8/%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C.jfif', 'type': 'person', 'person': {'email': 'sj.jo@teamsparta.co'}} |  |  | 필수 |  | https://www.notion.so/40-53b3dc6a7f37492e8a11ae86a893c691 |
|  |  |  | 19세 미만 불합격 처리 | {'object': 'user', 'id': 'cc4071e2-a203-4271-a42f-8336081cf383', 'name': '조수진(KDT교육운영팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/a2cebd1d-dda6-41d3-b5fd-67c9692023d8/%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C.jfif', 'type': 'person', 'person': {'email': 'sj.jo@teamsparta.co'}} |  | 서류 불합격 정책 기준 수정 | 필수 |  | https://www.notion.so/19-66abcf2a433d4ea3a8ec01dd43fb9e57 |
|  |  |  | 300자 이상 작성을 넛징하는 메시지 수정
• As-is 300자 이상 작성하면 합격할 확률이 62% 올라요.
• To-be 300자 이상 작성한 분들의 평균 합격률은 91.4% 에요! | {'object': 'user', 'id': 'cc4071e2-a203-4271-a42f-8336081cf383', 'name': '조수진(KDT교육운영팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/a2cebd1d-dda6-41d3-b5fd-67c9692023d8/%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C.jfif', 'type': 'person', 'person': {'email': 'sj.jo@teamsparta.co'}} |  |  | 필수 |  | https://www.notion.so/300-As-is-300-62-To-be-300-91-4-7e570c79aace4a1ba277d3a5b880f9c7 |
|  | nbc_apply2_essay_length_300 (로그에 어떤 내용이 들어가야 하는 지는 로그 정리 노션 링크 걸기) |  | 글자수가 300자 넘은 상태에서 1차 지원 제출 시 로그 추가 | {'object': 'user', 'id': 'cc4071e2-a203-4271-a42f-8336081cf383', 'name': '조수진(KDT교육운영팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/a2cebd1d-dda6-41d3-b5fd-67c9692023d8/%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C.jfif', 'type': 'person', 'person': {'email': 'sj.jo@teamsparta.co'}} |  |  | 선택 |  | https://www.notion.so/300-1-aec5f72a94cf489eb4f6c5ae3636c011 |
|  |  |  | 특정 글자 연속 4번 이상 반복 시 보류 처리 | {'object': 'user', 'id': 'cc4071e2-a203-4271-a42f-8336081cf383', 'name': '조수진(KDT교육운영팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/a2cebd1d-dda6-41d3-b5fd-67c9692023d8/%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C.jfif', 'type': 'person', 'person': {'email': 'sj.jo@teamsparta.co'}} |  |  | 선택 |  | https://www.notion.so/4-d52cbb4f63094e8cb98e7405293db238 |
|  |  |  | 욕설, 비방 문자 포함
- 욕설, 비방으로 판단되어야 하는 문자들 예시: ㅅㅂ, 바보
- 개발적으로 이런 문자들을 필터링 해주는 로직이 있다면 공유 필요 | {'object': 'user', 'id': 'cc4071e2-a203-4271-a42f-8336081cf383', 'name': '조수진(KDT교육운영팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/a2cebd1d-dda6-41d3-b5fd-67c9692023d8/%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C.jfif', 'type': 'person', 'person': {'email': 'sj.jo@teamsparta.co'}} |  |  | 선택 |  | https://www.notion.so/de93f00e32ba4863b986eb73b958911b |
|  |  |  | 지원동기 예시 30자 이상 동일 시 보류 처리 | {'object': 'user', 'id': 'cc4071e2-a203-4271-a42f-8336081cf383', 'name': '조수진(KDT교육운영팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/a2cebd1d-dda6-41d3-b5fd-67c9692023d8/%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C.jfif', 'type': 'person', 'person': {'email': 'sj.jo@teamsparta.co'}} |  |  | 선택 |  | https://www.notion.so/30-e242476bac814ee7a8a5aaff481de164 |
|  |  |  | 지원동기 200자 미만 보류 처리 | {'object': 'user', 'id': 'cc4071e2-a203-4271-a42f-8336081cf383', 'name': '조수진(KDT교육운영팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/a2cebd1d-dda6-41d3-b5fd-67c9692023d8/%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C.jfif', 'type': 'person', 'person': {'email': 'sj.jo@teamsparta.co'}} |  | 서류 보류 정책 기준 수정 | 필수 | 지원서 | https://www.notion.so/200-ef6580199334493992ea40fd4ff44f29 |
|  |  |  | 100자 미만 동안은 제출하기 버튼이 비활성화 상태 | {'object': 'user', 'id': 'cc4071e2-a203-4271-a42f-8336081cf383', 'name': '조수진(KDT교육운영팀)', 'avatar_url': 'https://s3-us-west-2.amazonaws.com/public.notion-static.com/a2cebd1d-dda6-41d3-b5fd-67c9692023d8/%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C.jfif', 'type': 'person', 'person': {'email': 'sj.jo@teamsparta.co'}} |  |  | 필수 |  | https://www.notion.so/100-f8ac90b29ab54cafbbf4cb319d1656b0 |
