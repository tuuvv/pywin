from pywinauto.application import Application
from pywinauto.timings import TimeoutError

# Khởi động Notepad
app = Application().start("notepad.exe")

# Lấy cửa sổ chính của Notepad
main_window = app.window(title="Untitled - Notepad")

try:
    # Đợi cho cửa sổ xuất hiện với tiêu đề và tên lớp đúng
    windowOpen = app.window(title_re='Some Form', class_name='Some:form').wait('visible', timeout=20, retry_interval=1)
    
    # Đặt focus vào cửa sổ và gõ chữ "hello"
    windowOpen.set_focus()
    windowOpen.type_keys("hello")
    
except TimeoutError as e:
    print(f"Error: Window not found within the timeout period. {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Optional: Save file and close Notepad (uncomment if needed)
# main_window.menu_select("File->Save")
# main_window.SaveAs.edit.set_text("hello.txt")
# main_window.SaveAs.Save.click()
# main_window.close()
