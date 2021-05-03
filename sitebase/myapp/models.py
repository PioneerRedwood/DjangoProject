from django.db import models
from django.urls import reverse


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

    def get_absolute_url(self):
        return reverse('myapp:detail', kwargs={'pk': self.id})


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


class StoreAddress(models.Model):
    id = models.CharField(max_length=8, primary_key=True, null=False)
    sector = models.CharField(max_length=16, null=False)
    brand_name = models.CharField(max_length=40)

    do = models.CharField(max_length=16, null=False)
    sigu = models.CharField(max_length=32, null=False)
    dong = models.CharField(max_length=16)

    longitude = models.CharField(max_length=16, null=False)
    latitude = models.CharField(max_length=16, null=False)


class Population(models.Model):
    id = models.CharField(max_length=8, primary_key=True, null=False)
    do = models.CharField(max_length=16, null=False)
    sigu = models.CharField(max_length=32, null=False)
    dong = models.CharField(max_length=16)
    population = models.IntegerField()
