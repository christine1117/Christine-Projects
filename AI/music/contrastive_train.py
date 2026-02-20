import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

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

# ========= encoder networks =========
class AudioEncoder(nn.Module):
    def __init__(self, input_dim, embed_dim=128):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, embed_dim)
        )

    def forward(self, x):
        return F.normalize(self.net(x), dim=1)


class MotionEncoder(nn.Module):
    def __init__(self, input_dim, embed_dim=128):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, embed_dim)
        )

    def forward(self, x):
        return F.normalize(self.net(x), dim=1)


audio_encoder = AudioEncoder(audio.shape[1])
motion_encoder = MotionEncoder(motion.shape[1])

optimizer = torch.optim.Adam(
    list(audio_encoder.parameters()) + 
    list(motion_encoder.parameters()), 
    lr=0.001
)

temperature = 0.07

# ========= contrastive training =========
print("training contrastive model...")

for epoch in range(300):
    audio_embed = audio_encoder(audio_t)
    motion_embed = motion_encoder(motion_t)

    logits = torch.matmul(audio_embed, motion_embed.T) / temperature

    labels = torch.arange(len(audio_embed))

    loss_a2m = F.cross_entropy(logits, labels)
    loss_m2a = F.cross_entropy(logits.T, labels)

    loss = (loss_a2m + loss_m2a) / 2

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 50 == 0:
        print(f"epoch {epoch}, loss {loss.item():.4f}")

print("final loss:", loss.item())

# ========= retrieval =========
audio_embed = audio_encoder(audio_t)
motion_embed = motion_encoder(motion_t)

similarity = torch.matmul(audio_embed, motion_embed.T)
similarity = similarity.detach().numpy()

top1 = 0
top5 = 0

for i in range(len(similarity)):
    ranking = np.argsort(similarity[i])[::-1]

    if ranking[0] == i:
        top1 += 1

    if i in ranking[:5]:
        top5 += 1

top1_acc = top1 / len(similarity)
top5_acc = top5 / len(similarity)

print("\nRESULT")
print("Top-1 accuracy:", top1_acc)
print("Top-5 accuracy:", top5_acc)