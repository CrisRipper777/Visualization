import akshare as ak

import pandas as pd

from pyecharts.charts import *

from pyecharts import options as opts

from pyecharts.globals import ThemeType

df = ak.stock_zh_a_hist(symbol="600036", start_date='20220101',
                        end_date='20220916', adjust="qfq").iloc[:, :6]

df.columns = [

    'date',

    'open',

    'close',

    'high',

    'low',

    'volume',

]

# 把 date 作为日期索引

df.index = pd.to_datetime(df.date)

df['date'] = df.index.year  # 将日期转换为年份

df = df.sort_index()

# data_price=data_price.copy()

# data_price.index=data_price.index.strftime('%Y%m%d')

df['sma'] = df.close.rolling(5).mean()

df['lma'] = df.close.rolling(10).mean()

df['lma20'] = df.close.rolling(20).mean()

df['lma30'] = df.close.rolling(30).mean()

df['lma60'] = df.close.rolling(60).mean()

kline = (

    Kline(init_opts=opts.InitOpts(width="1200px", height="600px"))  # 指定图形长宽

    .add_xaxis(xaxis_data=list(df.index))  # x轴数据

    .add_yaxis(  # y轴数据

        series_name="klines",  # 名称

        y_axis=df[["open", "close", "low", "high"]].values.tolist(),  # 数据源

        itemstyle_opts=opts.ItemStyleOpts(
            color="#ec0000", color0="#00da3c"),  # 颜色设置

    )

    .set_global_opts(  # 图表全局设置

        title_opts=opts.TitleOpts(title="K线及均线", pos_left='45%'),  # 标题位置

        legend_opts=opts.LegendOpts(pos_right="35%", pos_top="5%"),  # 图例位置

        yaxis_opts=opts.AxisOpts(is_scale=True,

                                 splitarea_opts=opts.SplitAreaOpts(is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)), ),

        datazoom_opts=[opts.DataZoomOpts(type_='inside')],  # K线缩放-内部滑动

        tooltip_opts=opts.TooltipOpts(  # 鼠标提示设置

            trigger="axis", axis_pointer_type="cross",  # 趋势线

            background_color="rgba(245, 245, 245, 0.8)",  # 背景颜色

            border_width=1, border_color="#ccc",

            textstyle_opts=opts.TextStyleOpts(color="#000"), ),

        visualmap_opts=opts.VisualMapOpts(is_show=False, dimension=2, series_index=5, is_piecewise=True,

                                          pieces=[{"value": 1, "color": "#00da3c"}, {"value": -1, "color": "#ec0000"}, ], ),

        axispointer_opts=opts.AxisPointerOpts(is_show=True,

                                              link=[{"xAxisIndex": "all"}], label=opts.LabelOpts(background_color="#777"), ),

        brush_opts=opts.BrushOpts(x_axis_index="all", brush_link="all",

                                  out_of_brush={"colorAlpha": 0.1}, brush_type="lineX", ),

    )

)

line = Line()  # 均线绘制

line.add_xaxis(df.index.tolist())  # x轴数据

line.add_yaxis('MA5', df.sma.round(2).tolist(), is_smooth=True)  # y轴数据

line.add_yaxis('MA10', df.lma.round(2).tolist(), is_smooth=True)

line.add_yaxis('MA20', df.lma20.round(2).tolist(), is_smooth=True)

line.add_yaxis('MA30', df.lma30.round(2).tolist(), is_smooth=True)

line.add_yaxis('MA60', df.lma60.round(2).tolist(), is_smooth=True)

line.set_series_opts(label_opts=opts.LabelOpts(is_show=False))  # 是否显示数据标签

line.set_global_opts(  # 均线全局设置

    datazoom_opts=[opts.DataZoomOpts(type_='inside')],  # 内部滑动

    legend_opts=opts.LegendOpts(pos_right="20%", pos_top="5%"),  # 图例位置

    tooltip_opts=opts.TooltipOpts(
        trigger="axis", axis_pointer_type="cross")  # 添加趋势线

)

kline.overlap(line)  # 将均线叠加到K线上

kline.render("K线.html")  # 保存到文件
