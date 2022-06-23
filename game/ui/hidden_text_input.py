from game.ui.text_input import TextInput


class HiddenTextInput(TextInput):
    def get_displayed_text(self):
        return "*" * len(self.text)
