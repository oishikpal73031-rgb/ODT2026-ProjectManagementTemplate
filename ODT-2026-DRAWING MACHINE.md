# 1. Team Identity

## 1.1 Studio / Group Name
`Drawing Machine`

## 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| Oishik Pal | Electronics + System Design | Fabrication | System thinking, motion logic, integration |
| Danish | Mechanical + Fabrication | Electronics | Structural execution, assembly, iteration |

## 1.3 Project Title
`Kinetic Sand Plotter`

## 1.4 One-Line Pitch
`A CNC-inspired kinetic machine that transforms precise motor control into slow, continuous patterns drawn in sand.`

## 1.5 Expanded Project Idea

**Response:**  
This project is a DIY ESP32-based CNC sand plotter that combines the motion logic of 2D CNC systems and 3D printers with the visual output of a kinetic sand table. A drawing head moves across a sand surface to generate continuous geometric and flowing patterns through synchronized stepper motor motion.  

The system uses 28BYJ-48 stepper motors with ULN2003 drivers, driving a rack and pinion mechanism mounted on drawer sliders for smooth linear motion. The machine operates purely in 2D space, relying entirely on coordinated X and Y motion to create patterns. The focus is on translating digital precision into physical, organic output, resulting in a visually calming and continuously evolving sand pattern system.

---

# 2. Philosophy Fit

## 2.2 What kind of experience are you creating?

**Response:**  
The project creates a meditative kinetic visual experience where users observe patterns being slowly generated in sand. Interaction is minimal but intentional, allowing users to trigger pattern generation while primarily engaging through observation.  

The experience evokes calmness, curiosity, and anticipation. The continuous motion and evolving output encourage repeated interaction.

## 2.3 Design Persona

**Response:**  
We are designing this as a small creative studio making an interactive kinetic installation for exhibition visitors and classmates.

---

# 3. Inspiration

## 3.1 References

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| Kinetic Object | Sisyphus Sand Table | Sand pattern visuals |
| Machine | CNC Plotters / 3D Printers | Axis control |
| Mechanism | Rack and Pinion | Precise motion |

## 3.2 Original Twist

**Response:**  
Uses rack and pinion instead of belts and multiple motors on one axis, requiring tight synchronization while keeping mechanics visible.

---

# 4. Project Intent

## 4.1 Core Interaction Loop

**Response:**  
Press button → trigger pattern → synchronized motion → pattern forms → complete → reset

## 4.2 Intended Player / Audience

| Question | Response |
|---|---|
| Who is this for? | Exhibition viewers |
| Age range | 15+ |
| Solo or multiplayer | Solo |
| Expected duration of one round | 30s–2min |
| What should the player feel? | Calm, curiosity |
| Is explanation required before use? | Minimal |

## 4.3 Player Journey

1. **Approach:** Sees moving sand  
2. **Start:** Press button  
3. **First Action:** Pattern begins  
4. **Main Interaction:** Continuous motion  
5. **System Response:** Pattern forms  
6. **Win / Lose / End Condition:** Pattern completes  
7. **Reset:** Ready again  

## 4.4 Rules of Play

- Press button to start  
- Do not obstruct movement  
- Wait for completion  
- Observe  

---

# 5. Definition of Success

## 5.1 Definition of “Playable”

- [ ] Smooth motion  
- [ ] Clear patterns  
- [ ] Motor sync  
- [ ] No binding  
- [ ] Repeatability  

## 5.2 Minimum Viable Version

**Response:**  
2-axis system drawing basic patterns

## 5.3 Stretch Features

- More patterns  
- Speed control  
- Complex curves  

---

# 6. System Overview

## 6.1 Project Type

- [x] Electronics-based  
- [x] Mechanical  
- [ ] Sensor-based  
- [ ] App-connected  
- [x] Motorized  
- [ ] Sound-based  
- [ ] Light-based  
- [ ] Screen/UI-based  
- [x] Fabricated structure  
- [x] Game logic based  
- [x] Installation / tabletop experience  
- [ ] Other: Not applicable  

## 6.2 High-Level System Description

**Response:**  

The system operates as a coordinated electromechanical setup that converts a simple user input into controlled motion across a sand surface.  

- **Input:**  
A push button is used to trigger the system. When pressed, it initiates a predefined motion pattern.  

- **Processing:**  
The ESP32 microcontroller receives the input and executes programmed motion logic. It calculates step sequences and timing for each motor, ensuring that all motors, especially those on the same axis, move in synchronization.  

- **Output:**  
Four stepper motors, controlled via ULN2003 drivers, generate precise rotational movement. This motion is translated into linear travel using a rack and pinion mechanism, allowing controlled movement along X and Y axes.  

