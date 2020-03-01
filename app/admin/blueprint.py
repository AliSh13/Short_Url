from flask_admin import BaseView, expose


class AnalyticsView(BaseView):
    @expose('/')
    def index(self):
        pass
        # return self.render('analytics_index.html')

