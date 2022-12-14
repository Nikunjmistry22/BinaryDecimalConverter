from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.image import Image
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFillRoundFlatButton

class ConverterApp(MDApp):

    def flip(self):
        if self.state==0:
            self.state=1
            self.toolbar.title="Decimal to Binary"
            self.input.text="enter a decimal number"
            self.converted.text=""
            self.label.text=""
        else:
            self.state = 0
            self.toolbar.title = "Binary to Decimal"
            self.input.text = "enter a binary number"
            self.converted.text = ""
            self.label.text = ""
    def convert(self,args):
        try:
            if self.state==0:
                val=int(self.input.text,2)
                self.converted.text=str(val)
                self.label.text="in Decimal is"
            else:
                val = bin(int(self.input.text))[2:]
                self.converted.text = val
                self.label.text = "in Binary is"
        except:
            if self.state==0:
                self.input.text=""
                self.label.text="Enter a valid binary number!!"
            else:
                self.input.text=""
                self.label.text="Enter a valid Decimal number!!"

    def build(self):
        self.state=0
        #Screen
        screen=MDScreen()
        #TopAppBar
        self.toolbar=MDTopAppBar(title="Binary to Decimal")
        self.toolbar.pos_hint={"top":1}
        self.toolbar.right_action_items=[
            ["rotate-3d-variant", lambda x:self.flip()]]

        screen.add_widget(self.toolbar)

        #Logo
        screen.add_widget(Image(
            source="logo-removebg-preview.png",
            size_hint={1,0.6},
            pos_hint = {"center_x": 0.5,"center_y":0.67}
        ))

        #Input
        self.input=MDTextField(
            text="enter a binary number",
            halign="center",
            size_hint= {0.8,1},
            pos_hint={"center_x":0.5,"center_y":0.4},
            font_size=22
        )
        screen.add_widget(self.input)

        #Label
        self.label=MDLabel(
            text="in Decimal is",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            font_size=22,
            theme_text_color="Secondary"
        )
        self.converted=MDLabel(
            text="",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.25},
            font_style="H5",
            theme_text_color="Primary"
        )
        screen.add_widget(self.label)
        screen.add_widget(self.converted)

        #convert button
        self.button=MDFillRoundFlatButton(
            text="Convert",
            font_size=17,
            pos_hint={"center_x":0.5,"center_y":0.15},
            on_press = self.convert
        )
        screen.add_widget(self.button)
        return screen

if __name__ == '__main__':
    ConverterApp().run()