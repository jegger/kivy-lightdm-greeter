import sys

from kivy.app import App
from kivy.support import install_gobject_iteration
from kivy.lang import Builder
from kivy.core.window import Window

#from gi.repository import LightDM

kv = '''
FloatLayout:
    username_spinner: username_spinner
    session_spinner: session_spinner
    info_label: info_label
    AnchorLayout:
        BoxLayout:
            size_hint: None, None
            size: 700, 280
            info_label: info_label
            orientation: 'vertical'
            GridLayout:
                cols: 2
                spacing: 5
                Label:
                    text: "Session"
                    haling: 'middle'
                    valing: 'left'
                    text_size: self.size
                    font_size: 40
                Spinner:
                    id: session_spinner
                    font_size: 40
                    text: self.values[0] if self.values else ""
                Label:
                    text: "Username"
                    haling: 'middle'
                    valing: 'left'
                    text_size: self.size
                    font_size: 40
                Spinner:
                    id: username_spinner
                    font_size: 40
                    text: self.values[0] if self.values else ""
                Label:
                    text: "Password"
                    haling: 'middle'
                    valing: 'left'
                    text_size: self.size
                    font_size: 40
                TextInput:
                    id: password_input
                    text: ""
                    password: True
                    font_size: 40
                    multiline: False
                    background_normal: 'images/textinput.png'
                    background_active: 'images/textinput-active.png'
                    on_text_validate:
                        login_button.trigger_action()
            Label:
                id: info_label
                size_hint_y: None
                height: 30
                color: 1,0,0,1
            Button:
                id: login_button
                text: "Login"
                size_hint_y: 0.3
                on_press: app.login(username_spinner.text, password_input.text, session_spinner.text)
    Image:
        source: 'images/kivy_logo.png'
        size: 183,120
        pos: (self.parent.width-self.width)/2, 50
        size_hint: None, None
'''


class GreeterApp(App):

    def __init__(self, **kwargs):
        super(GreeterApp, self).__init__(**kwargs)
        self.password = ""
        self.session = ""

        self.available_sessions = ["kde-plasma", "pbase"]
        self.available_users = ["rentouch", "hansli"]
        self.root_widget = Builder.load_string(kv)
        self.root_widget.username_spinner.values = self.available_users
        self.root_widget.session_spinner.values = self.available_sessions

    def build(self):
        install_gobject_iteration()
        """self.greeter = LightDM.Greeter()
        self.greeter.connect("authentication-complete", self.authentication_complete_cb)
        self.greeter.connect("show-prompt", self.show_prompt_cb)
        self.greeter.connect_sync()
        sessions =  LightDM.get_sessions()
        for sess in sessions:
            print LightDM.Session.get_name(sess)
            """

        return self.root_widget

    def login(self, username, password, session):
        self.password = password
        self.session = session
        print >> sys.stderr, "Initial entry of username, send it to LightDM"
        self.greeter.authenticate(username)

    def show_prompt_cb(self, greeter, text, promptType):
        print >> sys.stderr, "prompt type: " + str(promptType) + str(text)
        if greeter.get_in_authentication():
            greeter.respond(self.password)

    def authentication_complete_cb(self, greeter):
        if greeter.get_is_authenticated():
            session = "kde-plasma"
            if not greeter.start_session_sync(session):
                self.root_widget.info_label.text = "Error while starting session %s" % session
            else:
                print >> sys.stderr, "AUTH COMPLETED"
                self.root_widget.info_label.text = ":-)"
                self.stop()
        else:
            print >> sys.stderr, "Login failed"
            self.root_widget.info_label.text = "Wrong credentials :-("


if __name__ == '__main__':
    Window.clearcolor = (0.4274509804, 0.4274509804, 0.4274509804, 1)
    GreeterApp().run()
