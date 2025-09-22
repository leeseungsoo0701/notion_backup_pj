---
created_date: 2025-03-13
id: 1b52dc3e-f514-80fc-a178-cebab09f8388
url: https://www.notion.so/Kotlin-CRM-MMS-1b52dc3ef51480fca178cebab09f8388
perf_flag: yes
importance: 5
summary_5lines:
  - [2] 성과 공유
  - 액션 효율 측정 기간: 배포 후 1주일 (검수 기간 2-3일 제외)
  - 문제를 겪는 유저: 리워드 지급 CRM을 수신받는 백엔드 트랙 퍼널 체류자
  - [문제 정의]
  - 최초 프로젝트 시작 당시 설정한 기대효과 대비 실제 성과가 어땠는지 기술해주세요
---

# 2025-03-13_[Kotlin] 리워드 CRM 알림톡, MMS 분기 실험

| Property | Value |
| --- | --- |
| created_date | 2025-03-13 |
| id | 1b52dc3e-f514-80fc-a178-cebab09f8388 |
| url | https://www.notion.so/Kotlin-CRM-MMS-1b52dc3ef51480fca178cebab09f8388 |
| perf_flag | yes |
| importance | 5 |
| summary_5lines | |
|  | - [2] 성과 공유 |
|  | - 액션 효율 측정 기간: 배포 후 1주일 (검수 기간 2-3일 제외) |
|  | - 문제를 겪는 유저: 리워드 지급 CRM을 수신받는 백엔드 트랙 퍼널 체류자 |
|  | - [문제 정의] |
|  | - 최초 프로젝트 시작 당시 설정한 기대효과 대비 실제 성과가 어땠는지 기술해주세요 |

Original: https://www.notion.so/Kotlin-CRM-MMS-1b52dc3ef51480fca178cebab09f8388

- ▶ 목차

# [0] Why

---

### 0) 문제
**[문제 상황 해석]**
*타겟 유저와 문제로 나타나는 상황을 숫자로 나타내주세요.*
- 문제를 겪는 유저: 리워드 지급 CRM을 수신받는 백엔드 트랙 퍼널 체류자
- 문제 상황: 
6회차 기준 
= 나 리워드 안내 CRM 못 받았다!  (안내성으로 보냈는데)
(모집마감 15일 전 -> 마감 직전에 들어왔을 경우 놓쳐지는게 많았음 -> 마감 play로 수동 crm과 함께 액션되어 놓쳐질 가능성 up)
= 경향성
- 리워드 수령
  - 2차서류완료 : `73.9%` (184명 중 136명)
  - 슬랙가입완료 : `82.4%` (153명 중 126명)
  - HRD등록완료 : `84.4%` (122명 중 103명)
- 리워드 수령 to 결제 전환
  - 2차서류완료 : `47.8%` (136명 중 65명)
  - 슬랙가입완료 : `56.3%` (126명 중 71명)
