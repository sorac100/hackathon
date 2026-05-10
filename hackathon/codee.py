"""
Space Health Tracker
Winnie Zhang,
Sora Chang,
Kexin Huang,
Tanisha Mazumbar
Hackathon 2026

"""
# ---------------- Setup ---------------- #
import pygame
import tkinter as tk
from tkinter import ttk
import random
"""
# image sources

https://img.freepik.com/free-vector/future-spaceship-crew-member-personal-cabin-minimalistic-interior-with-neon-ambient-light_33099-924.jpg?semt=ais_hybrid&w=740&q=80
https://stock.adobe.com/search?k=%22nurse+cartoon%22&asset_id=1953769405
https://www.vecteezy.com/vector-art/26581235-cartoon-task-planners-cute-paper-sticky-notes-banners-to-do-list-or-memo-message-notepads-paper-sheets-blank-schedule-bookmarks-colorful-notepaper-for-kids-school-or-office
https://www.youtube.com/watch?v=e8CRgkPxniI
https://www.magnific.com/premium-vector/mental-health-problems-girl-is-sad-depressed-mood-person-vector-illustration_139970799.htm
https://www.shutterstock.com/search/child-pain?image_type=illustration
https://casper.com/blogs/article/how-to-sleep-through-the-night?srsltid=AfmBOopZYrNTyvncNq8BHR7dy69eeNNrSlvgTAbOZUnEOnnAl3JeDWkc
"""

