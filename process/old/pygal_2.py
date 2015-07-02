# woah this is really easy!!
import pygal
from pygal.style import Style

# change the color scheme
custom_style = Style(
    background='transparent',
    plot_background='transparent',
    foreground='#000000',
    opacity='.8',
    opacity_hover='.5',
    colors=('#FF4D4D', '#E87653'),
    font_family=('Arial'),
    )

# would like to be fill with a hatch??
pie_chart = pygal.Pie(style=custom_style)
pie_chart.title = 'I wish this was a custom outline'
pie_chart.add('usable city', 95)
pie_chart.add('parking spaces', 5)
pie_chart.render_to_file('/Users/karen/pyprojects/prk_story/pie.svg')