- **Physical Structure:**  
The motors are mounted on a rigid plywood and MDF frame. Drawer sliders guide the motion smoothly along both axes, while the gantry structure holds alignment. The rack and pinion system converts motor rotation into linear displacement, enabling the drawing head to move across the sand surface and form patterns.  

- **App Interaction:**  
No app is used in this system. All operations are handled directly through hardware input and onboard processing.  

Overall, the system transforms a single button input into synchronized multi-axis motion, producing continuous and repeatable patterns in sand through precise mechanical control.

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| Button | Input | Trigger |
| ESP32 | Processing | Logic |
| Stepper Motors | Output | Movement |
| Mechanical System | Physical Action | Executes motion |

---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch

**Insert image below:**  
<img src="images/CONCEPT SKETCH.jpeg" width="400">


## 7.2 Labeled Build Sketch

**Insert image below:**  
`Info yet to be given`

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | 20 inches |
| Width | 20 inches |
| Height | 8.5 cm |
| Estimated weight | 10kg |

---

# 8. Mechanical Planning

## 8.1 Mechanical Features

- [x] Gears  
- [x] Rack and pinion  
- [x] Sliders  
- [x] Shafts  

## 8.2 Mechanical Description

**Response:**  
Drawer sliders provide guided linear motion. Stepper motors drive pinion gears engaging racks, converting rotational motion into linear displacement. A rigid gantry maintains alignment.

## 8.3 Motion Planning

**Response:**  

- **What moves:**  
The gantry assembly carrying the drawing head moves across the sand surface along two axes. The X-axis moves horizontally, while the Y-axis is driven by three synchronized motors to move the structure vertically.  

- **What causes the movement:**  
Movement is generated by four 28BYJ-48 stepper motors. These motors rotate pinion gears, which engage with fixed racks to convert rotational motion into linear displacement. The motors are controlled by the ESP32 through ULN2003 drivers using timed step sequences.  

- **How far it moves:**  
The movement range is defined by the physical dimensions of the structure, approximately 15 inches along both X and Y axes. Motion is executed in discrete steps, calculated using a calibrated steps-per-inch value based on the pinion gear circumference, enabling precise positioning across the full travel range.  

- **How fast it moves:**  
Speed is controlled through step delay timing, typically operating in the range of 2–3 milliseconds per step. Acceleration and deceleration are managed using a trapezoidal motion profile to ensure smooth starts and stops, preventing mechanical stress and motor slip.  

- **What could go wrong:**  
- Motor desynchronization, especially on the multi-motor Y-axis, can cause skewed movement  
- Mechanical misalignment can lead to binding or uneven motion  
- Insufficient torque or excessive load may cause motors to stall  
- Gear backlash or poor rack engagement can reduce accuracy  
- Unstable power supply or wiring issues can lead to missed steps or inconsistent behavior  

## 8.4 Simulation / CAD / Animation Before Making

| Tool Used | File / Link | What Was Tested |
|---|---|---|
| Tinkercad / Basic CAD Modeling | [Info not given] | Overall structure layout including base frame, sand container, and gantry placement |
| Tinkercad / CAD | [Info not given] | Alignment of X and Y axes using drawer sliders and positioning of rack and pinion system |
| Tinkercad / CAD | [Info not given] | Clearance between moving gantry and frame to ensure no collision during motion |

## 8.5 Changes After Digital Testing

**Response:**  
Not applicable  

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
|---|---:|---|
| ESP32 | 1 | Main controller |
| Breadboard | 1 | Power distribution |
| 28BYJ-48 Stepper Motors | 4 | Axis movement |
| ULN2003 Drivers | 4 | Motor driving |
| LM2596 Buck Converter | 1 | Voltage regulation |
| 12V Adapter | 1 | Power supply |
| Wires (single + multicore) | — | Connections |
| Female Jack | 1 | Power input |

## 9.2 Wiring Plan

**Response:**  
A 12V adapter supplies power to an LM2596 buck converter, stepped down to 5V. This is distributed via a breadboard to all stepper drivers.  

The ESP32 is powered via USB and shares a common ground with the external supply.  

**Pin Mapping:**  
- X Axis: GPIO 13, 14, 27, 26  
- Y1: GPIO 26, 25, 33, 32  
- Y2: GPIO 2, 4, 5, 18  
- Y3: GPIO 19, 21, 22, 23  

All motors receive power from the regulated supply and share common ground.  

**Note:** GPIO 26 conflict exists between X and Y1 and must be corrected.

## 9.3 Circuit Diagram

**Insert image below:**  
<img src="images/CIRCUIT DIAGRAMm.jpg" width="400">


## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | 12V DC adapter (stepped down via LM2596) + ESP32 via USB |
| Voltage required | 5V regulated supply for motors and drivers |
| Current concerns | Multiple stepper motors running simultaneously can draw high current, risking voltage drops and unstable performance if supply is insufficient |
| Safety concerns | Ensure common ground between ESP32 and motor supply, avoid overloading the buck converter, secure connections to prevent short circuits, and maintain stable voltage output to prevent damage to components |

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| Thonny IDE | Writing and uploading MicroPython code to ESP32 |
| MicroPython | Executes motion control logic on ESP32 |

## 10.2 Software Logic

**Response:**  

The software controls coordinated motion of four stepper motors (1 for X-axis and 3 for Y-axis) to draw geometric shapes in sand based on user-defined dimensions.  

- **Startup Behavior:**  
On execution, the program prompts the user to input rectangle dimensions (X and Y in inches). GPIO pins for all motors are initialized as outputs, and initial position is set to (0,0).  

- **Input Handling:**  
User inputs the rectangle size via serial input (Thonny console). No physical button is used in this version.  

- **Sensor Reading:**  
No real-time sensor feedback is used in this code. Motion is open-loop and based on predefined calibration (steps per inch).  

- **Decision Logic:**  
The system converts input dimensions into step counts using a calibration factor (414 steps per inch).  
It calculates:  
- Distance to move (dx, dy)  
- Direction (positive or negative)  
- Total steps required per axis  

A coordinated stepping algorithm ensures both axes move proportionally to form straight lines.  

- **Output Behavior:**  
The ESP32 sends step sequences to:  
- X-axis motor (single motor)  
- Y-axis motors (3 motors synchronized)  

Y-axis logic includes mirrored stepping for one motor to maintain mechanical symmetry.  

- **Communication Logic:**  
Serial communication is used only for user input and debugging output (printing coordinates).  

- **Reset Behavior:**  
After completing the rectangle, the system stops. It does not automatically return to origin unless commanded in code.  

## 10.3 Code Flowchart

**Insert image below:**  
`[Info yet to be given]`

**Actual Flow (based on your code):**  
- Start  
- Initialize pins and variables  
- Take user input (X, Y dimensions)  
- Set current position (0,0)  
- Call draw_rectangle()  
  - Move to (0,0)  
  - Move to (X,0)  
  - Move to (X,Y)  
  - Move to (0,Y)  
  - Move back to (0,0)  
- End  

## 10.4 Pseudocode

```text
START

PRINT "Enter rectangle size"
INPUT X_LEN, Y_LEN

SET steps_per_inch = 414

SET current position (cur_x, cur_y) = (0,0)

INITIALIZE step sequence array

INITIALIZE X motor pins
INITIALIZE Y motor pins (Y1, Y2, Y3)

FUNCTION step_motor(motor, pattern):
    APPLY pattern to motor pins

FUNCTION step_y(index):
    APPLY forward sequence to Y2 and Y3
    APPLY reverse sequence to Y1

FUNCTION move_line(x_target, y_target):

    CALCULATE dx, dy
    CONVERT dx, dy to steps

    DETERMINE direction for X and Y

    FOR each step up to max(x_steps, y_steps):

        IF X step required:
            MOVE X motor (forward or reverse)

        IF Y step required:
            MOVE all Y motors (synchronized)

        WAIT small delay

    UPDATE current position

FUNCTION draw_rectangle():

    DEFINE 4 corners:
        (0,0), (X,0), (X,Y), (0,Y)

    MOVE to each point sequentially
    RETURN to origin

PRINT "Place machine at origin"

CALL draw_rectangle()

END
```
# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?

- [ ] Yes  
- [x] No  

## 11.2 Why is the app needed?

**Response:**  
Not applicable (No app integration in this project)

## 11.3 App Features

| Feature | Purpose |
|---|---|
| Not applicable | Not applicable |

## 11.4 UI Mockup

**Insert image below:**  
`Not applicable`

## 11.5 App Screen Flow

1. Not applicable  
2. Not applicable  
3. Not applicable  
4. Not applicable  

---

# 12. Bill of Materials

## 12.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost (INR) | Material / Spec | Why This Choice? |
|---|---:|---|---|---:|---|---|
| ESP32 | 1 | Yes | No | 0 (≈500) | MCU | Control |
| Breadboard | 1 | Yes | No | 0 (≈150) | Standard | Distribution |
| Stepper Motors | 4 | Yes | No | 0 (≈150 each) | 5V | Motion |
| Drivers | 4 | Yes | No | 0 (≈80 each) | ULN2003 | Control |
| Wires | — | Yes | No | 0 (≈200) | — | Connections |
| Plywood | 1 | Yes | No | 0 (≈400) | Wood | Structure |
| Screws | ~30 | Yes | No | 0 (≈100) | Steel | Assembly |
| LM2596 | 1 | No | Yes | 50 | Regulator | Power |
| Drawer Sliders | 3 | No | Yes | 450 | Metal | Motion |
| Rack | 6 | No | Yes | 270 | Gear | Linear motion |
| Pinion | 4 | No | Yes | 140 | Gear | Drive |

