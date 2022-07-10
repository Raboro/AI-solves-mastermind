from dataclasses import dataclass, field
import PySimpleGUI as sg


class Layout:

    @staticmethod
    def generate_layout() -> list:
        return [
            #  Rules
            [
                sg.Frame(
                    title="Rules",
                    title_location="n",
                    relief="raised",
                    border_width=4,
                    size=(900, 50),
                    layout=[
                        [
                            sg.Checkbox("Every color only one time in combination", pad=(10, 0)), 
                            sg.Checkbox("Only one color", pad=(10, 0)), 
                            sg.Checkbox("Color max two times in combo", pad=(10, 0)), 
                            sg.Checkbox("Color max three times in combo", pad=(10, 0))
                        ]
                    ]
                )
            ],

            #  Seperator
            [
                sg.HorizontalSeparator(pad=(0, 20))
            ],

            #  Colors
            [
                sg.Frame(
                    title="Colors",
                    title_location="n",
                    relief="raised",
                    border_width=4,
                    size=(900, 50),
                    layout=[
                        [
                            sg.Checkbox("Color white", pad=(10, 0)),
                            sg.Checkbox("Color black", pad=(10, 0)),
                            sg.Checkbox("Color red", pad=(10, 0)),
                            sg.Checkbox("Color green", pad=(10, 0)),
                            sg.Checkbox("Color yellow", pad=(10, 0)),
                            sg.Checkbox("Color blue", pad=(10, 0)),
                            sg.Checkbox("Color lila", pad=(10, 0)),
                            sg.Checkbox("Color orange", pad=(10, 0))
                        ]
                    ]
                ),
                
            ],
            
            #  Seperator
            [
                sg.HorizontalSeparator(pad=(0, 20))
            ],

            #  Text
            [
                sg.Text("Create Combination")
            ],

            #  Button Combination Input
            [
                sg.Button("1"),
                sg.Button("2"),
                sg.Button("3"),
                sg.Button("4")
            ],

            #  Submit
            [
                sg.Button(
                    "Submit", 
                    pad=((355, 355), (0,0)),
                    size=(25, 2)
                    )
            ]
        ]


@dataclass(slots=True)
class GuiMastermind:

    layout: object = field(init=False)
    window: sg.Window = field(init=False)


    def create_layout(self) -> None:
        self.layout = Layout.generate_layout()

    def create_window(self) -> None:
        self.window = sg.Window("AI solves mastermind", layout=self.layout, location=(550, 600))

    def event_loop(self) -> None:
        while True:

            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED:
                break

        self.window.close()