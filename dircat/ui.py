# from rich.console import Console
# from rich.panel import Panel
# from rich.table import Table
# from rich import box
# from rich.align import Align
# from rich.text import Text
# from rich.spinner import Spinner
# from rich.live import Live
# import time

# console = Console()


# # -----------------------------
# # 🏠 Home UI
# # -----------------------------
# def show_home():
#     logo = Text()
#     logo.append("🐱 DirCat\n", style="bold cyan")
#     logo.append("Instant project structure generator\n", style="dim")

#     console.print(Panel(Align.center(logo), border_style="cyan"))

#     # Commands table
#     table = Table(title="Commands", box=box.ROUNDED, expand=True)

#     table.add_column("Command", style="green", no_wrap=True)
#     table.add_column("Description", style="white")

#     table.add_row("dircat file.txt", "Create project from JSON / TXT / tree")
#     table.add_row("dircat create file.txt", "Explicit create command")
#     table.add_row("dircat --template ml", "Use built-in template")
#     table.add_row("dircat --dry-run", "Preview without creating files")
#     table.add_row("dircat --force", "Overwrite existing files")
#     table.add_row("dircat --here", "Create in current directory")
#     table.add_row("dircat '{json}'", "Inline JSON input")

#     console.print(table)

#     # Examples
#     console.print("\n[bold yellow]Examples:[/bold yellow]")
#     console.print("  dircat tree.txt")
#     console.print("  dircat test.json")
#     console.print("  dircat --template basic")
#     console.print("  dircat '{\"root\":\"app\",\"files\":[\"main.py\"]}'")

#     # Footer
#     console.print("\n[dim]✨ Tip: Paste GPT output directly — DirCat understands it[/dim]")
#     console.print("[dim]🚀 Built for fast vibe coding[/dim]\n")


# # -----------------------------
# # 🌀 Cute Loader Animation
# # -----------------------------
# def show_loader(message="Creating project..."):
#     spinner = Spinner("dots", text=f"[cyan]{message}[/cyan] 🐾")

#     return spinner


# # -----------------------------
# # 🎉 Success Message
# # -----------------------------
# def show_success():
#     console.print("\n[bold green]✅ Project created successfully![/bold green] 🐱\n")


from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
from rich.align import Align
from rich.text import Text
from rich.spinner import Spinner

console = Console()


# -----------------------------
# 🏠 Home UI (Clean Original Theme)
# -----------------------------
def show_home():
    # 🐱 ASCII logo (balanced, no extra bottom space)
    cat = Text()
    cat.append("   /\\_/\\\n", style="magenta")
    cat.append("  ( o.o )\n", style="magenta")
    cat.append("  (  =  )\n", style="magenta")
    cat.append("   > ^ <", style="magenta")  # no trailing newline

    # Right side text
    text = Text()
    text.append("DirCat 🐱\n", style="bold cyan")
    text.append("Instant project structure generator\n", style="dim")
    text.append("version 1.0.0\n", style="dim")
    text.append("developer - A3x-parvez", style="dim italic")

    # Layout
    header = Table.grid(padding=(0, 5))
    header.add_column(ratio=1)
    header.add_column(ratio=3)

    header.add_row(
        Align(cat, vertical="middle"),
        Align(text, vertical="middle")
    )

    console.print(
        Panel(
            header,
            border_style="cyan",
            expand=True,
            padding=(1, 2)
        )
    )

    # -----------------------------
    # Commands table
    # -----------------------------
    table = Table(
        title="Commands",
        box=box.ROUNDED,
        expand=True,
        border_style="cyan"
    )

    table.add_column("Command", style="green", no_wrap=True)
    table.add_column("Description", style="white")

    table.add_row("dircat file.txt", "Create project from JSON / TXT / tree")
    table.add_row("dircat create file.txt", "Explicit create command")
    table.add_row("dircat --template ml", "Use built-in template")
    table.add_row("dircat --dry-run", "Preview without creating files")
    table.add_row("dircat --force", "Overwrite existing files")
    table.add_row("dircat --here", "Create in current directory")
    table.add_row("dircat '{json}'", "Inline JSON input")

    console.print(table)

    
    # -----------------------------
    # Examples
    # -----------------------------
    console.print("\n[bold white]> Examples[/bold white]")

    console.print("  [dim]$[/dim] [cyan]dircat[/cyan] [green]tree.txt[/green]")
    console.print("  [dim]$[/dim] [cyan]dircat[/cyan] [green]test.json[/green]")
    console.print("  [dim]$[/dim] [cyan]dircat[/cyan] [magenta]--template[/magenta] [green]basic[/green]")
    console.print("  [dim]$[/dim] [cyan]dircat[/cyan] [yellow]'{\"root\":\"app\",\"files\":[\"main.py\"]}'[/yellow]")

    console.print("\n")  # spacing

    # -----------------------------
    # Footer
    # -----------------------------
    console.print("[bold white]> Tip:[/bold white] [dim]paste GPT output directly — dircat understands it[/dim]")
    console.print("[dim]> built for fast vibe coding 🚀[/dim]")

    # console.print("\n")
    
# -----------------------------
# 🌀 Loader Animation
# -----------------------------
def show_loader(message="Creating project..."):
    return Spinner("dots", text=f"[cyan]{message}[/cyan] 🐾")


# -----------------------------
# 🎉 Success Message
# -----------------------------
def show_success():
    console.print("[bold green]✔ Project created successfully[/bold green] 🐱")