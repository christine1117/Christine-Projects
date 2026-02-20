import numpy as np
import torch
import torch.nn as nn
from sklearn.metrics.pairwise import cosine_similarity

# ========= load dataset =========
audio = np.load("audio_dataset.npy")
motion = np.load("motion_dataset.npy")

print("audio:", audio.shape)
print("motion:", motion.shape)

# ---------- clean NaN ----------
audio = np.nan_to_num(audio)
motion = np.nan_to_num(motion)

# ---------- L2 normalize ----------
audio = audio / (np.linalg.norm(audio, axis=1, keepdims=True) + 1e-8)
motion = motion / (np.linalg.norm(motion, axis=1, keepdims=True) + 1e-8)


audio_t = torch.tensor(audio, dtype=torch.float32)
motion_t = torch.tensor(motion, dtype=torch.float32)

# ========= model =========
class AlignNet(nn.Module):
    def __init__(self, a_dim, m_dim):
        super().__init__()
        self.fc = nn.Linear(a_dim, m_dim)

    def forward(self, x):
        return self.fc(x)

model = AlignNet(audio.shape[1], motion.shape[1])

optimizer = torch.optim.Adam(model.parameters(), lr=0.0005)
loss_fn = nn.MSELoss()

# ========= train =========
print("training...")
for epoch in range(200):
    pred = model(audio_t)
    loss = loss_fn(pred, motion_t)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print("final loss:", loss.item())

# ========= retrieval =========
mapped = model(audio_t).detach().numpy()

top1 = 0
top5 = 0

for i in range(len(mapped)):
    sims = cosine_similarity(
        mapped[i].reshape(1, -1),
        motion
    )[0]

    ranking = np.argsort(sims)[::-1]

    if ranking[0] == i:
        top1 += 1

    if i in ranking[:5]:
        top5 += 1

top1_acc = top1 / len(mapped)
top5_acc = top5 / len(mapped)

print("\nRESULT")
print("Top-1 accuracy:", top1_acc)
print("Top-5 accuracy:", top5_acc)