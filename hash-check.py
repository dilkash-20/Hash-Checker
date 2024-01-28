import hashlib
import tkinter as tk

def generate_hash(text, hash_type):
    """
    Generate the hash of a string using a given hash type (MD5 or SHA-256).
    """
    hasher = hashlib.new(hash_type)
    hasher.update(text.encode())
    return hasher.hexdigest()

def compare_text_entries():
    """
    Compare the MD5 and SHA-256 hashes of two text entries.
    """
    text1 = text_entry1.get()
    text2 = text_entry2.get()

    if not text1 or not text2:
        result_label.config(text="Please enter Hashes to compare.")
        return

    text1_md5 = generate_hash(text1, 'md5')
    text1_sha256 = generate_hash(text1, 'sha256')
    text2_md5 = generate_hash(text2, 'md5')
    text2_sha256 = generate_hash(text2, 'sha256')

    if text1_md5 == text2_md5 and text1_sha256 == text2_sha256:
        result_label.config(text="The Hashes are the same.")
    else:
        result_label.config(text="The Hashes are different.")

# Create the main window
window = tk.Tk()
window.title("Text Hash Comparator")

# Create the text entry labels and entry fields
text_label1 = tk.Label(window, text="Hash 1:")
text_label1.grid(row=0, column=0)
text_entry1 = tk.Entry(window, width=50)
text_entry1.grid(row=0, column=1)

text_label2 = tk.Label(window, text="Hash 2:")
text_label2.grid(row=1, column=0)
text_entry2 = tk.Entry(window, width=50)
text_entry2.grid(row=1, column=1)

# Create the compare button
compare_button = tk.Button(window, text="Compare Hashes", command=compare_text_entries)
compare_button.grid(row=2, column=1)

# Create the result label
result_label = tk.Label(window, text="")
result_label.grid(row=3, column=1)

# Start the Tkinter event loop
window.mainloop()