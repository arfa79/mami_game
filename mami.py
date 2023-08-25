import time
import tkinter as tk
from tkinter import messagebox

def check_prediction(user_input, missing_word, chances, start_time, timer_duration):
    if user_input == missing_word:
        return "win"
    elif chances == 0:
        return "out_of_chances"
    elif time.time() - start_time > timer_duration:
        return "out_of_time"
    else:
        return "continue"

def start_game():
    example1 = entry_example1.get()
    missing_word = entry_example2.get()
    
    root.destroy()  # Close the setup window
    
    game_window = tk.Tk()
    game_window.title("Mami Game - Predictions")
    
    tk.Label(game_window, text="Predict 'missing word' as mami" , font=("Helvetica", 14)).pack(pady=10)
    
    chances = 3
    hearts = "❤️" * chances
    hearts_label = tk.Label(game_window, text=hearts, font=("Helvetica", 20))
    hearts_label.pack()
    
    timer_duration = 120  # 2 minutes in seconds
    start_time = time.time()
    timer_label = tk.Label(game_window, text="", font=("Helvetica", 20))
    timer_label.pack()

    def update_timer():
        elapsed_time = int(time.time() - start_time)
        remaining_time = max(timer_duration - elapsed_time, 0)
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
        if remaining_time > 0:
            game_window.after(1000, update_timer)
        else:
            game_over("Time's up! You've run out of time.")

    update_timer()

    user_input_entry = tk.Entry(game_window)
    user_input_entry.pack(pady=10)

    def predict():
        nonlocal chances, hearts
        user_input = user_input_entry.get()
        
        result = check_prediction(user_input, missing_word, chances, start_time, timer_duration)
        
        if result == "win":
            game_over("Congratulations! You've won!", game_window)
        elif result == "out_of_chances":
            game_over("Sorry, you've run out of chances. Better luck next time!", game_window)
        elif result == "out_of_time":
            game_over("Time's up! You've run out of time.", game_window)
        else:
            chances -= 1
            hearts = "❤️" * chances
            hearts_label.config(text=hearts)
            user_input_entry.delete(0, tk.END)
            if chances == 0:
                game_over("Sorry, you've run out of chances. Better luck next time!", game_window)

    def game_over(result_text, window):
        tk.Label(window, text=result_text, font=("Helvetica", 14)).pack(pady=10)
        user_input_entry.destroy()
        timer_label.config(text="00:00")
        predict_button.config(state=tk.DISABLED)
    def cheat () :
        return game_over('arfaaaaaaaa !!! you are goddamn right! victory is yours now :)' , game_window)
    user_input_entry = tk.Entry(game_window)
    user_input_entry.pack(pady=10)

    predict_button = tk.Button(game_window, text="Predict", command=predict)
    predict_button.pack(pady=10)
    predict_button = tk.Button(game_window, text="say my name", command=cheat)
    predict_button.pack(pady=10)

    game_window.mainloop()

root = tk.Tk()
root.title("Mami Game")

sentence = "Mami ke 'example1' bashe behesh migan 'missing_word'"

# GUI Elements (setup)
tk.Label(root, text="Welcome to the Mami Game!", font=("Helvetica", 16)).pack(pady=10)
tk.Label(root, text="Enter 'word':").pack()
entry_example1 = tk.Entry(root)
entry_example1.pack()
tk.Label(root, text="Enter 'missing word':").pack()
entry_example2 = tk.Entry(root)
entry_example2.pack()
start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack(pady=10)

root.mainloop()