import machine
import time

# =========================
# INPUTS
# =========================
print("\n📐 ZIGZAG SETTINGS")

LENGTH = float(input("Enter total length (X inches): "))
HEIGHT = float(input("Enter total height (Y inches): "))
ROWS = int(input("Enter number of altitudes (rows): "))

# =========================
# CALIBRATION
# =========================
SPI = 414

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
# CNC LINE MOVE
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

        if i < x_steps:
            if x_dir == 1:
                step_motor(x1, seq[idx])
            else:
                step_motor(x1, seq[3 - idx])

        if i < y_steps:
            if y_dir == 1:
                step_y(idx)
            else:
                step_y(3 - idx)

        time.sleep_ms(3)

    cur_x = x_target
    cur_y = y_target

# =========================
# ZIGZAG DRAW (CORRECT MATH)
# =========================
def draw_zigzag():

    print("\n🖊 Drawing zigzag fill...")

    if ROWS < 2:
        print("❌ Need at least 2 rows")
        return

    row_gap = HEIGHT / (ROWS - 1)

    direction = 1  # 1 = left→right, -1 = right→left

    for i in range(ROWS):

        y = i * row_gap

        if direction == 1:
            move_line(LENGTH, y)
        else:
            move_line(0, y)

        direction *= -1

    print("✅ Zigzag complete")

# =========================
# RUN
# =========================

print("\n⚠️ Place machine manually at (0,0)")

draw_zigzag()