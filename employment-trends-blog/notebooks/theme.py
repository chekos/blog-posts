def cimarron_theme():
    markColor = "#282828"
    axisColor = "#282828"
    backgroundColor = "#FFFAFA"
    font = "Ubuntu"
    labelfont = "Ubuntu Condensed"
    sourcefont = "Ubuntu Mono"
    gridColor = "#C9C9C9"
    return {
        "width": 1080,
        "height": 800,   
        "autosize": "fit",
        "config": {
           "padding": 10,
           "geoshape": {
               "fill": "#C0C0C0",
           },
           "arc": {
               "fill": markColor,
           },
           "area": {
               "fill": markColor,
           },
           "axisBand": {
               "grid": False,
           },
           "axisBottom": {
               "domain": False,
               "domainColor": "black",
               "domainWidth": 3,
               "grid": True,
               "gridColor": gridColor,
               "gridWidth": 1,
               "labelFontSize": 20,
               "labelFont": labelfont,
               "labelPadding": 8,
               "labelAngle": 0,
               "tickColor": axisColor,
               "tickSize": 10,
               "titleFontSize": 16,
               "titlePadding": 10,
               "titleFont": font,
               "title": "",
           },
           "axisLeft": {
               "domainColor": axisColor,
               "domainWidth": 1,
               "gridColor": gridColor,
               "gridWidth": 1,
               "labelFontSize": 20,
               "labelFont": labelfont,
               "labelPadding": 8,
               "tickColor": axisColor,
               "tickSize": 10,
               "ticks": True,
               "titleFontSize": 22,
               "titlePadding": 10,
               "titleFont": font,
           },
           "axisRight": {
               "domainColor": axisColor,
               "domainWidth": 1,
               "gridColor": gridColor,
               "gridWidth": 1,
               "labelFontSize": 12,
               "labelFont": labelfont,
               "labelPadding": 4,
               "tickColor": axisColor,
               "tickSize": 10,
               "ticks": True,
               "titleFontSize": 14,
               "titlePadding": 10,
               "titleFont": font,
           },
           "axisTop": {
               "domain": False,
               "domainColor": "black",
               "domainWidth": 3,
               "grid": True,
               "gridColor": gridColor,
               "gridWidth": 1,
               "labelFontSize": 12,
               "labelFont": labelfont,
               "labelPadding": 4,
               "tickColor": axisColor,
               "tickSize": 10,
               "titleFontSize": 14,
               "titlePadding": 10,
               "titleFont": font,
           },
           "background": backgroundColor,
           "group": {
               "fill": backgroundColor,
           },
           "legend": {
               "labelFontSize": 16,
               "labelFont": labelfont,
               "labelLimit": 500,
               "padding": 10,
               "symbolSize": 100,
               "symbolType": "square",
               "titleFontSize": 18,
               "titlePadding": 10,
               "titleFont": font,
           },
           "line": {
               "color": markColor,
               "stroke": markColor,
               "strokewidth": 5,
           },
           "trail": {
               "color": markColor,
               "stroke": markColor,
               "strokeWidth": 0,
               "size": 5,
           },
           "path": {
               "stroke": markColor,
               "strokeWidth": 0.5,
           },
           "point": {
               "filled": True,
           },
           "rect": {
               "fill": "#A20C4B",
               "opacity": 0.3,
           },
           "range": {
               "category": ["#dc0d7a", "#02a3cd", "#e4a100", "#dc0d12", "#0DDC6F","#074a7e", "#e46800", "#aa3594", "#a20c4b"],
               "diverging": [
                   "#dc0d12",
                   "#e9686b",
                   "#fbe1e1",
                   "#dff4f9",
                   "#81d1e6",
                   "#03a3cd"
               ],
               "heatmap": [
                   "#fcdfef",
                   "#f8bfde",
                   "#f59fce",
                   "#f180be",
                   "#ee60ad",
                   "#eb409d",
                   "#e7208c",
                   "#e4007c",
               ],
           },
           "symbol": {
               "opacity": 1,
               "shape": "circle",
               "size": 40,
               "strokeWidth": 1,
           },
           "style": {
               "bar": {
                   "binSpacing": 2,
                   "fill": markColor,
                   "stroke": False,
               },
               "text": {
                   "font": sourcefont,
                   "fontSize": 10,
                   "align": "right",
                   "text": "Made by @ChekosWH",
                   "href": "https://twitter.com/ChekosWH",
                   "fontWeight": 100,
                   "size": 10,
                   "dx": 300,
               }
           },
           "title":{
               "anchor": "start",
               "fontSize": 24,
               "fontWeight": 600,
               "font": font,
               "offset": 20,
           },
           "view": {
               "stroke": False,
               "padding": 15,
           },
            "header": {
                "fontWeight": 400,
                "labelFontSize": 28,
                "labelFont": labelfont,
                "titleFontSize": 28,
                "titleFont": font,
                "title": " ",
                "titleBaseline": "bottom",
                "titleOffset": -30,
            },
       },
    }
    
    
import altair as alt
alt.themes.register("cimarron", cimarron_theme)
alt.themes.enable("cimarron")