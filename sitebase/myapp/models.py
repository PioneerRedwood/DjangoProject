from django.db import models


class Brand(models.Model):
    # id | 업종 | 브랜드 | 상호 | 가맹사업 개시일 | 가맹사업 개월수
    id = models.CharField(max_length=8, primary_key=True)
    sector = models.CharField(max_length=16)
    brand_name = models.CharField(max_length=40)
    mutual = models.CharField(max_length=40)
    franchise_start_date = models.CharField(max_length=40)
    franchise_months = models.IntegerField()

    # 가맹점수 | 임직원수 | 신규개점 | 폐점수 | 종료수 | 명의변경
    num_of_franchise = models.IntegerField()
    num_of_employees = models.IntegerField()
    num_of_open = models.IntegerField()
    num_of_quit = models.IntegerField()
    num_of_cancel = models.IntegerField()
    num_of_name_changing = models.IntegerField()

    # 평균 매출액 | 면적 당 평균 매출액 | 가맹비 | 교육비 | 보증금 | 기타 비용
    average_sales = models.IntegerField()
    average_sales_per_area = models.IntegerField()
    franchise_fee = models.IntegerField()
    education_fee = models.IntegerField()
    deposit = models.IntegerField()
    other_cost = models.IntegerField()

    # 창업비용 | 면적당 비용 | 기준 면적 | 전체 비용
    startup_cost = models.IntegerField()
    cost_per_area = models.IntegerField()
    standard_area = models.IntegerField()
    total_cost = models.IntegerField()


"""
id, 상호, 대표자, 법인 설립 등기일, 사업자 등록일, 
대표번호, 대표 팩스 번호, 주소, 사업자 유형, 법인 등록 번호, 사업자 등록 번호
2020년-2017년 (자산, 부채, 자본, 매출액, 영업이익, 당기순이익)
2020년-2017년 (개점, 폐점(계약종료 + 계약해지), 명의변경)
최근 3년간 법 위반 사실(공정거래위원회의 시정조치, 민사소송 패소 및 민사상 화해, 형의 선고)
"""


class Headquarter(models.Model):
    # 5
    id = models.CharField(max_length=8, primary_key=True)
    mutual = models.CharField(max_length=40)
    representative = models.CharField(max_length=40)
    register_law_date = models.CharField(max_length=40)
    register_biz_date = models.CharField(max_length=40)

    # 6
    representative_number = models.CharField(max_length=40)
    fax_number = models.CharField(max_length=40)
    address = models.CharField(max_length=128)
    biz_type = models.CharField(max_length=40)
    law_number = models.CharField(max_length=40)
    biz_number = models.CharField(max_length=40)

    # 6
    assets_2020 = models.FloatField()
    liabilities_2020 = models.FloatField()
    equity_2020 = models.FloatField()
    sales_2020 = models.FloatField()
    income_2020 = models.FloatField()
    net_income_2020 = models.FloatField()

    # 6
    assets_2019 = models.FloatField()
    liabilities_2019 = models.FloatField()
    equity_2019 = models.FloatField()
    sales_2019 = models.FloatField()
    income_2019 = models.FloatField()
    net_income_2019 = models.FloatField()

    # 6
    assets_2018 = models.FloatField()
    liabilities_2018 = models.FloatField()
    equity_2018 = models.FloatField()
    sales_2018 = models.FloatField()
    income_2018 = models.FloatField()
    net_income_2018 = models.FloatField()

    # 6
    assets_2017 = models.FloatField()
    liabilities_2017 = models.FloatField()
    equity_2017 = models.FloatField()
    sales_2017 = models.FloatField()
    income_2017 = models.FloatField()
    net_income_2017 = models.FloatField()

    # 3
    opening_2020 = models.IntegerField()
    closing_2020 = models.IntegerField()
    name_change_2020 = models.IntegerField()

    # 3
    opening_2019 = models.IntegerField()
    closing_2019 = models.IntegerField()
    name_change_2019 = models.IntegerField()

    # 3
    opening_2018 = models.IntegerField()
    closing_2018 = models.IntegerField()
    name_change_2018 = models.IntegerField()

    # 3
    opening_2017 = models.IntegerField()
    closing_2017 = models.IntegerField()
    name_change_2017 = models.IntegerField()

    # 3
    num_of_correction = models.IntegerField()
    num_loss_of_law = models.IntegerField()
    num_of_sentences = models.IntegerField()
