import numpy as np
import torch
import torch.nn as nn
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt


audio = np.load("audio_dataset.npy")
motion = np.load("motion_dataset.npy")

print("audio:", audio.shape)
print("motion:", motion.shape)

print("audio nan:", np.isnan(audio).sum())
print("motion nan:", np.isnan(motion).sum())


audio = np.nan_to_num(audio)
motion = np.nan_to_num(motion)

# ---------- normalization----------
audio = (audio - audio.mean()) / (audio.std() + 1e-8)
motion = (motion - motion.mean()) / (motion.std() + 1e-8)

audio_t = torch.tensor(audio, dtype=torch.float32)
motion_t = torch.tensor(motion, dtype=torch.float32)


class AlignNet(nn.Module):
    def __init__(self, a_dim, m_dim):
        super().__init__()
        self.fc = nn.Linear(a_dim, m_dim)

    def forward(self, x):
        return self.fc(x)

model = AlignNet(audio.shape[1], motion.shape[1])
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)  # 降 learning rate
loss_fn = nn.MSELoss()

print("training...")

for epoch in range(300):
    pred = model(audio_t)
    loss = loss_fn(pred, motion_t)

    if torch.isnan(loss):
        print("LOSS BECAME NAN")
        break

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 50 == 0:
        print("epoch", epoch, "loss:", loss.item())

print("final loss:", loss.item())


mapped = model(audio_t).detach().numpy()

correct_scores = []
for i in range(len(mapped)):
    s = cosine_similarity(
        mapped[i].reshape(1, -1),
        motion[i].reshape(1, -1)
    )[0][0]
    correct_scores.append(s)

shuffled_motion = motion.copy()
np.random.shuffle(shuffled_motion)

shuffle_scores = []
for i in range(len(mapped)):
    s = cosine_similarity(
        mapped[i].reshape(1, -1),
        shuffled_motion[i].reshape(1, -1)
    )[0][0]
    shuffle_scores.append(s)

print("correct mean:", np.mean(correct_scores))
print("shuffle mean:", np.mean(shuffle_scores))


plt.hist(correct_scores, bins=40, alpha=0.6, label="correct")
plt.hist(shuffle_scores, bins=40, alpha=0.6, label="shuffled")
plt.legend()
plt.title("Alignment Distribution")
plt.show()