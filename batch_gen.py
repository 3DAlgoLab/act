import subprocess

start_i = 7
end_i = 38

for i in range(start_i, end_i+1):
    # print(i)
    # subprocess.run(["ls", "-l", f"/data/episode_{i}.hdf5"]) 
    subprocess.run(["python3", "visualize_episodes.py", "--dataset_dir", "/data", 
                    "--episode_idx", f"{i}"])