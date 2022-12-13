from console import console
from rich.panel import Panel
from rich.console import Group
from rich.text import Text
from rich.markdown import Markdown
from rich.prompt import IntPrompt, Prompt
from rich.table import Table
from database import select, getAllTables, insert, getTableInfo, getTablePK, delete, execute

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


def app(connection):

    allOptions = ['Select', 'Insert', 'Delete', 'Valoraciones de usuarios con rango "Moises"', 'Videojuegos que tienen genero "Meyo"', 'Editores que viven en la calle1', 'Usuarios que por su rango tengan un descuento_unico mayor a 8', 'Exit']
    allTables = getAllTables(connection.cursor())

    lm = ""
    ls = ""

    for o in allOptions:
        lm += "1. " + o + "\n"

    for t in allTables:
        ls += "1. " + t + "\n"

    main_panel_content = Group(Text.from_markup("[bold red]Options"), Markdown(lm))
    main_panel = Panel(main_panel_content)

    select_panel_content = Group(Text.from_markup("[bold red]Tables"), Markdown(ls))
    select_panel = Panel(select_panel_content)

    option = None
    while option != len(allOptions):
        console.print(Panel(Text.from_markup("[bold]DATABASE FINAL PROJECT", style='red on white', justify="center")))
        console.print(main_panel)
        option = IntPrompt.ask("Select an option", choices=[str(x + 1) for x in range(len(allOptions))])
        console.print(str(option) + ' ' + allOptions[option - 1], style="bold italic blue")
        match option:
            case 1:
                console.print(select_panel)
                t = IntPrompt.ask("Select a table", choices=[str(x + 1) for x in range(len(allTables))])
                x = select(connection.cursor(), allTables[t - 1])
                console.print(createTable(x))
                console.print("Rows: " + str(len(x[2])), style="italic blue")

            case 2:
                console.print(select_panel)
                t = IntPrompt.ask("Select a table", choices=[str(x + 1) for x in range(len(allTables))])
                
                allColumns = getTableInfo(connection.cursor(), allTables[t - 1])
                console.print("[bold red]Complete the data")
                listnCol = []
                listnData = []
                for c in allColumns[1]:
                    if c[1] == 'varchar':
                        ndata = Prompt.ask(c[0] + " [italic blue](" + c[1] + ")")
                        ndata = "'" + ndata + "'"
                    if c[1] == 'int':
                        ndata = IntPrompt.ask(c[0] + " [italic blue](" + c[1] + ")")
                        ndata = str(ndata)
                    listnCol.append(c[0])
                    listnData.append(ndata)
                insert(connection, [allTables[t - 1], listnCol, listnData])

            case 3:
                console.print(select_panel)
                t = IntPrompt.ask("Select a table", choices=[str(x + 1) for x in range(len(allTables))])
                
                pk = getTablePK(connection.cursor(), "RANGO")
                ndata = IntPrompt.ask("[bold red]PK value of the row [italic blue](" + pk + ")")
                delete(connection, [allTables[t - 1], pk, str(ndata)])

            case 4:
                x = execute(connection.cursor(), 'SELECT u.nombre, v.comentario FROM VALORACION AS v JOIN USUARIO AS u ON (v.CLIENTE_idCLIENTE = u.idCLIENTE) JOIN RANGO AS r ON (u.RANGO_idRANGO = r.idRANGO) WHERE r.nombre = "Moises"')
                console.print(createTable([allOptions[option - 1]] + x))
                console.print("Rows: " + str(len(x[1])), style="italic blue")
            
            case 5:
                x = execute(connection.cursor(), 'SELECT v.nombre FROM GENERO_has_VIDEOJUEGO gv JOIN GENERO g ON (gv.GENERO_idGENERO = g.idGENERO) JOIN VIDEOJUEGO v ON (gv.VIDEOJUEGO_idVIDEOJUEGO = v.idVIDEOJUEGO) WHERE g.nombre = "Meyo"')
                console.print(createTable([allOptions[option - 1]] + x))
                console.print("Rows: " + str(len(x[1])), style="italic blue")

            case 6:
                x = execute(connection.cursor(), 'SELECT e.nombre FROM EDITOR e JOIN UBICACION u ON (e.UBICACION_idUBICACION = u.idUBICACION) WHERE u.calle = "calle1"')
                console.print(createTable([allOptions[option - 1]] + x))
                console.print("Rows: " + str(len(x[1])), style="italic blue")

            case 7:
                x = execute(connection.cursor(), 'SELECT u.nombre, u.correo FROM USUARIO AS u JOIN RANGO AS r ON (u.RANGO_idRANGO = r.idRANGO) WHERE r.descuento_unico > 8')
                console.print(createTable([allOptions[option - 1]] + x))
                console.print("Rows: " + str(len(x[1])), style="italic blue")

            case _:
                pass
