from textual.app import App, ComposeResult
from textual.widgets import Label, Button, Header


class HolyWarApp(App[str]):
    ENABLE_COMMAND_PALETTE = False

    CSS_PATH = "question02.tcss"
    TITLE = "HolyWar"
    SUB_TITLE = "There is no truth - only war!"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label('How many apples?', id="question")
        yield Button('10', id='appl10', variant="primary")
        yield Button('None', id="none", variant="error")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(event.button.id)

if __name__ == '__main__':
    app = HolyWarApp()
    reply = app.run()
    print(reply)
