from console import console
from rich.panel import Panel
from rich.console import Group
from rich.text import Text
from rich.markdown import Markdown
from rich.prompt import IntPrompt
from rich.table import Table
from database import selectExample

def createTable(l):
    title = l[0]
    names = l[1]
    data = l[2]

    table = Table(title=title)
    for name in names:
        table.add_column(name)
    
    for d in data:
        x = [str(y) for y in d]

        table.add_row(*x)
    
    return table


def app(cursor):

    allOptions = ['Select', 'Insert', 'Delete', 'Exit']

    l = ""

    for o in allOptions:
        l += "1. " + o + "\n"

    main_panel_content = Group(Text.from_markup("[bold red]Options"), Markdown(l))
    main_panel = Panel(main_panel_content)

    select_panel_content = Group(Text.from_markup("[bold red]Options"), Markdown(l))
    select_panel = Panel(select_panel_content)

    option = None
    while option != len(allOptions):
        console.print(Panel(Text.from_markup("[bold]DATABASE FINAL PROJECT", style='red on white', justify="center")))
        console.print(main_panel)
        option = IntPrompt.ask("Enter name", choices=[str(x + 1) for x in range(len(allOptions))])
        console.print(str(option) + ' ' + allOptions[option - 1], style="bold italic blue")
        match option:
            case 1:
                l = selectExample(cursor, "USUARIO")
                console.print(createTable(l))
            case 2:
                console.print(allOptions[1])
            case 3:
                console.print(allOptions[2])
            case _:
                pass
