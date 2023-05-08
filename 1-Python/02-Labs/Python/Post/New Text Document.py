import time
import pyautogui as gui

# Open Chrome
gui.press("win")
time.sleep(1)
gui.typewrite("chrome")
time.sleep(1)
gui.press('Enter')
time.sleep(1)
gui.typewrite("www.facebook.com")
time.sleep(1)
gui.press('Enter')
time.sleep(1)

# Click on What's on your mind.png 
location = gui.locateOnScreen("Whats_on_your_mind.png")
center = gui.center(location)
gui.click(center)
time.sleep(1)
# Click on "Public" button
try:
    location = gui.locateOnScreen("public.png")
    center = gui.center(location)
    gui.click(center)
except TypeError:
    print("Image not found on screen")


# Type "Only me"
gui.typewrite("Only me")
time.sleep(1)

# Click on "Only me" option
location = gui.locateOnScreen("Only_Me.png")
center = gui.center(location)
gui.click(center)

# Click on "Done" button
location = gui.locateOnScreen("Done_after_only_me.png")
center = gui.center(location)
gui.click(center)

# Click on the "Write something here" field
location = gui.locateOnScreen("Whats_on_your_mind_writing.png")
center = gui.center(location)
gui.click(center)

# Type the post content
gui.typewrite("Testing")

# Click on "Post" button
location = gui.locateOnScreen("Post.png")
center = gui.center(location)
gui.click(center)
