import numpy as np
import pygame
import random

# Constants
G = 6.67430e-11  # Gravitational Constant
M_sun = 1.989e30  # Mass of the Sun (kg)
M_earth = 5.972e24  # Mass of Earth (kg)
M_mercury = 3.30104e23  # Mass of Mercury (kg)
M_venus=4.867e24 # Mass of Venus
M_mars=6.4171e23 #Mass of Mercury
#initial Distance and velocity
AU = 1.496e11  # 1 Astronomical Unit (meters)
dt = 60 * 60  # Time step (1 hour in seconds)

#EArth's initial position and velocity
x_earth=AU
y_earth=0
vx_earth=0
vy_earth=29.78e3



# Mercury's initial position and velocity
x_mercury = 0.387 * AU
y_mercury = 0
vx_mercury = 0
vy_mercury = 47.87e3  # Orbital speed of Mercury (m/s)

#VEnus's initial position and velocity
x_venus=0.723*AU
y_venus=0
vx_venus=0
vy_venus=35.02e3

#Mars
x_mars=1.524*AU
y_mars=0
vx_mars=0
vy_mars=24.07e3


#scsreen dimenstions
WIDTH,HEIGHT=1280,720
CENTER=(WIDTH//2,HEIGHT//2)

#pygame setup
pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Orbits")
clock=pygame.time.Clock()


#Simulation Loop vairables
earth_position_x,earth_position_y=[],[]
earth_orbit_x,earth_orbit_y=[],[]

venus_position_x,venus_position_y=[],[]
venus_orbit_x,venus_orbit_y=[],[]

mercury_position_x,mercury_position_y=[],[]
mercury_orbit_x,mercury_orbit_y=[],[]

mars_position_x,mars_position_y=[],[]
mars_orbit_x,mars_orbit_y=[],[]
#Total time simulation (1 years)
total_time=365*10*24*60*60 # 1  years in seconds
dt_base=60*60 # 1hour
dt_factor=10 # can be chnaged to adjust the speed
dt=dt_base*dt_factor
num_steps=total_time//dt
#simulation loop to calculate position
for i in range(num_steps):
    #MArs
    r_mars=np.sqrt(x_mars**2+y_mars**2)
    F_mars=G*M_mars*M_sun/r_mars**2
    Fx_mars=-F_mars*(x_mars/r_mars)
    Fy_mars=-F_mars*(y_mars/r_mars)
    ax_mars=Fx_mars/M_mars
    ay_mars=Fy_mars/M_mars
    vx_mars+=ax_mars*dt
    vy_mars+=ay_mars*dt
    x_mars+=vx_mars*dt
    y_mars+=vy_mars*dt
    mars_position_x.append(x_mars)
    mars_position_y.append(y_mars)
    mars_orbit_x.append(x_mars)
    mars_orbit_y.append(y_mars)
    #Earth 
    r_earth=np.sqrt(x_earth**2+y_earth**2)
    F_earth=G*M_earth*M_sun/r_earth**2
    Fx_earth=-F_earth*(x_earth/r_earth)
    Fy_earth=-F_earth*(y_earth/r_earth)
    ax_earth=Fx_earth/M_earth
    ay_earth=Fy_earth/M_earth
    vx_earth+=ax_earth*dt
    vy_earth+=ay_earth*dt
    x_earth+=vx_earth*dt
    y_earth+=vy_earth*dt
    earth_position_x.append(x_earth)
    earth_position_y.append(y_earth)
    earth_orbit_x.append(x_earth)
    earth_orbit_y.append(y_earth)

    #for venus
    r_venus=np.sqrt(x_venus**2+y_venus**2)
    F_venus=G*M_venus*M_sun/r_venus**2
    Fx_venus=-F_venus*(x_venus/r_venus)
    Fy_venus=-F_venus*(y_venus/r_venus)
    ax_venus=Fx_venus/M_venus
    ay_venus=Fy_venus/M_venus
    vx_venus+=ax_venus*dt
    vy_venus+=ay_venus*dt
    x_venus+=vx_venus*dt
    y_venus+=vy_venus*dt
    venus_position_x.append(x_venus)
    venus_position_y.append(y_venus)
    venus_orbit_x.append(x_venus)
    venus_orbit_y.append(y_venus)

    # Mercury calculations


    r_mercury = np.sqrt(x_mercury**2 + y_mercury**2)
    F_mercury = G * M_sun * M_mercury / r_mercury**2
    Fx_mercury = -F_mercury * (x_mercury / r_mercury)
    Fy_mercury = -F_mercury * (y_mercury / r_mercury)
    ax_mercury = Fx_mercury / M_mercury
    ay_mercury = Fy_mercury / M_mercury
    vx_mercury += ax_mercury * dt
    vy_mercury += ay_mercury * dt
    x_mercury += vx_mercury * dt
    y_mercury += vy_mercury * dt
    mercury_position_x.append(x_mercury)
    mercury_position_y.append(y_mercury)
    mercury_orbit_x.append(x_mercury)
    mercury_orbit_y.append(y_mercury)



#Visualization setup
running=True
frame=0

# Colors
earth_color = (0, 0, 255)
mercury_color = (255, 255, 0)
sun_color = (255, 165, 0)
venus_color=(173,216,230)
orbit_color_venus=(225,225,225)
orbit_color_earth = (0, 255, 0)
orbit_color_mercury = (255, 0, 0)
star_color=(225,225,225)
orbit_color_mars=(225,145,123)
mars_color=(225,224,223)

# Scaling factor
scale = 1e-9
stars=[]
num_stars=500
for _ in range(num_stars):
    x=random.randint(0,WIDTH)
    y=random.randint(0,HEIGHT)
    size=random.randint(1,1)
    stars.append((x,y,size))
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    #clear the screen
    screen.fill((0,0,0))

    #Draw the sun
    pygame.draw.circle(screen,sun_color,CENTER,30)

    # draw stars 
    for star in stars:
        pygame.draw.circle(screen, star_color, (star[0], star[1]), star[2])

    #Draw Mars Orbit
    #Draw Mars Orbit
    for i in range(1,len(mars_orbit_x)):
    # Access elements of the tuple using indexing
        x1 = int(CENTER[0] + mars_orbit_x[i-1] * scale)  # X-coordinate of previous point
        y1 = int(CENTER[1] + mars_orbit_y[i-1] * scale)  # Y-coordinate of previous point
        x2 = int(CENTER[0] + mars_orbit_x[i] * scale)    # X-coordinate of current point
        y2 = int(CENTER[1] + mars_orbit_y[i] * scale)    # Y-coordinate of current point
        pygame.draw.line(screen,orbit_color_mars,(x1,y1),(x2,y2),1)
    # Draw Earth's orbit
    for i in range(1, len(earth_orbit_x)):
        pygame.draw.line(screen, orbit_color_earth, 
                         (int(CENTER[0] + earth_orbit_x[i-1] * scale), int(CENTER[1] + earth_orbit_y[i-1] * scale)),
                         (int(CENTER[0] + earth_orbit_x[i] * scale), int(CENTER[1] + earth_orbit_y[i] * scale)), 1)

    # Draw Mercury's orbit
    for i in range(1, len(mercury_orbit_x)):
        pygame.draw.line(screen, orbit_color_mercury, 
                         (int(CENTER[0] + mercury_orbit_x[i-1] * scale), int(CENTER[1] + mercury_orbit_y[i-1] * scale)),
                         (int(CENTER[0] + mercury_orbit_x[i] * scale), int(CENTER[1] + mercury_orbit_y[i] * scale)), 1)
    # Draw venus's orbit
    for i in range(1, len(venus_orbit_x)):
        pygame.draw.line(screen, orbit_color_venus, 
                         (int(CENTER[0] + venus_orbit_x[i-1] * scale), int(CENTER[1] + venus_orbit_y[i-1] * scale)),
                         (int(CENTER[0] + venus_orbit_x[i] * scale), int(CENTER[1] + venus_orbit_y[i] * scale)), 1)

    #Draw Mars
    if frame < len(mars_position_x):
        mars_x = int(CENTER[0] + mars_position_x[frame] * scale)
        mars_y = int(CENTER[1] + mars_position_y[frame] * scale)
        pygame.draw.circle(screen, mars_color, (mars_x, mars_y), 10)
    # Draw Earth
    if frame < len(earth_position_x):
        earth_x = int(CENTER[0] + earth_position_x[frame] * scale)
        earth_y = int(CENTER[1] + earth_position_y[frame] * scale)
        pygame.draw.circle(screen, earth_color, (earth_x, earth_y), 10)
     # Draw venus
    if frame < len(venus_position_x):
        venus_x = int(CENTER[0] + venus_position_x[frame] * scale)
        venus_y = int(CENTER[1] + venus_position_y[frame] * scale)
        pygame.draw.circle(screen, venus_color, (venus_x, venus_y), 10)
    # Draw Mercury
    if frame < len(mercury_position_x):
        mercury_x = int(CENTER[0] + mercury_position_x[frame] * scale)
        mercury_y = int(CENTER[1] + mercury_position_y[frame] * scale)
        pygame.draw.circle(screen, mercury_color, (mercury_x, mercury_y), 5)

    # Update frame
    frame += 1

 
    
    # Update display
    pygame.display.update()
    clock.tick(60)





pygame.quit()