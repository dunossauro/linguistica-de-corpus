from bokeh.plotting import figure
from bokeh.charts import Bar
from bokeh.embed import file_html
from bokeh.resources import CDN

class Grap:
    def __init__(self, page):
        self.data = {'Palavras': [],
                'frequência': []}
        self.page = page

    def mount_dict(self):
        pass

    def mount_bar_grap(self):
        bar = Bar(self.data,
                   values = 'frequência',
                   label = 'Palavras',
                   title = self.page)

        return file_html(bar, CDN)
