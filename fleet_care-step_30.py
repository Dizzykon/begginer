# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: FleetCare
from tkinter import Label, Entry, Button, messagebox
from tkinter import ttk
import json

def get_user_profiles():
    with open("user_profiles.json", "r") as f:
        return json.load(f)

def save_user_profiles(profiles):
    with open("user_profiles.json", "w") as f:
        json.dump(profiles, f, indent=2)

def load_profile(profile_name):
    profiles = get_user_profiles()
    if profile_name in profiles:
        return profiles[profile_name]
    return None

def add_profile(name, email, role):
    profiles = get_user_profiles()
    profiles[name] = {"name": name, "email": email, "role": role}
    save_user_profiles(profiles)
    messagebox.showinfo("Успех", f"Профиль '{name}' добавлен")

def delete_profile(name):
    profiles = get_user_profiles()
    if name in profiles:
        del profiles[name]
        save_user_profiles(profiles)
        messagebox.showinfo("Успех", f"Профиль '{name}' удалён")
    else:
        messagebox.showwarning("Ошибка", f"Профиль '{name}' не найден")

def show_profile_dialog():
    profiles = get_user_profiles()
    for name, data in profiles.items():
        print(f"{name}: {data}")

def add_profile_ui():
    profiles = get_user_profiles()
    profile_names = list(profiles.keys())
    profile_list = ttk.Treeview(main_window, columns=("name", "email", "role"), show="headings")
    profile_list.heading("name", text="Имя")
    profile_list.heading("email", text="Email")
    profile_list.heading("role", text="Роль")
    profile_list.column("name", width=100)
    profile_list.column("email", width=200)
    profile_list.column("role", width=100)
    for name, data in profiles.items():
        profile_list.insert("", "end", values=(data["name"], data["email"], data["role"]))
    profile_list.pack(fill="both", expand=True, padx=10, pady=10)
