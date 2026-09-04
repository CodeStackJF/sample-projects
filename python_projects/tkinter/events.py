from tkinter import messagebox

def on_click_event():
    """
    Handle click events.

    Args:
        event: The event object containing information about the click event.
    """
    # Process the click event
    print("Click event detected.")
    messagebox.showinfo("Click event detected.", "You clicked the button!")
    # Additional logic for handling the click can be added here