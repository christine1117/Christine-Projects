import numpy as np
import librosa
import glob
import pickle
import os

audio_files = glob.glob("wav/*.wav")
motion_files = glob.glob("keypoints3d/*.pkl")

audio_dict = {}

# music ID → audio embedding
for a in audio_files:
    name = os.path.basename(a).replace(".wav", "")
    
    y, sr = librosa.load(a)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)
    audio_vec = np.mean(mfcc, axis=1)

    audio_dict[name] = audio_vec

audio_embeds = []
motion_embeds = []

for m in motion_files:
    name = os.path.basename(m)
    
    
    parts = name.split("_")
    music_id = [p for p in parts if p.startswith("m")][0]

    if music_id not in audio_dict:
        continue

    with open(m, "rb") as f:
        data = pickle.load(f)

    keypoints = np.array(data["keypoints3d"])
    motion_vec = np.mean(keypoints, axis=0).flatten()

    audio_embeds.append(audio_dict[music_id])
    motion_embeds.append(motion_vec)

audio_array = np.array(audio_embeds)
motion_array = np.array(motion_embeds)

print("audio shape:", audio_array.shape)
print("motion shape:", motion_array.shape)

np.save("audio_dataset.npy", audio_array)
np.save("motion_dataset.npy", motion_array)