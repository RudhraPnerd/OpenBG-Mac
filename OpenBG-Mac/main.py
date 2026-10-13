import sys
import platform
from pathlib import Path

from rich import print
from rich.console import Console
from rich.prompt import Prompt

import funcs
import progress

operating_sys = platform.system()
console = Console()

BASE = "https://raw.githubusercontent.com/RudhraPnerd/OpenBG-Mac/main/Wallpapers"
PICTURES = Path.home() / "Pictures"
NAMES = ["bigsur", "goldengate", "monterey", "sequoia", "sonoma", "tahoe", "ventura"]


def main():
    # if operating_sys == "Windows":
    #     print("[red]Your OS is not compatible with this program. Change to MacOS[/red]")
    #     return

    console.rule("[bold]Welcome to OpenBG-Mac!")
    console.print("Your ultimate macOS wallpaper changer.", justify="center")

    wallpaper = Prompt.ask(
        "Please enter the wallpaper you want to set",
        choices=NAMES + ["quit"],
    )

    if wallpaper in NAMES:
        progress.download(f"{BASE}/{wallpaper}.heic", PICTURES / f"{wallpaper}.heic")
        getattr(funcs, f"set_{wallpaper}")()
    elif wallpaper == "quit":
        print("[red]Exiting the program. Goodbye![/red]")
        sys.exit(0)


if __name__ == "__main__":
    main()