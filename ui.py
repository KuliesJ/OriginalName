from console import console
from rich.panel import Panel
from rich.console import Group
from rich.text import Text
from rich.markdown import Markdown
from rich.prompt import IntPrompt, Prompt
from rich.table import Table
from rich.align import Align
from database import select, getAllTables, insert, getTableInfo, getTablePK, delete, execute

def createTable(l):
    title = l[0]
    names = l[1]
    data = l[2]

    table = Table(title=title, title_style="italic cyan", row_styles=["white", "grey82"])
    for name in names:
        table.add_column(name)
    
    for d in data:
        x = [str(y) for y in d]

        table.add_row(*x)
    
    return Align(Panel(Group(table, "[italic blue]Rows: [cyan]" + str(len(data))), expand=False), "center")


def app(connection):

    allOptions = ['Select', 'Insert', 'Delete', 'Valoraciones de usuarios con rango "X"', 'Videojuegos que tienen genero "X"', 'Editores que viven en la calle "X"', 'Usuarios que por su rango tengan un descuento unico mayor a X', 'Exit']
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
        console.print(Panel(Text.from_markup("[bold]DATABASE FINAL PROJECT", style='red', justify="center")))
        console.print(main_panel)
        option = IntPrompt.ask("Select an option", choices=[str(x + 1) for x in range(len(allOptions))])
        console.print(str(option) + ' ' + allOptions[option - 1], style="bold italic blue")
        match option:
            case 1:
                console.print(select_panel)
                t = IntPrompt.ask("Select a table", choices=[str(x + 1) for x in range(len(allTables))])
                x = select(connection.cursor(), allTables[t - 1])
                console.print(createTable(x))
                
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
                
                pk = getTablePK(connection.cursor(), allTables[t - 1])
                ndata = IntPrompt.ask("[bold red]PK value of the row [italic blue](" + pk + ")")
                delete(connection, [allTables[t - 1], pk, str(ndata)])

            case 4:
                sample4 = Prompt.ask("Obtener los comentarios dejados por usuarios que tengan el rango", default="Moises")
                x = execute(connection.cursor(), 'SELECT u.nombre, v.comentario FROM VALORACION AS v JOIN USUARIO AS u ON (v.CLIENTE_idCLIENTE = u.idCLIENTE) JOIN RANGO AS r ON (u.RANGO_idRANGO = r.idRANGO) WHERE r.nombre = "{}"'.format(sample4))
                console.print(createTable([allOptions[option - 1].replace("X", sample4)] + x))
            
            case 5:
                sample5 = Prompt.ask("Obtener los juegos que tengan el genero", default="Meyo")
                x = execute(connection.cursor(), 'SELECT v.nombre, v.horas_de_juego, v.precio  FROM GENERO_has_VIDEOJUEGO gv JOIN GENERO g ON (gv.GENERO_idGENERO = g.idGENERO) JOIN VIDEOJUEGO v ON (gv.VIDEOJUEGO_idVIDEOJUEGO = v.idVIDEOJUEGO) WHERE g.nombre = "{}"'.format(sample5))
                console.print(createTable([allOptions[option - 1].replace("X", sample5)] + x))

            case 6:
                sample6 = Prompt.ask("Obtener los editores que vivan en la calle", default="calle1")
                x = execute(connection.cursor(), 'SELECT e.nombre, e.correo, u.numero FROM EDITOR e JOIN UBICACION u ON (e.UBICACION_idUBICACION = u.idUBICACION) WHERE u.calle = "{}"'.format(sample6))
                console.print(createTable([allOptions[option - 1].replace("X", sample6)] + x))

            case 7:
                sample7 = IntPrompt.ask("Obtener usuarios que tengan un descuento mayor a", default="0")
                x = execute(connection.cursor(), 'SELECT u.nombre, u.correo, r.descuento_unico FROM USUARIO AS u JOIN RANGO AS r ON (u.RANGO_idRANGO = r.idRANGO) WHERE r.descuento_unico > {}'.format(str(sample7)))
                console.print(createTable([allOptions[option - 1].replace("X", str(sample7))] + x))

            case _:
                pass
        if option != 8:
            Prompt.ask("Press [magenta]Enter[/] to continue")
