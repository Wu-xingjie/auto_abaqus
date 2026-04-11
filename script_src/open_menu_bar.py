from pywinauto import Application
import pyautogui
import os, time
from pywinauto.keyboard import send_keys
def runScript(script_path:str):
    # 打开abaqus
    print("[INFO] 尝试连接已打开的abaqus...")
    app = Application(backend="win32").connect(title_re=".*Abaqus/CAE.*")
    print("[INFO] abaqus连接成功")
    # 获取abaqus主窗口
    main_window = app.window(title_re=".*Abaqus/CAE.*")
    # 打开脚本导入对话框
    main_window.set_focus()
    send_keys("^%s")
    print("[INFO] 导入脚本对话框打开成功")
    dialog = app.window(title_re=".*Run Script.*|.*运行脚本.*")
    dialog.wait('visible', timeout=10)
    print(f"对话框标题: {dialog.window_text()}")
    # 输入脚本路径
    fn_png = os.path.join(os.path.abspath(os.curdir), r"..\pic\file_name.png")
    loc_file_name = pyautogui.locateOnScreen(fn_png, grayscale=True,confidence = 0.7)
    time.sleep(1)
    pyautogui.moveTo(loc_file_name)
    pyautogui.move((100,0))
    pyautogui.click()
    pyautogui.write(script_path)
    # 点击ok
    ok_png = os.path.join(os.path.abspath(os.curdir), r"..\pic\ok.png")
    loc_ok = pyautogui.locateOnScreen(ok_png, grayscale=True, confidence = 0.7)
    pyautogui.moveTo(loc_ok)
    pyautogui.doubleClick()

if __name__ == "__main__":
    runScript(r"D:\github_project\auto_abaqus\script_src\part\create_cube.py")