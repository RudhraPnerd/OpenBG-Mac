import subprocess
import os

def _run_wallpaper_script(script_name: str) -> bool:
    """
    Helper function to safely locate and execute a wallpaper shell script
    stored inside the 'Functions' subfolder.
    """
    # Get the directory where this current Python file lives
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 🌟 FIX: This tells Python to go inside the Functions directory first
    script_path = os.path.join(current_dir, "Functions", script_name)
    
    # Check if the script file exists locally
    if not os.path.exists(script_path):
        print(f"Error: Script file not found at {script_path}")
        return False
        
    try:
        # Run the script using the recommended subprocess module
        result = subprocess.run([script_path], capture_output=True, text=True, check=True)
        print(f"Successfully changed wallpaper using {script_name}!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to run {script_name}.")
        print(f"Error Output: {e.stderr}")
        return False



def set_bigsur() -> bool:
    """Changes the macOS wallpaper to Big Sur."""
    return _run_wallpaper_script("set_bigsur.sh")

def set_goldengate() -> bool:
    """Changes the macOS wallpaper to Golden Gate."""
    return _run_wallpaper_script("set_goldengate.sh") 

def set_monterey() -> bool:
    """Changes the macOS wallpaper to Monterey."""
    return _run_wallpaper_script("set_monterey.sh")

def set_seququoia() -> bool:
    """Changes the macOS wallpaper to Sequoia."""
    return _run_wallpaper_script("set_seququoia.sh")

def set_sonoma() -> bool:
    """Changes the macOS wallpaper to Sonoma."""
    return _run_wallpaper_script("set_sonoma.sh")

def set_tahoe() -> bool:
    """Changes the macOS wallpaper to Tahoe."""
    return _run_wallpaper_script("set_tahoe.sh")

def set_ventura() -> bool:
    """Changes the macOS wallpaper to Ventura."""
    return _run_wallpaper_script("set_ventura.sh")