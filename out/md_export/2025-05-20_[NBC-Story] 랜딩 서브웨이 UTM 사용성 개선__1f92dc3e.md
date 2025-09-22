---
created_date: 2025-05-20
id: 1f92dc3e-f514-80cc-9e7f-c04487657fc6
url: https://www.notion.so/NBC-Story-UTM-1f92dc3ef51480cc9e7fc04487657fc6
perf_flag: yes
importance: 5
summary_5lines:
  - 한 줄 요약: UTM 수정 → 저장 → 실서버 배포 버튼 활성화 → 정상 배포 되어야 함
  - [문제 정의]
  - 랜딩 서브웨이에서 div/UTM 수정 후 저장을 눌렀음에도 실서버 배포 버튼이 활성화되지 않음
  - 특히, UTM을 저장했을 때 실서버 배포 버튼 활성화가 아닌, 동일한 UTM 항목이 중복 생성됨
  - 이로 인해 실제 UTM 설정이 완료되었음에도, 배포 버튼이 비활성화되고 배포 작업을 완료할 수 없음
---

# 2025-05-20_[NBC-Story] 랜딩 서브웨이 UTM 사용성 개선

| Property | Value |
| --- | --- |
| created_date | 2025-05-20 |
| id | 1f92dc3e-f514-80cc-9e7f-c04487657fc6 |
| url | https://www.notion.so/NBC-Story-UTM-1f92dc3ef51480cc9e7fc04487657fc6 |
| perf_flag | yes |
| importance | 5 |
| summary_5lines | |
|  | - 한 줄 요약: UTM 수정 → 저장 → 실서버 배포 버튼 활성화 → 정상 배포 되어야 함 |
|  | - [문제 정의] |
|  | - 랜딩 서브웨이에서 div/UTM 수정 후 저장을 눌렀음에도 실서버 배포 버튼이 활성화되지 않음 |
|  | - 특히, UTM을 저장했을 때 실서버 배포 버튼 활성화가 아닌, 동일한 UTM 항목이 중복 생성됨 |
|  | - 이로 인해 실제 UTM 설정이 완료되었음에도, 배포 버튼이 비활성화되고 배포 작업을 완료할 수 없음 |

Original: https://www.notion.so/NBC-Story-UTM-1f92dc3ef51480cc9e7fc04487657fc6

> 💡 
    > 💡 아래를 기준으로 `기획 및 실험의 핵심 가치`를 설정합니다.

# [0] Why

---