7회차는   
https://prod-files-secure.s3.us-west-2.amazonaws.com/83c75a39-3aba-4ba4-a792-7aefe4b07895/0b39d144-bba4-4fc9-bfa9-c69f69119670/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WSULH3Q%2F20250912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250912T005027Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHXuGpD%2B7r1cW9iurbrUM2YXWcqZtwr1ZpzPC0Gtqib8AiAdyp84M6FPIxgIbbrLxKFEhBEwwKlLj9GAUhCbVS3QYir%2FAwghEAAaDDYzNzQyMzE4MzgwNSIMt6Pu3JJk6%2F6VmM%2BbKtwDGjEgLsaQCES8mtn29%2B4YR0nLtW%2BPC1Vy8vRyl2Crb6pFY9xKPlDOihPFN1sx5CGBEgSI%2BZvmlWpIDmSz4hqPXxDUVnlKco%2BHqBO%2BXFKocsSSV6ey9HgTTg85o038eZfQwKdCzob3JfG997%2Fbp6uQtUfAMPmZZZCU6tvBL9RF%2B3SjzqDbnj1Ndow2m1O2iRBOEZOdn3Y%2F6GoJ1QWtGkp3oMDH15xTMVZw97smndsjCFGPqdxsJ0vy2Cqr1adqEYaYTJgnWx9osP0LGlogX1E1vrLHINn50KjNtGSiTv6yTB3cqVFKZw5cUt4lPG1on%2BFMyKiv9%2BzFEuBj8j40c0LxemvDFWPmg7BZYTp%2BNDh0Gm8re1C7Yx8PDKkM%2BDhcJJyRiD62STcIBd1hHuZIELLw7GSy8PB8%2Fv5bww6q6vylsSLNW%2B1npZRPiZ%2FKrD045HQMp4sIcrDxBa0bzQIMGEbbE3vs5pIYOfkcjSr7a%2BwzLVMjupCZMPx1OOBuPtqEY5dvZNc%2FDcLOeil7r2vzniha8alcMlbx%2B%2BhjIvgIJBkqHoqGnYyzv0Ee2gAxOwQbnSvPiJC4UbT%2FpB1ZP6fwTf5pQDafV7vcVXRiJKPoEOjQD%2BE7OjV8e2NY8LPS%2BIswwNCNxgY6pgH9ogBIE7aiYwTEIs6KqUKnzDPXsh%2BlLpwkm4yKHJ2L1d4sBlz6fLK7P72cd%2Fg9jbGfQnymifDVImj8H%2FR8ZSMNldBRH9eTGtz1grfwW1R5T9vUviGEi5gF1PI%2FWydmCDCp3J66TTPGT2fwBF%2BVOdUyXpcTvX4bnPwYj5xRSsnFHjka7xKZ7lq8WDc0j%2F3cvOD%2F0IGDIvNNyvwh%2FD%2BVnfyP4QwFFe2z&X-Amz-Signature=318a6b209673ee26b43b01bda088837de2c30689f50ab599c5c575599fe5a3d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
https://prod-files-secure.s3.us-west-2.amazonaws.com/83c75a39-3aba-4ba4-a792-7aefe4b07895/02cbb126-0eda-4420-a6ab-35c9116f4284/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WSULH3Q%2F20250912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250912T005027Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHXuGpD%2B7r1cW9iurbrUM2YXWcqZtwr1ZpzPC0Gtqib8AiAdyp84M6FPIxgIbbrLxKFEhBEwwKlLj9GAUhCbVS3QYir%2FAwghEAAaDDYzNzQyMzE4MzgwNSIMt6Pu3JJk6%2F6VmM%2BbKtwDGjEgLsaQCES8mtn29%2B4YR0nLtW%2BPC1Vy8vRyl2Crb6pFY9xKPlDOihPFN1sx5CGBEgSI%2BZvmlWpIDmSz4hqPXxDUVnlKco%2BHqBO%2BXFKocsSSV6ey9HgTTg85o038eZfQwKdCzob3JfG997%2Fbp6uQtUfAMPmZZZCU6tvBL9RF%2B3SjzqDbnj1Ndow2m1O2iRBOEZOdn3Y%2F6GoJ1QWtGkp3oMDH15xTMVZw97smndsjCFGPqdxsJ0vy2Cqr1adqEYaYTJgnWx9osP0LGlogX1E1vrLHINn50KjNtGSiTv6yTB3cqVFKZw5cUt4lPG1on%2BFMyKiv9%2BzFEuBj8j40c0LxemvDFWPmg7BZYTp%2BNDh0Gm8re1C7Yx8PDKkM%2BDhcJJyRiD62STcIBd1hHuZIELLw7GSy8PB8%2Fv5bww6q6vylsSLNW%2B1npZRPiZ%2FKrD045HQMp4sIcrDxBa0bzQIMGEbbE3vs5pIYOfkcjSr7a%2BwzLVMjupCZMPx1OOBuPtqEY5dvZNc%2FDcLOeil7r2vzniha8alcMlbx%2B%2BhjIvgIJBkqHoqGnYyzv0Ee2gAxOwQbnSvPiJC4UbT%2FpB1ZP6fwTf5pQDafV7vcVXRiJKPoEOjQD%2BE7OjV8e2NY8LPS%2BIswwNCNxgY6pgH9ogBIE7aiYwTEIs6KqUKnzDPXsh%2BlLpwkm4yKHJ2L1d4sBlz6fLK7P72cd%2Fg9jbGfQnymifDVImj8H%2FR8ZSMNldBRH9eTGtz1grfwW1R5T9vUviGEi5gF1PI%2FWydmCDCp3J66TTPGT2fwBF%2BVOdUyXpcTvX4bnPwYj5xRSsnFHjka7xKZ7lq8WDc0j%2F3cvOD%2F0IGDIvNNyvwh%2FD%2BVnfyP4QwFFe2z&X-Amz-Signature=fd5da865fb1c7736d41dc8d4c9a3452d40c0b959b684e9627daa36f9248dc703&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
https://prod-files-secure.s3.us-west-2.amazonaws.com/83c75a39-3aba-4ba4-a792-7aefe4b07895/6d2f93a3-e90d-4a9a-9afa-67d9f9ace699/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WSULH3Q%2F20250912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250912T005027Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHXuGpD%2B7r1cW9iurbrUM2YXWcqZtwr1ZpzPC0Gtqib8AiAdyp84M6FPIxgIbbrLxKFEhBEwwKlLj9GAUhCbVS3QYir%2FAwghEAAaDDYzNzQyMzE4MzgwNSIMt6Pu3JJk6%2F6VmM%2BbKtwDGjEgLsaQCES8mtn29%2B4YR0nLtW%2BPC1Vy8vRyl2Crb6pFY9xKPlDOihPFN1sx5CGBEgSI%2BZvmlWpIDmSz4hqPXxDUVnlKco%2BHqBO%2BXFKocsSSV6ey9HgTTg85o038eZfQwKdCzob3JfG997%2Fbp6uQtUfAMPmZZZCU6tvBL9RF%2B3SjzqDbnj1Ndow2m1O2iRBOEZOdn3Y%2F6GoJ1QWtGkp3oMDH15xTMVZw97smndsjCFGPqdxsJ0vy2Cqr1adqEYaYTJgnWx9osP0LGlogX1E1vrLHINn50KjNtGSiTv6yTB3cqVFKZw5cUt4lPG1on%2BFMyKiv9%2BzFEuBj8j40c0LxemvDFWPmg7BZYTp%2BNDh0Gm8re1C7Yx8PDKkM%2BDhcJJyRiD62STcIBd1hHuZIELLw7GSy8PB8%2Fv5bww6q6vylsSLNW%2B1npZRPiZ%2FKrD045HQMp4sIcrDxBa0bzQIMGEbbE3vs5pIYOfkcjSr7a%2BwzLVMjupCZMPx1OOBuPtqEY5dvZNc%2FDcLOeil7r2vzniha8alcMlbx%2B%2BhjIvgIJBkqHoqGnYyzv0Ee2gAxOwQbnSvPiJC4UbT%2FpB1ZP6fwTf5pQDafV7vcVXRiJKPoEOjQD%2BE7OjV8e2NY8LPS%2BIswwNCNxgY6pgH9ogBIE7aiYwTEIs6KqUKnzDPXsh%2BlLpwkm4yKHJ2L1d4sBlz6fLK7P72cd%2Fg9jbGfQnymifDVImj8H%2FR8ZSMNldBRH9eTGtz1grfwW1R5T9vUviGEi5gF1PI%2FWydmCDCp3J66TTPGT2fwBF%2BVOdUyXpcTvX4bnPwYj5xRSsnFHjka7xKZ7lq8WDc0j%2F3cvOD%2F0IGDIvNNyvwh%2FD%2BVnfyP4QwFFe2z&X-Amz-Signature=64e0a96bc3dade5074c2b1489b597756fe9ebd999de17ec3c0cfaff39a5f0db1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
주차 별 CRM ctr cvr 추이
- 지면에 더 닿을 수 있도록 알림톡으로 배치 + 서류합격 리워드 추가 (예정) + 최종합류 CRM 세팅
- 합류헤택의 유효성을 확인하기 위한 지표가 되기도
  - 2차서류완료 / 최종합격 시, 안내 공통 CRM과 리워드 지급 CRM이 **모두 LMS로 발송**되고 있음 (총 3건)
  - CTA가 분기 되어, 각 CRM의 다음 CTA로 전환의 블로커가 있음
  ⇒ 결제 레버인 리워드 활용 CRM이 지난 회차 대비, [리워드 수령 to 결제 전환] 구간에서 부진
    - 리워드 수령 to 결제 전환
