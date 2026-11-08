import tkinter as tk

def send_message():
    user_text = entry_box.get()
    if user_text:
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"Customer: {user_text}\n\n", "user")
        entry_box.delete(0, tk.END)
        
        chat_area.insert(tk.END, "PayMate AI: Analyzing your request...\n", "bot")
        chat_area.insert(tk.END, "PayMate AI: Generating secure PayPal invoice link...\n", "bot")
        
        dynamic_link = f"https://sandbox.paypal.com/checkout/instant?item={user_text.replace(' ', '_')}&token=paymate_ai_live_2026"
        
        chat_area.insert(tk.END, f"Link: {dynamic_link}\n\n", "link")
        chat_area.config(state=tk.DISABLED)
        chat_area.yview(tk.END)

root = tk.Tk()
root.title("PayMate AI Pro")
root.geometry("500x650")
root.configure(bg="#1c1c1c")

title_label = tk.Label(root, text="⚡ PayMate AI Checkout ⚡", font=("Helvetica", 18, "bold"), bg="#1c1c1c", fg="#e60000")
title_label.pack(pady=15)

chat_area = tk.Text(root, bg="#2d2d2d", fg="white", font=("Consolas", 12), bd=0, padx=15, pady=15, wrap=tk.WORD)
chat_area.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

chat_area.tag_config("user", foreground="#00ffcc", font=("Consolas", 12, "bold"))
chat_area.tag_config("bot", foreground="#ff3333", font=("Consolas", 12, "bold"))
chat_area.tag_config("link", foreground="#3399ff", font=("Consolas", 12, "underline"))

chat_area.insert(tk.END, "PayMate AI: Hello! How can I help you with your order today?\n\n", "bot")
chat_area.config(state=tk.DISABLED)

entry_frame = tk.Frame(root, bg="#1c1c1c")
entry_frame.pack(fill=tk.X, padx=20, pady=15)

entry_box = tk.Entry(entry_frame, font=("Helvetica", 14), bg="#404040", fg="white", bd=0, insertbackground="white")
entry_box.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8, padx=(0, 10))

send_button = tk.Button(entry_frame, text="Send 🚀", font=("Helvetica", 12, "bold"), bg="#e60000", fg="white", bd=0, activebackground="#ff3333", activeforeground="white", command=send_message)
send_button.pack(side=tk.RIGHT, ipadx=15, ipady=5)

root.mainloop()