### 0) 문제
**[문제 상황]**
- 문제를 겪는 유저: BAU 랜딩 운영 담당자 (브콘팀)
- 문제 상황:
  - 랜딩 서브웨이에서 div/UTM 수정 후 저장을 눌렀음에도 **실서버 배포 버튼이 활성화되지 않음**
  - 특히, **UTM을 저장했을 때 실서버 배포 버튼 활성화가 아닌, 동일한 UTM 항목이 중복 생성**됨
  - 동일 `utm 값(aideveloper_test)`이 2개 생기며, 모두 `상태 ON`으로 표시되어 혼란을 초래함
  https://prod-files-secure.s3.us-west-2.amazonaws.com/83c75a39-3aba-4ba4-a792-7aefe4b07895/f43e5b13-8fa4-4e9e-a00c-4204906efe44/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-05-21_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_3.14.05.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662O7X3MA2%2F20250912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250912T014648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCferQEEmdBgT0CNftmKj75iQH3mPLzLUCTyE5ccqFc2gIhAMuKlMOJXJYWqE%2BZTgIbuwSExZn7Gl3mrVX0mkVEPqSaKv8DCCMQABoMNjM3NDIzMTgzODA1IgxRtu98Keg3zs84sgkq3ANO157hdYzn04CpZo1NKQRJfqZFKo6aNsc66peucve5yWGBsVb8AHHucee0iIv4HKFIgwj1EWkvdy0HMBHjH22vo41cucatDcID1SZzMqBoFr2tzIcMjCG323jFeP8WFLAdwvI6ICc0Uui5t6JLhOA4e4kvgFIUc3D1occsg96vj%2FtWAAIRnhas%2B30OUt2KmRRYt%2BejXMEx2BkzaLPz1f%2FnDmkaPcmnWtHLikZqMjoFdXi%2BVAe34tXweIbly%2BsoMlh%2FKm9glcZoS13J%2BjfrafA3PsmNBWH9Suq7Hhj7lo3s2ZXpLpCaBjDJ4odPsOuRbgZ6WlJMkFC2j9rYAy9RJpTl%2BSUkvaxXdijdVkSFm91yi7FL8zztbX5tyigF4UILYz3Mm0DgHs5WoFSDQJojfrsAjr72Y9MEBqmftHmNVRiv07Ror3zBKzrxoPRCc0aO7QDSV%2BdAmGzBVGvRfNsgoVxLdd3W1wA1e9Z1seCC%2FFOPluE5%2BhBrAv2Xilu9VQC%2BRxinXXpd47rpY2JK33Wyq6U%2FYwOhVSx0kg%2BQekSJD3cH9rVn%2BW9NqQ3EmkdHxHgCVdpzoIkKwzUt6fjXAOqviL54mR%2FduhEO2WGl8KqQyDaAgaTJtGZjJBlASFNuXjCy8I3GBjqkARgZzb7wLt8fPs77jjnuyZ3Bwi5OEtWIrvy8A08wG0PgjknFtzCKA3mATCpkfacUOdzkw7JTQPMG7l4vlP%2BW7VqbQrfStjuO%2Bv6elvdp8ctOiGOiVVzPv%2Bs23O39qcye0RwL7VHMUsQPcEOWW%2FbASSgGByKwoyNYrpUWLwtBvKaNndnUcfKyAyuoOE0auB4aIiWzOqC6pcQaWZmFeD5d5dL9X7y4&X-Amz-Signature=9b029f0fe971e20401dce546115b134545bbd88f22931f77c90a3aa001e99320&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
**[문제 정의]**
- **UTM 저장 버튼의 기능이 실서버 배포 조건 변경을 트리거하지 못하고, 비정상적인 UTM 항목 중복 생성으로 이어지는 구조적 결함이 있음**
- 이로 인해 실제 UTM 설정이 완료되었음에도, 배포 버튼이 비활성화되고 배포 작업을 완료할 수 없음

# [1] Goal

## 상세 기획안 (executive summary)
- 랜딩 서브웨이에서 UTM 수정 후 저장 버튼을 눌러도 실서버 배포 버튼이 활성화되지 않으며, 대신 동일한 UTM 값의 row가 중복 생성되는 이슈가 발생하고 있음. 
- 이로 인해 정상적인 배포가 불가능해지고, 반복 저장 및 협업 요청이 빈번해지고 있어 시급한 개선이 필요함.

## 프로덕트 디자인
- ▶ **1️⃣ 플로우 1번: UTM 수정 및 저장 후 실서버 배포**
  한 줄 요약: UTM 수정 → 저장 → 실서버 배포 버튼 활성화 → 정상 배포 되어야 함
  - 1-1: 정상 플로우 (예상 동작)
| step | 액션 | 시스템 응답 |
| --- | --- | --- |
| 1 | UTM 항목 수정 또는 신규 입력 |  |
| 2 | 저장 버튼 클릭 | 기존 UTM 항목 덮어쓰기 / 상태 변경 감지 |
| 3 | 실서버 배포 버튼 클릭 | 정상 배포 |
  - 1-2: 버그 플로우 (문제 발생 상황)
| step | 액션 | 시스템 응답 |
| --- | --- | --- |
| 1 | 기존 utm 값 수정 후 저장 | 동일 utm 값 중복 생성됨 (ex. aideveloper_test 2개 존재) |
| 2 | 실서버 배포 버튼 비활성화 유지 | 배포 진행 불가 |
| 3 | 반복 저장 / 별도 문의 필요 | 작업 비효율 및 커뮤니케이션 비용 증가 |

# [2] Review & Learning

## Story 회고 및 러닝 정리
- 액션 효율 측정 기간: 
- 액션 전 지표
  - 
- 현재 지표
  - 
- 얻은 러닝
  - 
- 그 외 논의사항
  -

## Databases
