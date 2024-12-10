        x1 = int(CENTER[0] + mars_orbit_x[i-1] * scale)  # X-coordinate of previous point
        y1 = int(CENTER[1] + mars_orbit_y[i-1] * scale)  # Y-coordinate of previous point
        x2 = int(CENTER[0] + mars_orbit_x[i] * scale)    # X-coordinate of current point
        y2 = int(CENTER[1] + mars_orbit_y[i] * scale)    # Y-coordinate of current point
        pygame.draw.line(screen,orbit_color_mars,(x1,y1),(x2,y2),1)