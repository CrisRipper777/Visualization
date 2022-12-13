from pyecharts.charts import Bar, Page, Line
from pyecharts import options as opts
from pyecharts.globals import ThemeType

x = ['2016年','2017年','2018年','2019年','2020年','2021年']
y1 = [1694, 1535, 1380, 1383, 1167, 1058]
y2 = [1235.2, 1167.5, 1017.6, 921.9, 918.8, 756.4]
sz = [458.8, 367.5, 362.4, 461.1, 248.2, 301.6]

bar = (
    Bar(init_opts=opts.InitOpts(width="600px", height="580px",theme=ThemeType.ROMANTIC))
    # 设置x轴
    .add_xaxis(xaxis_data=x)
    # 设置y轴
    .add_yaxis(series_name='营业收入', y_axis=y1, label_opts=opts.LabelOpts(is_show=False))
    .add_yaxis(series_name='营业支出', y_axis=y2, label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title='每年收支统计'),
    tooltip_opts=opts.TooltipOpts(
            is_show=True, trigger="axis", axis_pointer_type="cross"
        ),
        xaxis_opts=opts.AxisOpts(
            type_="category",
            axispointer_opts=opts.AxisPointerOpts(is_show=True, type_="shadow"),
        ),)
)
line = (
    Line()
    .add_xaxis(xaxis_data=x)
    .add_yaxis(
        series_name="净收益",
        yaxis_index=1,
        y_axis=[458.8, 367.5, 362.4, 461.1, 248.2, 301.6],
        label_opts=opts.LabelOpts(is_show=False),
    )
)

# 生成html文件
bar.render("每年收支统计图.html")

