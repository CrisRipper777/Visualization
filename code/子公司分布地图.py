from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ThemeType

province_distribution = {'山西': 16, '河北': 34, '安徽': 16, '江西': 16, '贵州': 10, '河南': 49, '北京': 85, '陕西': 27, '重庆': 45, '福建': 110, '湖南': 34, '甘肃': 3, '四川': 54, '浙江': 137, '广东': 368, '上海': 101, '山东': 109, '湖北': 82, '广西': 9, '天津': 42, '内蒙': 5, '新疆': 2, '辽宁': 53, '江苏': 107, '吉林': 1, '宁夏': 1, '云南': 45, '海南': 30, '黑龙': 1}
provice = list(province_distribution.keys())
values = list(province_distribution.values())
c = (
    Map(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
    .add("数量", [list(z) for z in zip(provice, values)], "china")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(max_=140, is_piecewise=True), title_opts=opts.TitleOpts(title="平安银行子公司分布图")
    )
    .render("子公司分布地图.html")
)