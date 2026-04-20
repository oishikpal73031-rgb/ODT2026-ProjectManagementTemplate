import machine
import time

# =========================
# USER INPUT
# =========================
print("\n📐 ENTER RECTANGLE SIZE")

X_LEN = float(input("Enter length (X in inches): "))
Y_LEN = float(input("Enter height (Y in inches): "))

# =========================
# CALIBRATION
# =========================
SPI = 414  # steps per inch

# =========================
# POSITION TRACKING
# =========================
cur_x = 0.0
cur_y = 0.0

# =========================
# STEP SEQUENCE
# =========================
seq = [
    [1,0,0,1],
    [1,1,0,0],
    [0,1,1,0],
    [0,0,1,1]
]

# =========================
# MOTORS
# =========================
x1 = [machine.Pin(p, machine.Pin.OUT) for p in [13,12,14,27]]

y1 = [machine.Pin(p, machine.Pin.OUT) for p in [26,25,33,32]]
y2 = [machine.Pin(p, machine.Pin.OUT) for p in [2,4,5,18]]
y3 = [machine.Pin(p, machine.Pin.OUT) for p in [19,21,22,23]]

# =========================
# STEP FUNCTIONS
# =========================
def step_motor(motor, pattern):
    for i in range(4):
        motor[i].value(pattern[i])

def step_y(idx):
    s_f = seq[idx]
    s_r = seq[3 - idx]

    for i in range(4):
        y1[i].value(s_r[i])

    for i in range(4):
        val = s_f[i]
        y2[i].value(val)
        y3[i].value(val)

# =========================
# LINE MOVE (COORDINATED)
# =========================
def move_line(x_target, y_target):
    global cur_x, cur_y

    dx = x_target - cur_x
    dy = y_target - cur_y

    x_steps = int(dx * SPI)
    y_steps = int(dy * SPI)

    x_dir = 1 if x_steps > 0 else -1
    y_dir = 1 if y_steps > 0 else -1

    x_steps = abs(x_steps)
    y_steps = abs(y_steps)

    max_steps = max(x_steps, y_steps)

    for i in range(max_steps):

        idx = i % 4

        # X axis
        if i < x_steps:
            if x_dir == 1:
                step_motor(x1, seq[idx])
            else:
                step_motor(x1, seq[3 - idx])

        # Y axis
        if i < y_steps:
            if y_dir == 1:
                step_y(idx)
            else:
                step_y(3 - idx)

        time.sleep_ms(3)

    cur_x = x_target
    cur_y = y_target

    print("📍", cur_x, cur_y)

# =========================
# DRAW RECTANGLE
# =========================
def draw_rectangle():

    print("\n🖊 Drawing rectangle...")

    p1 = (0, 0)
    p2 = (X_LEN, 0)
    p3 = (X_LEN, Y_LEN)
    p4 = (0, Y_LEN)

    move_line(*p1)
    move_line(*p2)
    move_line(*p3)
    move_line(*p4)
    move_line(*p1)

    print("✅ Rectangle complete")

# =========================
# RUN
# =========================

print("\n⚠️ Place machine manually at (0,0)")

draw_rectangle()