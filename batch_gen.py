import subprocess

start_i = 0
end_i = 49
target_list = list(range(start_i, end_i + 1))
# target_list = [1, 2, 3, 49]

for i in target_list:
    # print(i)
    # subprocess.run(["ls", "-l", f"/data/episode_{i}.hdf5"])
    subprocess.run(
        [
            "python3",
            "visualize_episodes.py",
            "--dataset_dir",
            "./data",
            "--episode_idx",
            f"{i}",
        ]
    )
