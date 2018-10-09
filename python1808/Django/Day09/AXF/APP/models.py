from django.db import models

# Create your models here.

class Main(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=30)
    trackid = models.CharField(max_length=20)

    class Meta:
        abstract = True #抽象类

#首页-轮播
class MainWheel(Main):
    class Meta:
        db_table = 'axf_wheel'


#首页-导航
class MainNav(Main):
    class Meta:
        db_table = 'axf_nav'


#首页-必须购买
class MainMustbuy(Main):
    class Meta:
        db_table = 'axf_mustbuy'


#首页-购买
class MainShop(Main):
    class Meta:
        db_table = 'axf_shop'


class MainShow(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=20)

    img1 = models.CharField(max_length=100)
    childcid1 =models.CharField(max_length=10)
    productid1 = models.CharField(max_length=10)
    longname1 = models.CharField(max_length=50)
    price1 = models.CharField(max_length=10)
    marketprice1 = models.CharField(max_length=10)

    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=10)
    longname2 = models.CharField(max_length=50)
    price2 = models.CharField(max_length=10)
    marketprice2 = models.CharField(max_length=10)

    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=10)
    longname3 = models.CharField(max_length=50)
    price3 = models.CharField(max_length=10)
    marketprice3 = models.CharField(max_length=10)

    class Meta:
        db_table = 'axf_mainshow'


class MainFoodTpye(models.Model):
    typeid = models.CharField(max_length=10)
    typename = models.CharField(max_length=20)
    childtypenames = models.CharField(max_length=150)
    typesort = models.IntegerField()

    class Meta:
        db_table = 'axf_foodtypes'


class Goods(models.Model):
    # 商品id
    productid = models.CharField(max_length=10)
    #商品图片
    productimg = models.CharField(max_length=150)
    #商品名称
    productname = models.CharField(max_length=50)
    #商品长名称
    productlongname = models.CharField(max_length=100)
    #是否精选
    isxf = models.NullBooleanField(default=False)
    #是否买一赠一
    pmdesc = models.CharField(max_length=10)
    #规格
    specifics = models.CharField(max_length=20)
    #价格
    price = models.CharField(max_length=10)
    #超市价格
    marketprice = models.CharField(max_length=10)
    #
    categoryid = models.CharField(max_length=10)
    #子类组id
    childcid = models.CharField(max_length=10)
    #子类组名称
    childcidname = models.CharField(max_length=10)
    #详情页id
    dealerid = models.CharField(max_length=10)
    #库存
    storenums = models.IntegerField()
    #销量
    productnum = models.IntegerField()

    class Meta:
        db_table = 'axf_goods'