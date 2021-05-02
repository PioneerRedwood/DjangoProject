# DjangoProject
정보공개서로부터 읽어낸 데이터를 웹 통신을 하기 위한 서버 프로토타입 프로젝트
[데이터 수집 프로젝트](https://github.com/PioneerRedwood/CrawlingData)

## 2021.04.29.
Brand, Headquarter 데이터 MySql에 삽입



### Brand 테이블 정보
    id, 업종(sector), 브랜드 이름(brand_name), 상호(mutual),
    가맹사업 시작일(franchise_start_date), 가맹사업 개월수(franchise_months),
    가맹점수(num_of_franchise), 임직원수(num_of_employees),
    신규개점수(num_of_open), 폐점수(num_of_quit), 해지수(num_of_cancel),
    명의변경수(num_of_name_changing), 평균매출액(average_sales), 면적당 평균 매출액(average_sales_per_area),
    가맹비(franchise_fee), 교육비(education_fee), 보증금(deposit), 기타비용(other_cost),
    창업비용(startup_cost), 면적당 비용(cost_per_area), 기준면적(standard_area), 
    총 비용(total_cost)
✌브랜드 테이블은 정보공개서에서 제공한 데이터를 가공하여 제작했다.

### Headquarter 테이블 정보
    id, 상호(mutual), 대표자(representative), 법인 설립 등기일(register_law_date),
    사업자 등록일(register_biz_date), 대표번호(representative_number), 
    대표 팩스 번호(fax_number), 주소(address), 사업자 유형(biz_type),
    법인 등록 번호(law_number), 사업자 등록 번호(biz_number),
    2020년 자산(assets_2020), 2020년 부채(liabilities_2020), 2020년 자본(equity_2020), 2020년 매출액(sales_2020), 2020년 영업이익(income_2020), 2020년 당기순이익(net_income_2020) ... 
    2020년 개점(opening_2020), 2020년 폐점(closing_2020), 2020년 명의변경(name_change_2020) ... 
    공정거래위원회 시정 조치(num_of_correction), 민사소송 패소 및 민사상 화해(num_loss_of_law), 형의 선고(num_of_sentences)

✌본사 테이블은 정보공개서에서 제공한 데이터를 가공하여 제작했다.

