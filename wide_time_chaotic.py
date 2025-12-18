import cv2
import numpy as np
from moviepy import VideoFileClip
import os
import time

def logistic_map(n, x=0.7, r=3.93):  # r should be between 3.57 and 4.0 for chaotic behavior; initial state x is inconsequential as long as it's between 0 and 1
    for _ in range(n):
        x = r * x * (1 - x)
    return x
    
def wide_time_effect(get_frame, t, backward_steps=6, forward_steps=10, blend_amount=0.5, fps=18):
    time_step = logistic_map(int(t * fps))
    time_step_norm = time_step/fps
    accumulator = get_frame(t).astype(np.float32)
    for i in range(1, backward_steps + 1):
        past_time = t - i * time_step_norm
        if past_time >= 0:
            past_frame = get_frame(past_time).astype(np.float32)
            accumulator = cv2.addWeighted(accumulator, 1.0, past_frame, blend_amount, 0.0)
            
    for i in range(1, forward_steps + 1):
        future_time = t + i * time_step_norm
        if future_time <= clip.duration:
            future_frame = get_frame(future_time).astype(np.float32)
            accumulator = cv2.addWeighted(accumulator, 1.0, future_frame, blend_amount, 0.0)
            
    total_weight = 1 + (blend_amount * (backward_steps + forward_steps))
    
    final_frame = accumulator / total_weight
    return np.clip(final_frame, 0, 255).astype(np.uint8)


start_time = time.time()
 
clip = VideoFileClip("test.mp4") #insert video path here
audio = clip.audio

fps = 18
processed_clip = clip.transform(lambda gf, t: wide_time_effect(gf, t, backward_steps=6, forward_steps=10, blend_amount=0.5, fps=fps))
final_clip = processed_clip.with_audio(audio)
final_clip.write_videofile("r_393.mp4", fps=fps, audio_codec="aac")
print("--- %s seconds ---" % (time.time() - start_time))



