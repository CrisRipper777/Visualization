from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.globals import ThemeType

attr = ['交通运输、仓储和邮政业', '房地产业', '制造业', '批发和零售业', '租赁和商务服务业', '金融业', '电力、热力、燃气及水生产和供应业', '建筑业']
v1 = [4.7, 4.7, 19, 28, 4.7, 28, 4.7, 4.7]
c=(
        Pie(init_opts=opts.InitOpts(theme=ThemeType.ROMANTIC))
        .add(
                "", [list(z) for z in zip(attr, v1)],radius=[55,175],center=["35%", "50%"]
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="投资类型分布图"),legend_opts=opts.LegendOpts(pos_left="right",orient="vertical"))
        .render(path="投资类型分布图.html")
)