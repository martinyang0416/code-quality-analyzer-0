import math

def compute_intervals(a_seg, b_seg, R):
    a_t_start, a_t_end, a_vx, a_vy, a_x0, a_y0 = a_seg
    b_t_start, b_t_end, b_vx, b_vy, b_x0, b_y0 = b_seg

    t_start = max(a_t_start, b_t_start)
    t_end = min(a_t_end, b_t_end)
    if t_start >= t_end:
        return []

    a = a_vx - b_vx
    c1 = (a_x0 - b_x0) - a_vx * a_t_start + b_vx * b_t_start
    b_coeff = a_vy - b_vy
    c2 = (a_y0 - b_y0) - a_vy * a_t_start + b_vy * b_t_start

    A = a**2 + b_coeff**2
    B = 2 * (a * c1 + b