## 12.2 Material Justification

**Response:**  

The selection of materials and components is based on precision, ease of fabrication, and system reliability:  

- **Plywood (instead of acrylic or cardboard):**  
Plywood provides sufficient rigidity to support the gantry and maintain alignment under load. Acrylic, while cleaner visually, is brittle and prone to cracking under stress. Cardboard lacks structural integrity for moving mechanical systems.  

- **Rack and Pinion (instead of belt drive):**  
Rack and pinion ensures direct motion transfer with minimal slack. Belt systems introduce elasticity and backlash, which reduces positional accuracy, especially critical in pattern drawing.  

- **Drawer Sliders (instead of free rail or custom guides):**  
Drawer sliders provide pre-aligned, low-friction linear motion without the need for precision machining. They reduce complexity and ensure consistent motion.  

- **28BYJ-48 Stepper Motors (instead of DC motors):**  
Stepper motors allow precise position control without feedback systems. DC motors would require encoders and complex control loops, increasing system complexity.  

- **ULN2003 Drivers:**  
These are compatible with the selected stepper motors and simplify interfacing with the ESP32.  

- **LM2596 Buck Converter:**  
Ensures stable voltage regulation from a higher voltage input. Direct supply without regulation could lead to inconsistent motor performance or damage.  

- **Breadboard and Wires:**  
Used for rapid prototyping and easy modification during testing phases.  

- **Metal Gears (Rack and Pinion):**  
Provide durability and consistent engagement compared to plastic alternatives, reducing wear and maintaining accuracy over time.  

Overall, the material selection prioritizes mechanical stability, repeatability, and ease of integration over aesthetics or compactness.

## 12.3 Items to Purchase Separately

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| LM2596 Buck Regulator | To step down 12V input to stable 5V for motors and drivers | Info not given | Info not given | Received |
| Drawer Sliders (3 pcs) | Provide smooth and stable linear motion for X and Y axes | Info not given | Info not given | Received |
| Rack (6 pcs) | Converts rotational motion of motors into linear movement | Info not given | Info not given | Received |
| Pinion Gears (4 pcs) | Engages with rack to drive axis motion | Info not given | Info not given | Received |

## 12.4 Budget Summary

| Budget Item | Estimated Cost (INR) |
|---|---:|
| Electronics (ESP32, motors, drivers, wires, breadboard) | ₹1,800 |
| Mechanical parts (rack, pinion, sliders) | ₹860 |
| Fabrication materials (plywood, screws) | ₹500 |
| Purchased extras (buck regulator, additional components) | ₹50 |
| Contingency (unexpected replacements / failures) | ₹300 |
| **Total Estimated Cost** | ₹3,510 |

The project cost is controlled due to key components being already available. Most spending was on mechanical parts like sliders and rack and pinion, which are essential for precision.  

If needed, cost can be reduced by:  

- Using simpler linear guides instead of drawer sliders  
- Switching to lower-cost wood materials  
- Reducing motor count with alternative mechanical linkage  

However, these changes may reduce motion smoothness and reliability, so the current setup prioritizes performance over minimal cost.

## 12.5 Budget Reflection

**Response:**  

The current cost is justified and appropriate for the system being built. Most expenses directly contribute to motion accuracy, structural stability, and reliable performance, which are critical for this project.  

Any reduction in cost would involve compromising on key components such as drawer sliders or the rack and pinion system, which would negatively affect smoothness and precision. Therefore, the budget is considered efficient and necessary for achieving the intended outcome.

---

# 13. Planning the Work

## 13.1 Team Working Agreement

**Response:**  

Tasks were divided based on strengths but executed collaboratively. Oishik primarily handled electronics, coding, and documentation, while Danish focused more on mechanical fabrication and assembly. However, both members were involved in all major stages including design decisions, testing, and integration.  

Decisions were made through direct discussion and quick iteration. Instead of over-planning, ideas were tested physically and refined based on results. This allowed faster problem solving, especially during mechanical and synchronization issues.  

Progress was checked continuously through working prototypes rather than formal reviews. Each stage was validated by testing motion, alignment, and system behavior before moving forward.  

If a task was delayed or not working, both members shifted focus to resolve it together. The approach was flexible, prioritizing problem solving over rigid task ownership.  

Documentation was primarily maintained by Oishik, with inputs from Danish during key stages like fabrication changes and testing observations. This ensured the process was recorded alongside development without slowing down the build.

