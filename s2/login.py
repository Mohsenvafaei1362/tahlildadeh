# import kivy
# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout  # Import BoxLayout

# class LoginApp(App):
#     def build(self):
#         self.title = 'Login App'

#         layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
#         layout.background_color = (0.9, 0.9, 0.9, 1)  # رنگ پس‌زمینه خاکستری روشن

#          # عنوان
#         title_label = Label(text='ورود به سیستم', font_size=24, bold=True, halign='center')
#         layout.add_widget(title_label)

#         # Create elements
#         username = TextInput(text='Username', multiline=False)
#         password = TextInput(text='Password', password=True, multiline=False)
#         login_button = Button(text='Login')
#         login_button.bind(on_press=self.login)

#         # Layout elements
#         layout = BoxLayout(orientation='vertical')
#         layout.add_widget(username)
#         layout.add_widget(password)
#         layout.add_widget(login_button)

#         return layout

#     def login(self, instance):
#         # ... (Your login logic here)
#         username_text = self.root.children[0].text
#         password_text = self.root.children[1].text
#         print('Username:', username_text)
#         print('Password:', password_text)

# if __name__ == '__main__':
#     LoginApp().run()
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginApp(App):
    def build(self):
        self.title = 'Login App'

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.background_color = (0.9, 0.9, 0.9, 1)  # رنگ پس‌زمینه خاکستری روشن

        # عنوان
        title_label = Label(text='ورود به سیستم', font_size=24, bold=True, halign='center')
        layout.add_widget(title_label)

        # فیلد نام کاربری
        username = TextInput(hint_text='نام کاربری', multiline=False, size_hint=(1, None), height=40)
        layout.add_widget(username)

        # فیلد رمز عبور
        password = TextInput(hint_text='رمز عبور', password=True, multiline=False, size_hint=(1, None), height=40)
        layout.add_widget(password)

        # دکمه ورود
        login_button = Button(text='ورود', size_hint=(1, None), height=40)
        login_button.bind(on_press=self.login)
        layout.add_widget(login_button)

        return layout

    def login(self, instance):
         # ... (Your login logic here)
        username_text = self.root.children[0].text
        password_text = self.root.children[1].text
        print('Username:', username_text)
        print('Password:', password_text)

if __name__ == '__main__':
    LoginApp().run()