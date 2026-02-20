# 🎵 Multimodal Music–Motion Alignment

## Overview

This project explores **cross-modal representation learning** between music audio signals and human motion dynamics.

Using the AIST++ dance dataset, we investigate whether a model can learn to align:

- 🎧 Music audio features  
- 🕺 3D human motion representations  

into a shared embedding space.

The goal is to evaluate whether meaningful correspondences between music and dance can be learned through contrastive training.

---

## Motivation

Music and human movement are strongly correlated through rhythm, tempo, and structural dynamics. However, learning this relationship computationally is non-trivial.

This project aims to answer:

> Can a model learn meaningful cross-modal alignment between music and motion representations?

We approach this as a **multimodal retrieval problem**, inspired by contrastive learning frameworks such as CLIP.

---

## Dataset

We use the **AIST++ dataset**, which provides:

- 3D human skeleton sequences (motion)
- Corresponding dance music tracks (audio)

Total samples:

- 1408 paired audio–motion examples  
- Audio features extracted via MFCC  
- Motion represented as 3D keypoint embeddings  

---

## Method

### 1️⃣ Feature Extraction

**Audio representation**
- MFCC (Mel-frequency cepstral coefficients)
- Mean pooling over time

**Motion representation**
- 3D skeleton keypoints
- NaN handling via `np.nanmean`
- Mean pooling over time

---

### 2️⃣ Linear Baseline

We first trained a simple linear regression model:

Evaluation via cosine similarity and retrieval metrics showed performance close to random baseline, indicating that simple regression is insufficient for cross-modal alignment.

---

### 3️⃣ Contrastive Learning Framework

We implemented a CLIP-style contrastive training setup.

Two encoders are trained:

- Audio encoder (MLP)
- Motion encoder (MLP)

Both are mapped into a shared embedding space.

Training objective:

- Pull matching audio–motion pairs closer
- Push mismatched pairs apart

Loss function:

- Symmetric cross-entropy (InfoNCE)
- Temperature scaling

---

## Evaluation

We evaluate the model using **cross-modal retrieval**.

For each audio sample:

1. Compute cosine similarity with all motion samples  
2. Rank candidates  
3. Measure retrieval accuracy  

Metrics:

- Top-1 accuracy
- Top-5 accuracy

---

## Results

### Linear Baseline

- Top-1 ≈ 0.07% (random-level performance)

### Contrastive Model

- Top-1 ≈ 3.48%
- Top-5 ≈ 13.2%

Compared to random retrieval:

- Top-1 improved by ~50×  
- Top-5 improved by ~37×  

This demonstrates that the model learns meaningful cross-modal alignment signals.

---

## Key Insights

- Linear regression fails to capture multimodal relationships.
- Contrastive learning significantly improves retrieval performance.
- Even simple MFCC and skeleton features contain recoverable cross-modal information.
- Retrieval-based evaluation is more informative than regression loss alone.

---

## Future Work

Potential improvements include:

- Temporal modeling (RNN / Transformer)
- Beat-synchronous alignment
- Motion velocity features
- Larger embedding dimensions
- Hard negative mining
- Batch-based contrastive learning

---

## Repository Structure
```
music-motion-project/
│
├── build_dataset.py
├── contrastive_train.py
├── retrieval_test.py
├── audio_dataset.npy
├── motion_dataset.npy
└── README.md
```
---

## Research Contribution

This project demonstrates:

- End-to-end multimodal pipeline construction
- Dataset preprocessing and alignment
- Contrastive representation learning
- Cross-modal retrieval evaluation

It serves as a foundational exploration into multimodal AI systems for music–motion understanding.