### 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|--------|------|-------|----------------|----------|------------|--------|
| T1 | Finalize concept and system approach | Oishik Pal & Danish | 2 | 30 March | None | Completed |
| T2 | Complete BOM and cost planning | Oishik Pal | 2 | 1 April | T1 | Completed |
| T3 | Mechanical design planning (gantry, sliders, rack layout) | Danish | 3 | 2 April | T1 | Completed |
| T4 | Procure additional components | Oishik Pal & Danish | 2 | 4 April | T2 | Completed |
| T5 | Electronics setup and initial testing | Oishik Pal | 3 | 6 April | T2 | Completed |
| T6 | Fabrication of base structure and assembly | Danish | 5 | 9 April | T3 | Completed |
| T7 | Motor mounting and mechanical alignment | Oishik Pal & Danish | 4 | 11 April | T6 | Completed |
| T8 | Wiring and power distribution setup | Danish | 3 | 12 April | T5 | Completed |
| T9 | Firmware development (motion control logic) | Oishik Pal | 5 | 14 April | T5 | Completed |
| T10 | Axis synchronization and motion calibration | Oishik Pal & Danish | 4 | 16 April | T9 | Completed |
| T11 | Full system integration | Oishik Pal & Danish | 4 | 17 April | T8, T10 | Completed |
| T12 | Testing and debugging | Oishik Pal & Danish | 4 | 18 April | T11 | Completed |
| T13 | Playtesting and refinement | Oishik Pal & Danish | 3 | 18 April | T12 | Completed |
| T14 | Documentation and README completion | Oishik Pal & Danish | 3 | 19 April | T13 | Completed |

## 13.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| Concept and gameplay | Oishik Pal & Danish | Shared |
| Electronics | Danish | Shared |
| Coding (motion logic, synchronization) | Oishik Pal | Danish |
| Mechanical design (gantry, rack, sliders) | Danish | Oishik Pal |
| Fabrication and assembly | Danish | Oishik Pal |
| Wiring and power system | Danish | Shared |
| System integration | Oishik Pal & Danish | Shared |
| Testing and debugging | Oishik Pal & Danish | Shared |
| Playtesting and refinement | Oishik Pal & Danish | Shared |
| Documentation (README, logs) | Oishik Pal | Danish |

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [ ] Idea finalized  
- [ ] Core interaction decided  
- [ ] Sketches made  
- [ ] BOM completed  
- [ ] Purchase needs identified  
- [ ] Key uncertainty identified  
- [ ] Basic feasibility tested  

### Week 2 — Build Subsystems
Expected outcomes:
- [ ] Electronics tests completed  
- [ ] Structure and motion planning completed  
- [ ] Mechanical concept tested (rack and pinion + sliders)  
- [ ] Power system tested (buck converter setup)  
- [ ] Individual subsystems partially working  

### Week 3 — Integrate
Expected outcomes:
- [ ] Physical structure built  
- [ ] Motors mounted and aligned  
- [ ] Electronics integrated  
- [ ] Code connected to hardware  
- [ ] First working motion across X and Y axes  
- [ ] Basic pattern drawing achieved  

### Week 4 — Refine and Finish
Expected outcomes:
- [ ] Motion smoothness improved  
- [ ] Synchronization issues reduced  
- [ ] Playtesting completed  
- [ ] Mechanical adjustments made  
- [ ] Documentation completed  
- [ ] Final working build ready  

## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | Finalize idea, plan system, complete BOM | Concept finalized, CNC + sand plotter direction confirmed, BOM created, core risks (motor sync, alignment) identified | Reduced complexity by avoiding belts and choosing rack and pinion | Begin sourcing parts and testing basic motor control |
| Week 2 | Build and test subsystems | Electronics tested with ESP32 and stepper motors, power system with LM2596 configured, initial mechanical trials with sliders and rack | Identified need for rigid alignment and stable power, adjusted mounting approach | Complete structure and prepare for full assembly |
| Week 3 | Integrate full system | Structure fabricated, motors mounted, wiring completed, initial code tested for axis movement, first patterns attempted | Faced synchronization issues in multi-motor Y-axis, required code adjustments and calibration | Refine motion logic and improve synchronization |
| Week 4 | Refine, test, finalize | Motion smoothed using delay tuning and better sequencing, servo integration completed, stable pattern generation achieved, documentation compiled | Minor mechanical tweaks for alignment and smoother travel | Final testing, documentation polish, and submission |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| Motor desynchronization (multi-motor axis) | Technical | High | High | Synchronize stepping logic in same execution cycle, reverse sequence for mirrored motors | Oishik Pal & Danish |
| Mechanical binding / misalignment | Mechanical | High | High | Rebuild frame alignment, adjust mounting, ensure parallel sliders | Danish |
| Stepper motors getting stuck / insufficient torque | Technical | Medium | High | Use half-step mode, optimize delay timing, reduce load on axis | Oishik Pal |
| Faulty or loose wiring connections | Electrical | High | Medium | Rewire connections, replace faulty wires, ensure proper grounding | Oishik Pal |
| Power instability / voltage drops | Electrical | Medium | High | Use LM2596 regulator, maintain stable 5V supply, common ground across system | Oishik Pal |
| Component fit issues (rack, pinion, sliders) | Mechanical | High | Medium | Iterative adjustment, repositioning, and redesign of mounts | Danish |
| Structural instability during motion | Mechanical | Medium | High | Reinforce base, improve rigidity of gantry | Danish |
| Repeated redesign causing time delays | Time | High | Medium | Prioritize working version first, then refine incrementally | Oishik Pal & Danish |
| Inconsistent pattern output | Gameplay / Output | Medium | Medium | Calibrate steps per unit, refine motion logic | Oishik Pal |