start = ""
while start != "yes" and start != "no":
    start = input("Are you under 10?: ")
    if start == "yes":

        # START
        clock = pygame.time.Clock()

        pygame.init()

        font = pygame.font.SysFont(None, 25)
        fontt = pygame.font.SysFont(None, 25)

        l = 800
        w = 600
        screen = pygame.display.set_mode((l, w))

        speed = 5

        # images

        nurse_image = pygame.image.load("wave.png").convert_alpha()
        paper_image = pygame.image.load("paper.png").convert_alpha()
        mentalpic = pygame.image.load("mental.png").convert_alpha()
        physical = pygame.image.load("physical.png").convert_alpha()
        water = pygame.image.load("water.png").convert_alpha()
        sleep = pygame.image.load("sleeptime.png").convert_alpha()

        bg = pygame.image.load('bg.png').convert()


        # FUNCTIONS
        def calculate_mental_state(sleep_hours, stress):

            sleep_hours = int(sleep_hours)
            stress = int(stress)
            mental_score = 0
            if sleep_hours >= 9:
                mental_score += 10
            elif sleep_hours >= 7:
                mental_score += 7
            elif sleep_hours >= 5:
                mental_score += 5
            elif sleep_hours >= 3:
                mental_score += 3

            if stress >= 9:
                mental_score -= 9
            elif stress >= 7:
                mental_score -= 7
            elif stress >= 5:
                mental_score -= 5
            elif stress >= 3:
                mental_score -= 3
            else:
                mental_score += 0

            mental_score -= stress

            if mental_score <= -4:
                return "Critical"
            elif mental_score <= 1:
                return "At risk"
            elif mental_score <= 5:
                return "Stable"
            else:
                return "Low risk"

        def cal_physical(age_group, sleep_hours, gym_time):
            sleep_hours = int(sleep_hours)
            gym_time = int(gym_time)
            level_score = 5

            if sleep_hours < 6:
                level_score -= 2
            elif sleep_hours > 9:
                level_score -= 1

            if gym_time < 1:
                level_score -= 2
            elif gym_time >= 2:
                level_score += 2

            if age_group == "senior":
                level_score -= 1
            elif age_group == "kid":
                level_score += 1

            if level_score < 2:
                return "Bad"
            elif level_score <= 5:
                return "Neutral"
            else:
                return "Good"

        def calculate_water(base_water, gym_time, age_group):
            base_water = int(base_water)
            gym_time = int(gym_time)
            if age_group=="kid":
                exercise_water= gym_time
            elif age_group=="workforce":
                exercise_water= gym_time * 2
            else:
                exercise_water= gym_time * 3
            total=exercise_water + base_water
            return exercise_water, total

        def recommendation(mental_state, physical_state, sleep_hours, gym_time):
            
            sleep_hours = int(sleep_hours)
            gym_time = int(gym_time)
            bdialogue("SPACE HEALTH REPORT", l/2, nurse_rect.top-75)

            bdialogue("HEALTH ANALYSIS", l/2, nurse_rect.top-35)
            bdialogue(f"Mental state is in {mental_state} condition", l/2, nurse_rect.top-10)
            bdialogue(f"Physical state is in {physical_state} condition", l/2, nurse_rect.top+15)
            
            # Sleep feedback
            if sleep_hours < 7:
                bdialogue("Sleep Deficit Detected", l/2, nurse_rect.top+40)
                bdialogue("In space, poor sleep increases cognitive errors and reaction time delays.", l/2, nurse_rect.top+65)
                bdialogue("Recommendation: Improve sleep schedule and reduce light exposure before rest.", l/2, nurse_rect.top+90)
            elif sleep_hours > 9:
                bdialogue("Excess sleep Detected", l/2, nurse_rect.top+40)
                bdialogue("Too much sleep can reduce muscle maintenance in microgravity.", l/2, nurse_rect.top+65)
                bdialogue("Recommendation: Balance rest with activity.", l/2, nurse_rect.top+90)
            else:
                bdialogue("Sleep Stability Good", l/2, nurse_rect.top+40)
                
            bdialogue("EXERCISE ANALYSIS", l/2, nurse_rect.top+130)

            if gym_time < 1:
                bdialogue("Low Exercise Level", l/2, nurse_rect.top+155)
                bdialogue("Bone density loss occurs quickly in microgravity.", l/2, nurse_rect.top+180)
                bdialogue("Recommendation: Increase resistance training.", l/2, nurse_rect.top+205)
            elif gym_time >= 2:
                bdialogue("Strong Exercise Compliance", l/2, nurse_rect.top+155)
            else:
                bdialogue("Moderate Exercise Level", l/2, nurse_rect.top+155)
            
            bdialogue("--- SPACE HEALTH EDUCATION SUMMARY ---", l/2, nurse_rect.top+245)
            bdialogue("Key risks include bone loss, muscle atrophy, sleep disruption, and cognitive stress.", l/2, nurse_rect.top+270)
            bdialogue("Goal: balance sleep, exercise, and mental health for long-term space survival.", l/2, nurse_rect.top+295)
            bdialogue(f'The total amount of extra water given is {extra} L', l/2, nurse_rect.top+320)
            bdialogue(f'Your new total amount of water is {total} L', l/2, nurse_rect.top+345)
            
        def dialogue(text, x, y):
            text2 = font.render(text, True, (0, 0, 0), (255, 255, 255))
            text_rect = text2.get_rect(center=(x, y))
            screen.blit(text2, text_rect)

        def bdialogue(text, x, y):
            text2 = fontt.render(text, True, (0, 0, 0))
            text_rect = text2.get_rect(center=(x, y))
            screen.blit(text2, text_rect)

        # ---------------- MAIN PROGRAM ---------------- #

        status = 'game1'

        nurse_rect = nurse_image.get_rect()
        nurse_rect.midbottom = (-20, w)

        paper_rect = paper_image.get_rect()
        paper_rect.midbottom = (l/2, -20)

        running = True

        variable = ""
        age = ""
        sex = ""
        gym_time = ""
        sleep_time = ""
        stress = ""
        base_water = ""
        symptom_type = ""
        mental = ""
        part = ""
        part1 = ""
        age_group = ""

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if status == "game1":
                        if event.key == pygame.K_RETURN:
                            status = "game2"
                            
                        elif event.key == pygame.K_BACKSPACE:
                            age = age[:-1]
                        else: 
                            age += event.unicode
                            
                    elif status == "game2":
                        if event.key == pygame.K_RETURN:
                            status = "game3"
                        elif event.key == pygame.K_BACKSPACE:
                            gym_time = gym_time[:-1]
                        else: 
                            gym_time += event.unicode
                            
                    elif status == "game3":
                        if event.key == pygame.K_RETURN:
                            status = "game4"
                        elif event.key == pygame.K_BACKSPACE:
                            sleep_time = sleep_time[:-1]
                        else: 
                            sleep_time += event.unicode
                    
                    elif status == "game4":
                        if event.key == pygame.K_RETURN and (1 <= int(stress) <= 10):
                            status = "game5"
                        elif event.key == pygame.K_RETURN and not (1 <= int(stress) <= 10):
                            stress = ""
                        elif event.key == pygame.K_BACKSPACE:
                            stress = stress[:-1]
                        else: 
                            stress += event.unicode
                            
                    elif status == "game5":
                        if event.key == pygame.K_RETURN:
                            status = "game6"
                        elif event.key == pygame.K_BACKSPACE:
                            base_water = base_water[:-1]
                        else: 
                            base_water += event.unicode
                            
                    elif status == "game6":
                        if event.key == pygame.K_RETURN and (symptom_type == "a" or symptom_type == "b"):
                            status = "game7"
                        elif event.key == pygame.K_RETURN and not (symptom_type == "a" or symptom_type == "b"):
                                symptom_type = ""
                        elif event.key == pygame.K_BACKSPACE:
                            symptom_type = symptom_type[:-1]
                        else: 
                            symptom_type += event.unicode
                            
                    elif status == "game7":
                        if event.key == pygame.K_RETURN and (1 <= int(mental) <= 10):
                            status = "game8"
                        elif event.key == pygame.K_RETURN and not (1 <= int(mental) <= 10):
                            mental = ""
                        elif event.key == pygame.K_BACKSPACE:
                            mental = mental[:-1]
                        else: 
                            mental += event.unicode
                    
                    elif status == "game8":
                        if event.key == pygame.K_RETURN and (part == "a" or part == "b"):
                            status = "game9"
                        elif event.key == pygame.K_RETURN and not (part == "a" or part == "b"):
                            part = ""
                        elif event.key == pygame.K_BACKSPACE:
                            part = part[:-1]
                        else: 
                            part += event.unicode
                            
                    elif status == "game9":
                        if event.key == pygame.K_RETURN and (part1 == "a" or part1 == "b"):
                            status = "game9.5"
                        elif event.key == pygame.K_RETURN and not (part1 == "a" or part1 == "b"):
                            part1 = ""
                        elif event.key == pygame.K_BACKSPACE:
                            part1 = part1[:-1]
                        else: 
                            part1 += event.unicode
            
            screen.blit(bg, (0, 0))
            clock.tick(60)
            screen.blit(nurse_image, nurse_rect)
            screen.blit(paper_image, paper_rect)
            
            if status == 'game1':
                if nurse_rect.midbottom != (l/2, w):
                    nurse_rect.x += speed
                else:
                    dialogue("How old are you?", l/2, nurse_rect.top-20)
                    dialogue(age, l/2, nurse_rect.top)
                    dialogue("Press return to input", l/2, nurse_rect.top+20)
                    nurse_image = pygame.image.load("board.png").convert_alpha()
                
            elif status == 'game2':
                dialogue("How many hours have you exercised lately?", l/2, nurse_rect.top-20)
                dialogue(gym_time, l/2, nurse_rect.top)
                dialogue("Press return to input", l/2, nurse_rect.top+20)
                
            elif status == 'game3':
                dialogue("How many hours of sleep do you usually get in a day?", l/2, nurse_rect.top-20)
                dialogue(sleep_time, l/2, nurse_rect.top)
                dialogue("Press return to input", l/2, nurse_rect.top+20)
                sleep_rect = sleep.get_rect()
                sleep_rect.center = (l/5, w*1/5)
                screen.blit(sleep, sleep_rect)

            elif status == 'game4':
                dialogue("Rate your stress level (1–10):", l/2, nurse_rect.top-20)
                dialogue(stress, l/2, nurse_rect.top)
                dialogue("Press return to input", l/2, nurse_rect.top+20)
                
            elif status == 'game5':
                dialogue("How many litres of water do you usually receive daily?:", l/2, nurse_rect.top-20)
                dialogue(base_water, l/2, nurse_rect.top)
                dialogue("Press return to input", l/2, nurse_rect.top+20)
                
                water_rect = water.get_rect()
                water_rect.center = (l*4/5, w/2)
                screen.blit(water, water_rect)
            
            elif status == 'game6':
                dialogue("Are you experiencing mental or physical difficulties?", l/2, nurse_rect.top-20)
                dialogue("for mental health, input a and for physical health, input b", l/2, nurse_rect.top)
                dialogue(symptom_type, l/2, nurse_rect.top+20)
                dialogue("Press return to input", l/2, nurse_rect.top+40)
                
                physical_rect = physical.get_rect()
                physical_rect.center = (l*4/5, w*4/5)
                screen.blit(physical, physical_rect)
                
                mentalpic_rect = mentalpic.get_rect()
                mentalpic_rect.center = (l/5, w*4/5)
                screen.blit(mentalpic, mentalpic_rect)
            
            if status == 'game7':
                # Mental
                if symptom_type == "b":
                    status = 'game8'
                if symptom_type == "a":
                    dialogue("Rate your condition from 1–10 (10 = extreme pain): ", l/2, nurse_rect.top-20)
                    dialogue(mental, l/2, nurse_rect.top)
                    dialogue("Press return to input", l/2, nurse_rect.top+20)
            
            elif status == 'game8':
                # Physical
                dialogue("Are you feeling pain in a specific area? for yes, input a and for no, input b", l/2, nurse_rect.top-20)
                dialogue(part, l/2, nurse_rect.top)
                dialogue("Press return to input", l/2, nurse_rect.top+20)
                
            elif status == 'game9':
                if part == "b":
                    status = 'game9.5'
                elif part == "a":
                    dialogue("Are you feeling pain in your head or your back? for head, input a and for back, input b", l/2, nurse_rect.top-20)
                    dialogue(part1, l/2, nurse_rect.top)
                    dialogue("Press return to input", l/2, nurse_rect.top+20)
                    
            elif status == 'game9.5':
                if nurse_rect.right > l/3:
                    nurse_rect.x -= speed
                else:
                    nurse_image = pygame.image.load("thumb.png").convert_alpha()
                if paper_rect.bottom < w+30:
                    paper_rect.y += speed
                else:
                    # main display
                    if part1 == "a":
                        bdialogue("Your likely diagnosis is space related eye syndrome", l/2, nurse_rect.top-115)
                    elif part1 == "b":
                        bdialogue("Your likely diagnosis is fatigue-related discomfort", l/2, nurse_rect.top-115)
                    if part1 == "":
                        bdialogue("Your likely diagnosis is general fatigue", l/2, nurse_rect.top-115)
                        
                    mental_state = calculate_mental_state(sleep_time, stress)
                    physical_state = cal_physical(age_group, sleep_time, gym_time)
                    extra, total = calculate_water(base_water, gym_time, age_group)
                    recommendation(mental_state, physical_state, sleep_time, gym_time)
                    
            pygame.display.flip()
        pygame.quit()
    
    elif start == "no":
        # ---------------- Setup ---------------- #

        import tkinter as tk
        from tkinter import ttk
        import random

        # ---------------- WINDOW ---------------- #

        root = tk.Tk()
        root.title("Space Health Tracker")
        root.geometry("950x700")
        root.configure(bg="#1f2235") #Dark Blue Theme

        # ---------------- VARIABLES ---------------- #

        week = 1 #Current Week
        travel_time = 0 #Total Weeks Travelled

        stress = 0
        sleep_time = 0
        gym_time = 0
        base_water = 0
        age_group = ""

        # ---------------- APPERANCE ---------------- #

        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "TLabel",
            background="#1f2235",
            foreground="white",
            font=("Arial", 12)
        )

        # NEXT WEEK button
        style.configure(
            "Big.TButton",
            font=("Arial", 16, "bold"),
            padding=18)

        # ---------------- FUNCTIONS ---------------- #

        def calculate_mental_state(sleep_hours, stress):

            mental_score = 0

            if sleep_hours >= 9: #More Sleep = better mental health
                mental_score += 10
            elif sleep_hours >= 7:
                mental_score += 7
            elif sleep_hours >= 5:
                mental_score += 5
            elif sleep_hours >= 3:
                mental_score += 3

            mental_score -= stress #Stress reduce mental score

            if mental_score <= -4:
                return "Critical"
            elif mental_score <= 1:
                return "At Risk"
            elif mental_score <= 5:
                return "Stable"
            else:
                return "Low Risk"


        def cal_physical(age_group, sleep_hours, gym_time):

            level_score = 5 #Base health score

            # Bad sleep = worse health
            if sleep_hours < 6:
                level_score -= 2
            elif sleep_hours > 9:
                level_score -= 1

            # Excercise improve health
            if gym_time < 1:
                level_score -= 2
            elif gym_time >= 2:
                level_score += 2

            if age_group == "senior":
                level_score -= 1
            elif age_group == "kid":
                level_score += 1

            if level_score < 2:
                return "Bad"
            elif level_score <= 5:
                return "Neutral"
            else:
                return "Good"


        def calculate_water(base_water, gym_time, age_group):
            """
            Calculates the extra amount of water needed due to excerise
            """
            if age_group == "kid":
                extra = gym_time
            elif age_group == "workforce":
                extra = gym_time * 2 #Need double the amount of water
            else:
                extra = gym_time * 3 #Need triple

            total = base_water + extra #Total water provided

            return extra, total


        def weekly_event():
            global stress, sleep_time, gym_time

            event = random.randint(1, 5)

            if event == 1:
                text = "Solar storm disrupted systems."
                stress += 5
                sleep_time -= 2

            elif event == 2:
                text = "Successful team workout."
                stress -= 2
                gym_time += 2

            elif event == 3:
                text = "Equipment malfunction."
                gym_time -= 2

            elif event == 4:
                text = "Encouraging messages from Earth."
                stress -= 4

            else:
                text = "Emergency interrupted sleep."
                sleep_time -= 3
                stress += 5

            return text

        # ---------------- START SIMULATION ---------------- #

        def start_simulation():

            global travel_time, stress, sleep_time, gym_time, base_water, age_group, week

            week = 1
            #Getting the value from the slider values (UI)
            age = age_slider.get()
            travel_time = travel_slider.get()
            gym_time = gym_slider.get()
            sleep_time = sleep_slider.get()
            stress = stress_slider.get()
            base_water = water_slider.get()

            if age <= 14:
                age_group = "kid"
            elif age <= 65:
                age_group = "workforce"
            else:
                age_group = "senior"

            output_text.delete("1.0", tk.END) #Clears the screen before starting
            output_text.insert(tk.END, " Simulation Started\n\n")

            next_week_button.config(state="normal")

        # ---------------- NEXT WEEK ---------------- #

        def next_week():

            global week

            if week > travel_time: #Stops when they leave spaceship
                output_text.insert(tk.END, "\n Journey Complete.\n")
                return

            event = weekly_event() #creates a random event

            mental = calculate_mental_state(sleep_time, stress) #Update states

            physical = cal_physical(age_group, sleep_time, gym_time)

            extra, total = calculate_water(base_water, gym_time, age_group)

            output_text.insert(tk.END, f"\n========== WEEK {week} ==========\n")
            output_text.insert(tk.END, f"Weeks Remaining: {travel_time - week}\n\n")
            output_text.insert(tk.END, f"EVENT: {event}\n\n")
            output_text.insert(tk.END, f"Mental State: {mental}\n")
            output_text.insert(tk.END, f"Physical State: {physical}\n")
            output_text.insert(tk.END, f"Extra Water Needed: {extra}L\n")
            output_text.insert(tk.END, f"Total Water: {total}L\n")

            if sleep_time < 7:
                output_text.insert(tk.END, "Sleep Deficit\n")

            if gym_time < 1:
                output_text.insert(tk.END, "Low Exercise\n")

            output_text.insert(tk.END, "\n")

            week += 1 #continues the simulation

        # ---------------- TITLE ---------------- #

        title = ttk.Label(
            root,
            text=" SPACE HEALTH TRACKER",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=20)

        # ---------------- MAIN FRAME ---------------- #

        main_frame = ttk.Frame(root)

        main_frame.pack(fill="both", expand=True)

        # ---------------- INPUT FRAME ---------------- #

        input_frame = ttk.Frame(main_frame)

        input_frame.pack(side="left", padx=20, pady=20)


        def create_slider(label, from_num, to_num):

            ttk.Label(input_frame, text=label).pack(anchor="w")

            slider = tk.Scale( #The slider
                input_frame,
                from_=from_num,
                to=to_num,
                orient="horizontal",
                length=250,
                bg="#1f2235",
                fg="white",
                highlightthickness=0
            )

            slider.pack(pady=10)

            return slider


        travel_slider = create_slider("Travel Weeks", 1, 52)
        age_slider = create_slider("Age", 1, 100)
        sleep_slider = create_slider("Sleep Hours", 0, 12)
        gym_slider = create_slider("Gym Hours", 0, 10)
        stress_slider = create_slider("Stress Level", 1, 10)
        water_slider = create_slider("Water Intake", 0, 10)

        # ---------------- BUTTONS ---------------- #

        start_button = ttk.Button(
            input_frame,
            text="Start Simulation",
            command=start_simulation
        )

        start_button.pack(pady=15) #Above and below space (y-axis)

        # INCREASING THE WEEK
        next_week_button = ttk.Button(
            input_frame,
            text="NEXT WEEK",
            command=next_week,
            state="disabled",
            style="Big.TButton"
        )

        next_week_button.pack(pady=20, ipadx=20, ipady=10)

        # ---------------- OUTPUT ---------------- #

        output_frame = ttk.Frame(main_frame)

        output_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        output_text = tk.Text(
            output_frame,
            bg="#2b2f4a",
            fg="white",
            font=("Consolas", 11),
            width=55,
            height=30,
            bd=0
        )

        output_text.pack(fill="both", expand=True)

        # ---------------- RUN APP ---------------- #

        root.mainloop()

        # ---------------- WINDOW ---------------- #

        root = tk.Tk()
        root.title("Space Health Tracker")
        root.geometry("950x700")
        root.configure(bg="#1f2235") #Dark Blue Theme

        # ---------------- VARIABLES ---------------- #

        week = 1
        travel_time = 0

        stress = 0
        sleep_time = 0
        gym_time = 0
        base_water = 0
        age_group = ""

        # ---------------- APPERANCE ---------------- #

        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "TLabel",
            background="#1f2235",
            foreground="white",
            font=("Arial", 12)
        )

        style.configure(
            "Big.TButton",
            font=("Arial", 16, "bold"),
            padding=18
        )

        # ---------------- FUNCTIONS ---------------- #

        def calculate_mental_state(sleep_hours, stress):

            mental_score = 0

            if sleep_hours >= 9:
                mental_score += 10
            elif sleep_hours >= 7:
                mental_score += 7
            elif sleep_hours >= 5:
                mental_score += 5
            elif sleep_hours >= 3:
                mental_score += 3

            mental_score -= stress

            if mental_score <= -4:
                return "Critical"
            elif mental_score <= 1:
                return "At Risk"
            elif mental_score <= 5:
                return "Stable"
            else:
                return "Low Risk"


        def cal_physical(age_group, sleep_hours, gym_time):

            level_score = 5

            if sleep_hours < 6:
                level_score -= 2
            elif sleep_hours > 9:
                level_score -= 1

            if gym_time < 1:
                level_score -= 2
            elif gym_time >= 2:
                level_score += 2

            if age_group == "senior":
                level_score -= 1
            elif age_group == "kid":
                level_score += 1

            if level_score < 2:
                return "Bad"
            elif level_score <= 5:
                return "Neutral"
            else:
                return "Good"


        def calculate_water(base_water, gym_time, age_group):

            if age_group == "kid":
                extra = gym_time
            elif age_group == "workforce":
                extra = gym_time * 2
            else:
                extra = gym_time * 3

            total = base_water + extra

            return extra, total


        def recommendation(sleep, gym, stress):

            if sleep < 7:
                return "Improve sleep consistency for recovery."
            elif sleep > 9:
                return "Reduce oversleeping for better balance."

            if gym < 1:
                return "Increase exercise to prevent muscle loss."
            elif gym >= 2:
                return "Exercise levels are strong."

            if stress >= 7:
                return "Reduce stress through rest and planning."

            return "Health balance is stable."


        def weekly_event():
            global stress, sleep_time, gym_time

            event = random.randint(1, 5)

            if event == 1:
                text = "Solar storm disrupted systems."
                stress += 5
                sleep_time -= 2

            elif event == 2:
                text = "Successful team workout."
                stress -= 2
                gym_time += 2

            elif event == 3:
                text = "Equipment malfunction."
                gym_time -= 2

            elif event == 4:
                text = "Encouraging messages from Earth."
                stress -= 4

            else:
                text = "Emergency interrupted sleep."
                sleep_time -= 3
                stress += 5

            return text

        # ---------------- START SIMULATION ---------------- #

        def start_simulation():

            global travel_time, stress, sleep_time, gym_time, base_water, age_group, week

            week = 1

            age = age_slider.get()
            travel_time = travel_slider.get()
            gym_time = gym_slider.get()
            sleep_time = sleep_slider.get()
            stress = stress_slider.get()
            base_water = water_slider.get()

            if age <= 14:
                age_group = "kid"
            elif age <= 65:
                age_group = "workforce"
            else:
                age_group = "senior"

            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, " Simulation Started\n\n")

            next_week_button.config(state="normal")

        # ---------------- NEXT WEEK ---------------- #

        def next_week():

            global week

            if week > travel_time:
                output_text.insert(tk.END, "\n Journey Complete.\n")
                return

            event = weekly_event()

            mental = calculate_mental_state(sleep_time, stress)
            physical = cal_physical(age_group, sleep_time, gym_time)
            extra, total = calculate_water(base_water, gym_time, age_group)

            output_text.insert(tk.END, f"\n========== WEEK {week} ==========\n")
            output_text.insert(tk.END, f"Weeks Remaining: {travel_time - week}\n\n")

            output_text.insert(tk.END, f"EVENT: {event}\n\n")
            output_text.insert(tk.END, f"Mental State: {mental}\n")
            output_text.insert(tk.END, f"Physical State: {physical}\n")
            output_text.insert(tk.END, f"Extra Water Needed: {extra}L\n")
            output_text.insert(tk.END, f"Total Water: {total}L\n")

            if sleep_time < 7:
                output_text.insert(tk.END, "Sleep Deficit\n")

            if gym_time < 1:
                output_text.insert(tk.END, "Low Exercise\n")

            # ✅ FINAL RECOMMENDATION LINE
            output_text.insert(
                tk.END,
                f"\nRecommendation: {recommendation(sleep_time, gym_time, stress)}\n"
            )

            output_text.insert(tk.END, "\n")

            week += 1

        # ---------------- UI ---------------- #

        title = ttk.Label(
            root,
            text=" SPACE HEALTH TRACKER",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=20)

        main_frame = ttk.Frame(root)
        main_frame.pack(fill="both", expand=True)

        input_frame = ttk.Frame(main_frame)
        input_frame.pack(side="left", padx=20, pady=20)


        def create_slider(label, from_num, to_num):

            ttk.Label(input_frame, text=label).pack(anchor="w")

            slider = tk.Scale(
                input_frame,
                from_=from_num,
                to=to_num,
                orient="horizontal",
                length=250,
                bg="#1f2235",
                fg="white",
                highlightthickness=0
            )

            slider.pack(pady=10)

            return slider


        travel_slider = create_slider("Travel Weeks", 1, 52)
        age_slider = create_slider("Age", 1, 100)
        sleep_slider = create_slider("Sleep Hours", 0, 12)
        gym_slider = create_slider("Gym Hours", 0, 10)
        stress_slider = create_slider("Stress Level", 1, 10)
        water_slider = create_slider("Water Intake", 0, 10)

        start_button = ttk.Button(
            input_frame,
            text="Start Simulation",
            command=start_simulation
        )
        start_button.pack(pady=15)

        next_week_button = ttk.Button(
            input_frame,
            text="NEXT WEEK",
            command=next_week,
            state="disabled",
            style="Big.TButton"
        )
        next_week_button.pack(pady=20, ipadx=20, ipady=10)

        output_frame = ttk.Frame(main_frame)
        output_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        output_text = tk.Text(
            output_frame,
            bg="#2b2f4a",
            fg="white",
            font=("Consolas", 11),
            width=55,
            height=30,
            bd=0
        )

        output_text.pack(fill="both", expand=True)

        root.mainloop()
