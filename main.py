from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.clock import Clock
import random

class MemoryGame(App):
    def build(self):
        self.cards = list(range(10)) * 2
        random.shuffle(self.cards)
        self.layout = GridLayout(cols=4, rows=5)
        self.buttons = []
        self.first_card = None
        self.second_card = None
        self.matched_pairs = 0

        for i in range(20):
            button = Button(text='?', font_size=70, size_hint=(0.2, 0.2), background_color=(0, 0, 0, 1))
            button.bind(on_press=self.on_button_press)
            self.layout.add_widget(button)
            self.buttons.append(button)

        return self.layout

    def on_button_press(self, instance):
        index = self.buttons.index(instance)
        if self.first_card is None:
            self.first_card = index
            instance.text = str(self.cards[index])
        elif self.second_card is None and index != self.first_card:
            self.second_card = index
            instance.text = str(self.cards[index])
            self.check_match()

    def check_match(self):
        if self.cards[self.first_card] == self.cards[self.second_card]:
            self.buttons[self.first_card].background_color = (0, 1, 0, 1)  # Green color
            self.buttons[self.second_card].background_color = (0, 1, 0, 1)  # Green color
            self.matched_pairs += 1
            self.first_card = None
            self.second_card = None
            if self.matched_pairs == 10:
                self.show_congratulations()
        else:
            self.buttons[self.first_card].background_color = (1, 0, 0, 1)  # Red color
            self.buttons[self.second_card].background_color = (1, 0, 0, 1)  # Red color
            Clock.schedule_once(self.reset_cards, 2)

    def reset_cards(self, dt):
        self.buttons[self.first_card].text = '?'
        self.buttons[self.second_card].text = '?'
        self.buttons[self.first_card].background_color = (0, 0, 0, 1)  # Reset to black color
        self.buttons[self.second_card].background_color = (0, 0, 0, 1)  # Reset to black color
        self.first_card = None
        self.second_card = None

    def show_congratulations(self):
        popup = Popup(title="congratulations", content=Label(text="You win"), size_hint=(0.5, 0.5))
        popup.open()

if __name__ == '__main__':
    MemoryGame().run()