## 15.2 Biggest Unknown Right Now

**Response:**  
The biggest uncertainty was maintaining precise synchronization between multiple stepper motors on a single axis while ensuring the mechanical structure remained perfectly aligned. Even small timing mismatches or physical misalignments led to skewed motion, forcing repeated adjustments in both code and structure.

## 16. Testing and Playtesting

### 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|-------------------|---------------------|------------------|
| X-axis movement (independent) | Run X motor sequence alone across full range | Smooth linear motion without stalling or jerks |
| Y-axis movement (independent, all motors) | Run all Y motors together and observe alignment | All motors move in sync with no skew or lag |
| X and Y axes together (diagonal motion) | Execute coordinated movement using interpolation logic | Straight diagonal path without deviation |
| Horizontal movement (X under load) | Move gantry left to right repeatedly | No binding, consistent speed across travel |
| Vertical movement (Y under load) | Move gantry front to back repeatedly | No misalignment between Y motors |
| All motors running simultaneously | Trigger full pattern execution | Stable motion with no missed steps or jitter |
| Stepper synchronization (multi-motor axis) | Observe Y-axis motors during motion | No visible desync or twisting of structure |
| Power stability under load | Run all motors continuously for extended duration | No resets, no voltage drops, consistent performance |
| Wiring reliability | Physically inspect and stress test connections | No loose connections or intermittent faults |
| Mechanical alignment | Run repeated motion cycles and observe rails | No friction points, smooth travel across full range |
| Pattern accuracy | Execute predefined pattern sequence | Patterns form correctly and consistently |
| Long duration operation | Run continuous patterns for extended time | System remains stable without overheating or failure |

---

### 16.2 Playtesting Plan

| Question | How You Will Check |
|----------|-------------------|
| Do players understand what to do? | Observe first-time users interacting without any instructions |
| Is the interaction satisfying? | Collect verbal feedback after one full pattern cycle |
| Do players want another turn? | Observe if users trigger another pattern voluntarily |
| Is the challenge balanced? | Not applicable (no competitive or difficulty-based gameplay) |
| Is the response clear and immediate? | Check if button input results in immediate and predictable motion |

---

### 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|------|-------------|------|----------------|--------|-------------|
| 19 April | Y-axis motors not moving in sync, causing skew | Technical | Adjusted stepping sequence and ensured simultaneous signal updates in code | Partly | Further refine timing and reverse sequence for mirrored motors |
| 19 April | Gantry getting stuck and not moving smoothly | Mechanical | Re-aligned sliders and repositioned rack and pinion setup | Worked | Reinforce structure and recheck alignment under load |
| 19 April | Motors stalling under load | Technical | Reduced speed by increasing step delay and tested half-step sequence | Partly | Optimize torque vs speed balance and reduce friction |
| 19 April | Loose / faulty wiring causing inconsistent behavior | Electrical | Rewired connections and replaced weak wires | Worked | Secure all connections properly and avoid loose contacts |
| 19 April | System not moving linearly, jerky motion | Mechanical | Rebuilt structure orientation and adjusted slider placement | Worked | Fine-tune alignment and ensure parallel rails |

---

### 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|--------|--------------|--------------------|-------------------|---------------------|
| Classmate | Pressed button and observed full pattern cycle | Initial purpose not immediately clear without context | Watching patterns slowly form in sand | Add minimal visual cue or label for interaction |
| Peer | Triggered multiple cycles and observed motion closely | Expected more control or variation in input | Smooth mechanical motion and precision | Introduce multiple pattern options in future |
| Friend | Observed without interacting initially, then tried input | Unsure if system was responsive at first | Calm, repetitive motion and visual output | Improve immediate response feedback after input |
| Classmate | Interacted once and watched entire cycle | No confusion in usage but limited interaction depth | Clean patterns and synchronized movement | Add variation in speed or pattern complexity |

---

## 17. Build Documentation

### 17.1 Fabrication Process

