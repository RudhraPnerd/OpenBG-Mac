import funcs
import sys

print("Welcome to the OpenBG-Mac! Your ultimate macOS wallpaper changer.")

wallpaper = input("Please enter the wallpaper you want to set (bigsur, goldengate, monterey, seququoia, sonoma, tahoe, ventura): ").strip().lower()

if wallpaper == "bigsur":
    funcs.set_bigsur()
elif wallpaper == "goldengate":
    funcs.set_goldengate()
elif wallpaper == "monterey":
    funcs.set_monterey()
elif wallpaper == "seququoia":
    funcs.set_seququoia()
elif wallpaper == "sonoma":
    funcs.set_sonoma()
elif wallpaper == "tahoe":
    funcs.set_tahoe()
elif wallpaper == "ventura":
    funcs.set_ventura()
elif wallpaper == "quit":
    print("Exiting the program. Goodbye!")
    sys.exit(0)
else:
    print("Invalid wallpaper selection.")
