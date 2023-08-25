import time
import pytest
import tkinter as tk
from tkinter import messagebox

from mami import start_game , check_prediction

@pytest.fixture
def root():
    root = tk.Tk()
    yield root
    root.destroy()

@pytest.fixture
def game_window():
    game_window = tk.Tk()
    yield game_window
    game_window.destroy()

def test_check_prediction():
    assert check_prediction("correct", "correct", 3, time.time(), 120) == "win"
    assert check_prediction("wrong", "correct", 3, time.time(), 120) == "continue"
    assert check_prediction("correct", "correct", 0, time.time(), 120) == "out_of_chances"
    assert check_prediction("correct", "correct", 3, time.time() - 130, 120) == "out_of_time"

def test_start_game(root, game_window):
    entry_example1 = tk.Entry(root)
    entry_example2 = tk.Entry(root)
    name_var = tk.StringVar()
    name_var.set("Mami")
    
    entry_example1.insert(0, "example1")
    entry_example2.insert(0, "missing_word")
    
    name_option_menu = tk.OptionMenu(root, name_var, "Mami")
    
    start_button = tk.Button(root, text="Start Game", command=start_game)
    start_button.invoke()
    
    game_window.update()
    
    user_input_entry = game_window.winfo_children()[3]
    predict_button = game_window.winfo_children()[5]
    cheat_button = game_window.winfo_children()[6]
    
    user_input_entry.insert(0, "missing_word")
    predict_button.invoke()
    
    assert predict_button.cget("state") == "disabled"
    assert user_input_entry.cget("state") == "disabled"
    
    cheat_button.invoke()
    assert user_input_entry.get() == "missing_word"
    
    assert user_input_entry.cget("state") == "normal"

if __name__ == "__main__":
    pytest.main()