The fabrication process began with constructing the base structure using plywood. A 20 × 20 inch frame was cut and assembled to form the primary enclosure. A secondary top frame was then built to support the gantry and ensure structural stability.

Drawer sliders were mounted along the sides of the frame to enable smooth linear motion. These were carefully aligned and fixed using screws to maintain parallel movement across the axes.

The rack and pinion system was fabricated using a plywood cutting machine, ensuring consistent tooth profiles for reliable motion transfer. The racks were mounted along the slider paths, while pinion gears were attached to the motor shafts. Components were secured using a combination of adhesive and mechanical fastening methods such as nails and screws.

Motor mounts were created using MDF to provide a rigid and precise housing for the stepper motors. These mounts were fixed onto the structure, and the X-axis assembly was installed first. The Y-axis system, consisting of multiple motors, was then integrated following the same process.

A significant part of the fabrication involved iterative refinement. The system underwent approximately 8–9 revisions, focusing on improving alignment, reducing mechanical resistance, and ensuring synchronized movement. Adjustments included repositioning components, reinforcing joints, and recalibrating the structure to eliminate binding and achieve smooth, repeatable motion.

The final build reflects a balance between structural rigidity and precise mechanical alignment, which is critical for consistent pattern generation.

---

### 17.2 Build Photos

---

### 17.3 Version History

| Version | Date | What Changed | Why |
|--------|------|--------------|-----|
| v1 | [29th May 2026] | Initial structure built with drawer sliders mounted vertically along the length; motors installed with rack and pinion setup | Intended to achieve linear motion using vertical slider alignment |
| v2 | [10th May 2026] | System disassembled and rebuilt after motion failure; sliders repositioned and reoriented | Motors were getting stuck, movement was not smooth, and system failed to translate motion effectively |
| v3 | [19th April 2026] | Sliders mounted flat (horizontal orientation) with components rebuilt on top; improved alignment of racks, pinions, and motor mounts | Achieved smooth and continuous motion, resolved binding issues, and enabled proper system functionality |

---

## 18. Final Outcome

### 18.1 Final Description

**Response:**

The final system is a fully functional ESP32-based CNC sand plotter capable of generating continuous patterns through synchronized multi-axis motion. The machine uses four stepper motors driving a rack and pinion mechanism mounted on drawer sliders to achieve controlled linear movement across a sand surface.

The structure is built using a plywood frame with MDF motor mounts, ensuring rigidity and alignment. Motion across the X and Y axes is achieved through precise stepper control, with special attention given to synchronizing multiple motors on the Y-axis to prevent skew.

A key addition in the final version is the integration of two limit switches on the axes. These switches are used to detect the extreme ends of motion and establish a reliable origin (home) position. When the gantry reaches either end and triggers the switches, the system can recalibrate its position reference, improving repeatability and consistency of pattern generation.

The final build reflects multiple iterations of mechanical and electronic refinement, resulting in smooth motion, stable operation, and visually consistent sand patterns driven by calibrated motor control.

---

### 18.2 What Works Well

- Smooth and synchronized motion across X and Y axes, especially after calibration  
- Reliable pattern generation with consistent and repeatable output  
- Stable mechanical structure with reduced binding after multiple iterations  

---

### 18.3 What Still Needs Improvement

- Further refinement in multi-motor synchronization to eliminate minor skew  
- Reduction of mechanical friction for even smoother motion over long runs  
- More variation and complexity in generated patterns to enhance engagement  

---

### 18.4 What Changed From the Original Plan

**Response:**

The initial idea was to build a simple CNC-style sand plotter with basic axis movement and pattern generation. During development, the project evolved significantly due to practical challenges and iterative improvements.

Mechanically, the structure was redesigned multiple times. The original slider orientation did not allow smooth motion, causing the system to stall and bind. This led to a complete rebuild with a different slider configuration, improving stability and movement.

Electronically and in control logic, additional focus was placed on synchronizing multiple motors on the Y-axis, which was not fully anticipated in the initial plan. This required refinements in stepping sequences and timing to ensure coordinated motion.

A major addition was the implementation of limit switches, which were not part of the original concept. These were introduced to establish a reliable origin point and improve positional consistency.

Overall, the project shifted from a straightforward implementation to a more refined system emphasizing alignment, synchronization, and repeatability, driven by real-world testing and iteration.

---

## 19. Reflection

### 19.1 Team Reflection

**Response:**

The team worked effectively in terms of collaboration and adaptability. Both members were involved across all stages, which helped in faster problem solving and better understanding of the system as a whole. The balance between electronics, coding, and mechanical work was handled well, with each member leaning into their strengths while still contributing to other areas.

Progress was slowed mainly by mechanical and alignment issues. Multiple rebuilds, component fitting problems, and motor synchronization challenges took significant time. Frequent debugging of wiring and motor behavior also added delays.

