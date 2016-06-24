from system.core.controller import *

class Friends(Controller):
    def __init__(self, action):
        super(Friends, self).__init__(action)

        self.load_model('Friend')
        self.db = self._app.db

    def index(self):
        friends=self.models['Friend'].get_all()
        return self.load_view('index.html', friends=friends)

    def show(self, id):
        friends=self.models['Friend'].get_by_id(id)
        return self.load_view('show.html', friend=friends)

    def add(self):
        return self.load_view('update.html')

    def update(self, id):
        friends=self.models['Friend'].get_by_id(id)
        return self.load_view('update.html', friend=friends)

    def delete_process(self, id):
        friend=self.models['Friend'].get_by_id(id)
        if friend:
            self.models['Friend'].delete_friend(id)
        return redirect('/')

    def add_process(self):
        self.models['Friend'].insert_friend(request.form)
        return redirect('/')

    def update_process(self, id):
        self.models['Friend'].update_friend(request.form, id)
        return redirect('/')

    def delete(self, id):
        friends=self.models['Friend'].get_by_id(id)
        return self.load_view('delete.html', id=id, friend=friends)