- 리워드  수령을 못한 db
- 알림톡 > MMS
1. 알림톡 분기 → 3일 뒤에 수령하지 않으면 리워드가 사라져요! LMS로 
- 내용이 많이 바뀌지 않으면 ⇒ 인지가 떨어지는 편
- 보통 마지막 액션이 문자로 가져가느 ㄴ편이 좋음
- ▶ 상세 데이터

### 백엔드 트랙 6회차
  - 리워드 수령
    - 2차서류완료 : `73.9%` (184명 중 136명)
    - 슬랙가입완료 : `82.4%` (153명 중 126명)
    - HRD등록완료 : `84.4%` (122명 중 103명)
  - 리워드 수령 to 결제 전환
    - 2차서류완료 : `47.8%` (136명 중 65명)
    - 슬랙가입완료 : `56.3%` (126명 중 71명)

### 백엔드 트랙 7회차
  > 💡 
    - 2차서류완료 to 리워드 수령 to 결제 (24명 to 20명 to 9명)
    https://prod-files-secure.s3.us-west-2.amazonaws.com/83c75a39-3aba-4ba4-a792-7aefe4b07895/8c70d664-a4eb-4c7a-9b04-97000212220c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFQZAKHW%2F20250912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250912T005042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAlXQ%2BkVOZD%2BHgPzFHiR4JxWMMKTPJZPE05jnzou3%2F8lAiAZhqjWARTLBnUPAE16HG1COXtGOJmPfLV5RNJ0NzBiGCr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMpoSUwby62o%2FeU6VOKtwDv4ZIYwrnrmPuAZpzwRbgg5AvbjYWK3JkCP3T8ENnfhHUw7WOEURpSPJSAZCdP2zwowozOEHUVGKGapffjgtOPnsHkklJwtgGR1N3iMNtimu43g1iy40hy1l%2BnPjll8Rk9BykNMLu7DGgFIPpPxBWqKjJf9ot48uww3YBcTuMXLw%2FO14DGq%2B3iYAlLHihfTlR2MT2lsegL5%2B7Ipb%2BXBBEBS3mg%2FpJiHhgDa13m9Xtnc417ix%2FaDO8u4o%2FmzxiwDanAuzYwA5flojexsuvuODYSaF%2BFRh6TW%2BJm%2FH6QUbuaymBBCz%2F6ZjtUHbh9Io25x%2FANWhaAAYmTXtbgGLPHhXiT1VIZOdC1ubBe1QfAiSBtac4psJcNHcnFXckXvUw3wEo1kgy2PyZADtFHWBvtxJjIrp6eb6spaYvpAtJKfUuKaw7R%2FP9Yjh50MMlbcgkaC%2Bq9GMmAow8m5QCTSBXd0MRVgjm7WrP3KUp1HADrfEVn46Ld4t1vUWGyZCnhBEVZoXd90ysBkf%2Fe2%2FNv%2FVbVd2NgvxgIU78CnGM8ha%2BGrsnKoKB9kDs%2Fn2hbUajGfdJE%2Fzj%2FXC89HgdjHM2TMEYd%2FCtDH8WUBtYfSlZAsmzTGUDLofEFTG51b24R1IsjLYwotGNxgY6pgGj8l9clJSiNsl6RkgnDcqOn5eQ2C3SyerJwE9pbO9ahQQoySvGGUTAMjy8eCY%2BpiQEpIctXeGHe81lZSsEoBp3SI0JtnYrVSTWqO%2Fm4pjQlCUiuUYBucW07s5VbmsxkbAmeQBj1yTSY7o2CKX6EyTv85wiVXZCGSvDlnbdMuDJceMlEeDlCSqAvHiFulm3bAX8tABaB6H27%2FFOQp8Jp2ABgnwud9fS&X-Amz-Signature=feb1e3d3904a1f70fd05f09b2045ef8d89d34f360bdc95b6cd02590d45196495&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
  > 💡 
    - 서합 to 리워드 수령 to 결제 (24명 to 19명 to 1명)
    https://prod-files-secure.s3.us-west-2.amazonaws.com/83c75a39-3aba-4ba4-a792-7aefe4b07895/c189815a-f186-47cf-8b6a-b581d9b63d91/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHPPZNU3%2F20250912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250912T005043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFQ0900cUKKwTKF0XQuiqFVn2o3BpGM4CWbfRz70vXPXAiAuk8F1CBh5WunFT%2FPMCRO5MhquJuCJo8027AtwFoofcSr%2FAwghEAAaDDYzNzQyMzE4MzgwNSIMgQI6R6dIF9FA1%2BAOKtwDBfF9%2BhlAPM3uy4xH1FidzjoKwoKhsAWh2n6Y4j49loW%2FqmD6z3Nyk5zQ94z33izwOE1K%2Bc7ya7xnkcP52su4jAWCekPMwzM6L4VSvC1rcFVvwufNx7ASCFno53Dd%2FIRBL53EnXg9tBOWdAH9PJg8JcxWTw6LPVWVEVjVK%2FiqLPD%2BzQ4hXmfY3zEGSgd6ziGX%2F%2F3ynyniX0lAMXJF6OW%2BVqYVmipxdPWn3awTBBsFweu0vc2kMF1tMKH7sufixAAvVerU%2FOdUBOwMRCn00sSwGqbMMbEm0Ilp4dnRp%2B14%2BVCqz2DshZI18Gdy3dTMVrUJr%2FN%2B7HKdrMyEXuAPDV9Thjw6AedEdnrwhcg8Fl1kuoK3FhnO%2BQ6cWwf5u%2BswHpG8sVeEFLkkQeVqwJ%2BMWqz1i4c6V3YfxAjYlA%2FaUgeG5OOtVeRG%2BuywkAksiZdQ6iwuPh5mw2%2FA1XWLJkrMYEUcYqJvdgCvHlkUIaQTA3axmShj9%2F%2Bl36JdU480%2BVZFSbV19OxzOm%2BHNDM3nwfufSZXtntvMv124xSE%2FLtWtcPvu%2B5fp1uVreY3wT3OjdSN4IKqlyYCHkwLP%2FDt504wA4UwScIOxxafjlmfE2j%2BQR4PKZuTZXk7qwyE5Ar5EKUwy9GNxgY6pgG%2Fbp4sTGikKHJK0Aln46kcgqSiydjByjBHFn90ltZ%2BJeuJjSe2h1EM8bNMvXhwQfAKw8OJyPREYtBXQfFubmnkWFUIDcREiguC84OBqCnO2wp6Jj0XCyZCGXsWevUwDfJw2P7N%2B5iw53afFyr4KduGriQe8JcMONNoJmIEQ%2BCwusG3BAR19hhu0CH6300KCqoTmZ7Gt3Zz6H%2BqAl8SYbloRe7S4GnG&X-Amz-Signature=e2b50aca89a5ff8a2a2bf1892ec57c73fda0f1d1b407545fd71344de65f747e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
