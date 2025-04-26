import sys
import subprocess

from dotenv import load_dotenv

def main():

    load_dotenv('keys.env')  # Load environment variables from .env file

    while True:
        choice = input("Do you want to launch the CLI or GUI? (cli/gui): ").lower()
        if choice in ('cli', 'gui'):
            break
        print("Invalid choice. Please enter 'cli' or 'gui'.")

    try:
        if(choice == 'cli'):
            print("Launching CLI...")
            subprocess.run(['tradebot_cli'], check=True) # is a non-interatice process

            '''
            process = subprocess.Popen(
                    ["tradebot_cli"],
                    stdin=subprocess.PIPE,  # To send input
                    stdout=subprocess.PIPE,  # To read output
                    stderr=subprocess.PIPE,  # To read errors
                    text=True,  # To use strings instead of bytes
                    bufsize=1,
                    shell=True
                )
            # While the process is still running
            while process.poll() is None:

                command = input("Enter command: ")  # Get input from the user

                process.stdin.write(command + "\n") # Send the command to the CLI
                process.stdin.flush()
                output = process.stdout.readline() # Read a line of output
                print("CLI output:", output.strip())

            # Get the return code when the process finishes
            return_code = process.wait()
            print(f"CLI exited with code: {return_code}")
        '''

        elif(choice == 'gui'):
            print("Launching GUI...")
            subprocess.run(['tradebot_gui'], check=True)
        else:
            print("Invalid choice.  This should not happen due to the input validation.")
            sys.exit(1)

    except subprocess.CalledProcessError as e:
        print("Error launching CLI: {}".format(e)) #
        sys.exit(1)

    except FileNotFoundError:
        print("Error: {} executable not found.  Ensure the application is installed correctly and the entry points are configured in setup.py.".format(choice.upper())) # corrected
        sys.exit(1)

if __name__ == "__main__":
    main()
