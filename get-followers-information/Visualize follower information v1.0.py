# FOLLOWER SCATTER PLOT - note that this code depends on the CSV 
# being in reverse follow order, which is how the Twitter API currently
# returns followers. It will not work correctly if the rows in the CSV
# are rearranged.
 
import pandas as pd
import bokeh.plotting as bk
 
def follower_scatter_plot (followers, handle, opacity_norm=5000,
        bubble_size=4, color=(0,90,180), cat_column=None, 
        cat_colors=None, start=None, end=None,
        min_date=None, max_date=None, max_sample_size=200000):
    followers["createTime"] = pd.to_datetime (followers["createTime"])
    followers["order"] = followers.index 
    followers["order"] = followers["order"].max () - followers["order"]
    df = followers[followers["createTime"] > pd.to_datetime ("2005")]
    zoomed = ""
    if start is not None:
        df = df[df["order"] >= start]
        zoomed = " (zoomed)"
    if end is not None:
        df = df[df["order"] < end]
        zoomed = " (zoomed)"
    if min_date is not None:
        min_date = pd.to_datetime (min_date)
        df = df[df["createTime"] >= min_date]
        zoomed = " (zoomed)"
    if max_date is not None:
        max_date = pd.to_datetime (max_date)
        df = df[df["createTime"] < max_date]
        zoomed = " (zoomed)"
    title = "@" + handle + \
            " followers - follow order by creation date" + zoomed
    p = bk.figure (title=title, width=800, height=800,
            y_axis_type="datetime", x_axis_label="follow order",
            y_axis_label="creation date")
    if cat_colors is None or cat_column is None:
        if len (df.index) > max_sample_size:
            df = df.sample (max_sample_size)
        alpha = opacity_norm / len (df.index)
        p.circle (df["order"], df["createTime"], size=bubble_size,
                  color=color, alpha=alpha)
    else:
        for label in cat_colors:
            df0 = df[df[cat_column] == label]
            df1 = df.sample (1)
            p.circle (df1["order"], df1["createTime"], size=bubble_size, 
                      color=cat_colors[label], legend=label + \
                      " (" + str (len (df0.index)) + " accounts)")
            p.circle (df1["order"], df1["createTime"], size=bubble_size, 
                      color=(255,255,255))
        if len (df.index) > max_sample_size:
            df = df.sample (max_sample_size)
        alpha = opacity_norm / len (df.index)
        df["color"] = df[cat_column].apply (lambda x: cat_colors[x])
        p.circle (df["order"], df["createTime"], size=4, 
                  color=df["color"], alpha=alpha)      
        p.legend.location = "bottom_center"
    p.xaxis.axis_label_text_font_size = "15pt"
    p.yaxis.axis_label_text_font_size = "15pt"
    p.yaxis.major_label_text_font_size = "12pt"
    p.xaxis.major_label_text_font_size = "12pt"
    p.yaxis[0].formatter.hours = ["%H:%M"]
    p.yaxis[0].formatter.days = ["%Y-%m-%d"]
    p.title.text_font_size = "14pt"
    p.title.align = "center"
    p.xaxis[0].formatter.use_scientific = False    
    return p

handle = "hogehoge"
df = pd.read_csv ( handle + "_followers.csv", encoding="utf-8")
colors = {
    "has liked one or more tweets" : "#80a080",
    "has never liked a tweet" : "#f06000", 
}
df["cat"] = df["likes"].apply (lambda x: "has never liked a tweet" \
        if x == 0 else "has liked one or more tweets")
p = follower_scatter_plot (df, handle, cat_column="cat", cat_colors=colors)
bk.show (p)
