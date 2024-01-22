import numpy as np
import binvox_rw

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
from moviepy.editor import *

path = "./data/model.binvox"

def func(path, gif_path, video_path):

    with open(path, "rb") as f:
        model = binvox_rw.read_as_3d_array(f)

    voxels = model.data

    voxels = np.transpose(voxels, (2, 1, 0))
    voxels = np.transpose(voxels, (0, 2, 1))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_axis_off()

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.tick_params(bottom=False, left=False)

    ax.voxels(voxels, edgecolor='k')

    def rotate(angle):
        ax.view_init(azim=angle)

    # 创建动画
    rot_animation = animation.FuncAnimation(fig, rotate, frames=np.arange(0, 360, 4), interval=0.5)

    # 保存动画
    rot_animation.save(gif_path, dpi=100, writer='imagemagick')
    video = VideoFileClip(gif_path)
    target_duration = video.duration / 3
    compressed_video = video.fx(vfx.speedx, target_duration)
    compressed_video.write_videofile(video_path)

    plt.show()

if __name__ == "__main__":
    func(path, "./example.gif", "./example.mp4")