def on_button_pressed_a():
    kitronik_servo_lite.turn_right(90)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_sound_loud():
    kitronik_servo_lite.drive_forwards(100)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

basic.show_string("Hello class 12 my name is zepo with my frains timothy")