Time and task management were handled flexibly rather than rigidly. While this allowed quick iteration and problem solving, it also meant that some stages took longer than expected due to repeated revisions. Overall, responsibilities were shared well, and the team adapted effectively to challenges.

---

### 19.2 Technical Reflection

**Response:**

- **Electronics:**  
Gained practical understanding of power distribution, voltage regulation using a buck converter, and the importance of common grounding. Also learned how wiring quality directly affects system reliability.  

- **Coding:**  
Learned how to control multiple stepper motors simultaneously, implement synchronized stepping sequences, and manage timing for smooth motion. Understood the importance of handling mirrored motor logic and precise execution cycles.  

- **Mechanisms:**  
Developed a strong understanding of how rack and pinion systems convert rotational motion into linear movement. Learned that alignment and rigidity are critical for proper motion and that small errors can cause major issues.  

- **Fabrication:**  
Improved skills in working with plywood and MDF, assembling structures, and iterating physical designs. Learned that real-world fabrication often requires multiple revisions beyond initial planning.  

- **Integration:**  
Understood how electronics, code, and mechanical systems must work together as a single unit. Learned that even if individual parts work correctly, the overall system can fail without proper synchronization and alignment.  

---

### 19.3 Design Reflection

**Response:**

This project reinforced that designing for play does not require complexity, but clarity and intention. The interaction is minimal, yet the experience remains engaging because the outcome evolves over time. This highlighted the importance of designing for observation, not just interaction.

In terms of delight, the slow formation of patterns proved more impactful than fast or complex motion. The sense of anticipation and gradual visual payoff created a stronger emotional response than instant results.

For clarity, it became evident that a system should communicate its function visually. Users understood what to do simply by watching the machine, without needing instructions. This validated the idea that good physical design reduces the need for explanation.

The project emphasized physical interaction as passive engagement. Unlike typical interactive systems, this relies on watching rather than controlling. Designing for this required focusing on motion smoothness, consistency, and rhythm.

From a player understanding perspective, predictability combined with variation worked well. Users could understand the system quickly, yet still remain curious about different pattern outcomes.

Finally, iteration was critical. Many early assumptions about motion, structure, and output did not hold up during testing. Rebuilding the system multiple times led to better alignment, smoother motion, and a more refined experience. The final result is a direct outcome of continuous testing, failure, and refinement rather than initial planning alone.

---

### 19.4 If You Had One More Week

**Response:**

With an additional week, the focus would be on refinement rather than major changes.

- Motion precision and smoothness would be improved by further tuning step timing and synchronization, especially across the multi-motor Y-axis to eliminate minor inconsistencies.  
- Mechanical alignment would be fine-tuned to reduce friction and ensure perfectly parallel movement across the full range.  
- Pattern quality would be enhanced by developing more optimized motion paths and introducing smoother curves instead of primarily linear movements.  
- System reliability would be strengthened by securing wiring, improving mounting stability, and stress-testing for long-duration operation.  
- User experience would be refined by making pattern transitions cleaner and ensuring consistent starting positions using the limit switches.  
- Additionally, with more time, a simple UI/UX interface would be developed where users could create or draw their own patterns digitally and have them executed by the machine in sand.  

The goal would not be to add complexity, but to make the existing system more precise, stable, interactive, and visually satisfying.

# 20. Final Submission Checklist

Before submission, confirm that:
- [ ] Team details are complete
- [ ] Project description is complete
- [ ] Inspiration sources are included
- [ ] Player journey is written
- [ ] Sketches are added
- [ ] BOM is complete
- [ ] Purchase list is complete
- [ ] Budget summary is complete
- [ ] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [ ] Code flowchart is added
- [ ] Task breakdown is complete
- [ ] Weekly logs are updated
- [ ] Risk register is complete
- [ ] Testing log is updated
- [ ] Playtesting notes are included
- [ ] Build photos are included
- [ ] Final reflection is written

---

# 21. Suggested Repository Structure

```text
project-repo/
├── README.md
├── images/
│   ├── concept-sketch.jpg
│   ├── labeled-sketch.jpg
│   ├── circuit-diagram.jpg
│   ├── ui-mockup.jpg
│   ├── prototype-1.jpg
│   └── final-build.jpg
├── code/
│   ├── main.py
│   ├── test_code.py
│   └── notes.md
├── cad/
│   ├── models/
│   └── screenshots/
└── docs/
    ├── references.md
    └── extra-notes.md
```

---

# 22. Instructor Review

## 22.1 Proposal Approval
- [ ] Approved to proceed
- [ ] Approved with changes
- [ ] Rework required before proceeding

**Instructor comments:**  
`[Instructor fills this section]`

## 22.2 Midpoint Review
`[Instructor fills this section]`

## 22.3 Final Review Notes
`[Instructor fills this section]`

