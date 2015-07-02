# woah this is really easy!!
import pygal
from pygal.style import Style

# change the color scheme
custom_style = Style(
    background='transparent',
    plot_background='transparent',
    foreground='#000000',
    opacity='.5',
    opacity_hover='.8',
    colors=('#FF4D4D','#E853A0', '#E8537A', '#E95355', '#E87653'),
    font_family=('Arial')
    )

# draw the chart
bar_chart = pygal.Bar(fill=True, style=custom_style)
# add data
bar_chart.add('Fibnonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
# export to file! says to use a figure/embed tag to place in html
bar_chart.render_to_file('/Users/karen/pyprojects/prk_story/bar_chart.svg')