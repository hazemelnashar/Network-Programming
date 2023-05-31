import tkinter as tk
import socket

# Create a Tkinter window
root = tk.Tk()
root.title("Guessing Game")

# Define the host and port to use for the server
HOST = 'localhost'
PORT = 7002

# Create a socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Define a function to handle sending and receiving messages
def send_receive():
    # Get the player's guess from the entry box
    guess = guess_entry.get()
    guess_entry.delete(0, tk.END)

    # Send the guess to the server
    s.send(guess.encode())

    # Receive a message from the server with the result of the guess
    result = s.recv(1024).decode()
    result_label.config(text=result)

    # Check if the game is over
    if 'Congratulations' in result:
        s.close()
    return    

# Create a label to display the server's message
message_label = tk.Label(root, text="Guess the number:")
message_label.pack()

# Create an entry box for the player's guess
guess_entry = tk.Entry(root)
guess_entry.pack()

# Create a button to send the guess to the server
send_button = tk.Button(root, text="Send", command=send_receive)
send_button.pack()

# Create a label to display the result of the guess
result_label = tk.Label(root, text="")
result_label.pack()

# Run the Tkinter event loop
root.mainloop()