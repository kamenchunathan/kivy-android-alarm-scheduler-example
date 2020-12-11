from kivymd.app import MDApp
from kivy.logger import Logger
from kivy import platform


class TodoApp(MDApp):
    title = 'Todo'
    @staticmethod
    def set_alarm():
        Logger.debug('App: set alarm called')
        if platform == 'android':
            Logger.info('App: scheduling task')
            import schedule_task
            schedule_task.schedule_task()


if __name__ == '__main__':
    TodoApp().run()