**[문제 정의]**
*다각적으로 해석한 문제를 하나로 정의해주세요.*
- **리워드 지급 CRM이 결제 전환을 유도해야 하지만, 다른 CRM과의 CTA 충돌로 인해 리워드 수령 to 결제 전환율이 저하되고 있음**

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
- 선물함 자동 CRM을 알림톡으로 설정하면, 고객에게 쉽게 선물함이 인지 될 것이다.
  - → 알림톡과 LMS으로 채널을 분기하여 [리워드 수령 to 결제 전환] CVR을 개선 시킬 수 있을 것이다.
- 레퍼런스
    https://prod-files-secure.s3.us-west-2.amazonaws.com/83c75a39-3aba-4ba4-a792-7aefe4b07895/749bbe98-f18c-4d1a-beb6-48d82af86c3b/IMG_1153.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZAASHCI%2F20250912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250912T005049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFWgSbMxBDFGc8ArfIAvAvC4pvS5PC2iXeq%2FwHX2EqiVAiEApMXDl0bMHI1qE22wx2ZOOj7WJL0qmy%2BF1ctMneBzYfoq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDNAQu9wskeis18xbOSrcA4PyBts6iML2yS%2BIrWYCwW7khDW6eYADYnvgvJnXwnrkiIGqjVx%2B9gA5ei2LxtKxHNcH0eoFuuz8wT%2BS1AVhtfr5K5ROXHGzFl0m%2BYmR3EvLqBJvraAfyMZfUW4xnjGaB86KUFwqiCPbL%2F3T%2BFRprIxZd14PXy%2BAf%2BP0Kwrvp1yqQJVFmrKbgixOsUhbYvKpH190G%2FBBK9Laaniq4UwdC%2FL2KO%2FNGACm9qXA3u26Hbxh4p%2FdLo2LC20t%2BIzxMTBaelaS55XNP7cFJRfuXyrwaP1dv470xjkmo87wASRphI7ap8LRDxSPMfbkIZQw2rOVoQbrOTHUcbixsB046TUXvONLaeETiOKIZJCOnyN8%2BpXRD9G7gWpwAdTFqPFF49OjyJGQc%2B5VTG5iUG8DT1UF1yWEcA9U7bkP%2FUuR7%2FPIcPJiOHu01rvEEjeONK0y%2BmnQX%2F48MGV7nI5OSlkXMlGOql8vgUhbEsBC%2BiliEYmVGZCkkBU8JJ%2FfBfA9DAtmnrhtylwtDMcVWl0VRhDGLGMsnFWGVlJxnmBmApNP7oGH0MKJfCQZhhaXCGa4L2i85QgUTkRYPqcxavUHuONC%2BXO%2BXALm%2BddUNv%2FQ%2Bx42W30DyJTVGjZ9F5Sib8cYBUG9MM3QjcYGOqUBIxkLmm1R%2F1VAMOVxiimbeeOD6VloicAVjA6mL0LqWdyFsxvlMwSxV2wD329RiNcnZ9qENly0eN%2BvxzdpHm9hKfA5VoD0H0lXnd7kgTzLSGcleAAz59PGXXoFLXZ8iLPVQm%2B5trkOvc0LCsPyF7YvhleTTJgLpXnVjDWQLL3o6g3pLgGhYJ%2FgfVUGad4GDP%2FD3ofRFZlXBR3hylM3vdffC%2BpRmWD1&X-Amz-Signature=22a6a028e7e401aed922ff453320a952a3ee8d6eacc2fc75bb9a8144be427caf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
    https://prod-files-secure.s3.us-west-2.amazonaws.com/83c75a39-3aba-4ba4-a792-7aefe4b07895/88842386-ff48-4851-9aa7-87b94dd33e6e/IMG_1152.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKP4I2UJ%2F20250912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250912T005050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCloOtL7L0lxVSFKaUZ8%2BMD9V%2F71Itrh2kms%2F6Es8ja5QIgKyDsTM5YJ0LcNP9KkYXAQ%2BlMrN4mkVA2JGi4BYu2beEq%2FwMIIRAAGgw2Mzc0MjMxODM4MDUiDJWZOXc0U4zbQSr9rircAzdiMD4cGZ8a26uepSHcViBM9gHyL1dY8xLTBkuX%2F8quEHhmUA4%2FXrPIluTrhOp3dBxNu03VHp2cbrpd0437s90Q6wEm8bebRkGMk%2FVRyibP6IEFT0FOAXM5bcY21ONV%2BRznVcN%2BrM9Uj4NnoGOR7d6q0jr0qjFW85mFuWkeS5KYuZhMIdTgQ9rlQWGpzqzYU6CmvA%2BfQtVtbJH3fmTxxfeptF7d1E4h6bfi7DHY75%2Fv2Oe0aL60IGgwHkAFmU9Gth1K9YBHYbBDeaQaNt0gba1gHHqIgit5p%2Fy0kGsUGEcglkVo4qsmPZty1orpud1zftm46KqlR8XWjwpHpdcUqVz7wHeIk0XO9OT52id5HL1V0XYmPRSVxkKUS%2BpPSGVyAIyqsq8%2FHHsf0yXrbSx5uy34JUHN6RMKah1L71LtEXVvN9zDcDmHLwqPTDqzy5kqq5B3hKht8ttXOYYyx3r6bCbSnpJK6m27np%2FJurVa4lW8IN8MC1hLigvXYxumZKcrRGQKtAJYBgWEf1okRWF1j8FoOt4eUAidx6wnaeLH8M5iYkcZ1HFBe1xzHlJqodlufeR9tmB1cdo1bfSGvRWQrVzC08G%2Ff8%2F%2FT3Lp5c%2FgdOL3blQdt2%2FzO6fvd8MMMKrRjcYGOqUBrdR8OnEA8h%2FN5qh%2Bt8reSv%2BZCfM%2FGwsiMmSJoJcF3b7FNidI%2BNVj%2BsJf6RCn9Eb7g%2BfNtt7yNzKoyp4zvwu60XjnkaK3O6cDXYxK6VCOW%2BzxJ6nkVIwdZiKu9KZ1JyMFMnWEsqb%2Bk7NzqzsFzgsQ2Cb49xkkVbLlcBdU3iMi2TFHiLGqd5So07nL92aqv%2FSKWUTT60ktyzrTUHfDwtyBEHuplqhY&X-Amz-Signature=497b1b5f371a549112e256839c0fe007d0b964839fc45e6f2ac28c9ba77a8677&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
    https://prod-files-secure.s3.us-west-2.amazonaws.com/83c75a39-3aba-4ba4-a792-7aefe4b07895/00d17095-ca9a-4ed4-b732-8d83fe1083de/IMG_1151.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QJNBZOX%2F20250912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250912T005050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2B%2Bn8yKkIKRizQu1XZtV7KeRnx69nc4HjF7CwGVUOl7gIhAIm3dKwO4XnvsQ7eYYCbiRJYYuHstTYrgCfSsWxUtf6WKv8DCCEQABoMNjM3NDIzMTgzODA1Igz6h5Q7FXbx6nJMA3cq3AOArathSVM4pa9qSoyNXtTcHLkfjeAVKs7zOFYlwY%2Fgmth0V9XG6HbE560oVc%2FZNOxXy4UBq%2BnyUXJZGR3nw0Kdd2MvCD7R%2BKezrOFENdva6EKXp78Era%2B6QyeYqbjbeM%2F%2BQ9AVU4x%2BpM1P1%2FhczPDjSJs5UzCCEPs%2BE7LxiLlsGiAv5xGlAIUPgFLfv85mIdNCIGWfluCL4rA1h%2Bx7qieRcpl7JYAEXVoXOUG2cAni%2BwLpCtPAQGj0KRCncW5mT859FZwfAo5xdCm%2BI%2BkQHV30rXqTGC3B9nf5YN5wlAnH1%2F2%2FJmJ9mv9%2BUM4F1YWT8iMwM6qS%2FSCOdMI1qRnaL5e1phET4TG23MsFfuve9LEd6smEL4czon5YKbAYhRYEbPYvoOVGbECbimCh4Cl3dO34KywkCInVOSh9j0JzPxoW8Z%2FtU8GZO6dSl8U6Qa%2B6MHywAvq%2FuXGH2vwMrn1Uo9%2F7aKgyk%2FSMIsKqogHATebyIHCmXKOpIE29aWy6%2FK1dWjRBApHm9KSGXh8V1om8JXHmiaBvnlZLrkgJiZtUc0ujt40SkE2eoRcPsr1sAKxQcHNaqcSd522QGrTgIn5LVHEbRuSje0DcKEr6ZscgeCy%2BULMO4ppJU78FoEzqZzDg0Y3GBjqkAbRHQ0IqrSlWGqJlPSQR6IrsAzK4Xw1387h6tkhG5PGRp32PEDK8iW%2B4vsqPaBU1M6KjhaQ1PmLC5%2BRDOjwvL9ogKTHXPBjWs8IVy46%2BA0nSeXtgnvkrv51DIpk9E3cmiDj5S6C5aWut9QacTANypV793dwFFnxLJxLMSnFd1RmjR1nz2qVtyhr6SUe0aR%2FPJ1tePxrTqDju4oX5v%2FplDZ8mqXvT&X-Amz-Signature=464f47aaecf9d3147fd8f8bdffa08401f46879b133006894641cb4c3acfeaead&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject

### **2) 목표 지표 & 측정 기간**
*타겟 기반의 지표 설정을 통해 성공 지표와 가드레일 지표를 설정합니다. 
액션의 기간을 미리 설정하고 성공/실패에 따른 배운 점*
- 액션 효율 측정 기간: 배포 후 1주일 (검수 기간 2-3일 제외)
- 현재 지표
  - 2차서류완료 : 45% 
  - 서합 : 5.2
- 성공 지표
  - 2차서류완료 : 50% 이상
  - 서합 : 15% 이상
  - ▶ 성공 목표에 달성하게 된다면 우리는 무엇을 배웠고 앞으로 방향성이 어떻게 될까요?
    - 배운 점:
- 가드레일 지표
  - 2차서류완료 : 46% 
  - 서합 : 8% 
  - ▶ 목표에 달성하지 못했다면 우리는 무엇을 배웠고 앞으로 방향성이 어떻게 될까요?
    - 배운 점:

# [1] Goal

## 상세 기획안 (executive summary)

---

## Story 기획 산출물(Output)
*이 프로젝트를 통해 산출되어야 하는 결과물에 대해서 대략적으로 작성해주세요!*
- 리워드 3 가지 확정
  - 2차서류완료 / 서류 합격 / 최종 합격
- 리워드 MMS 제작
  - 트랙 및 혜택 종류 상관없이 공용적으로 사용할 수 있는 템플릿
- 2차서류완료 / 서류합격 / 최종합격 → 3 개 구간에 리워드 전용 알림톡 세팅

---

## 프로덕트 디자인
- ▶ 디자인 시, 필요한 정보(카피,이미지, 정책 등등)
| 목적과 배경 |  |
| --- | --- |
| 요구 사항 |  |
| 참고 데이터 |  |
| 유저 케이스 |  |
| 고민 포인트 |  |
| 피그마 |  |

---

## PRD
| **페이지 이름** | **작업명** | **상세 기능** | **소요 시간(d)** | **우선순위** | **개발 상태** |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

# [2] 성과 공유

---
*최초 프로젝트 시작 당시 설정한 기대효과 대비 실제 성과가 어땠는지 기술해주세요*

# [3] 액션 로그

## Databases
