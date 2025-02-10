# ⚡ Model Quantisation for Efficient Inference

## 🔍 Overview

Quantisation is a technique used to **reduce the memory footprint** and **speed up inference** in deep learning models by lowering the precision of numerical computations. This allows models to run efficiently on hardware with limited computational power, such as **mobile devices and edge computing platforms**.

## 🔬 How Quantisation Works

- **PyTorch Dynamic Quantisation** is used to convert model weights from **32-bit floating point (FP32) to 8-bit integers (INT8)**.
- This reduces **memory usage by 75%**, making the model significantly smaller.
- Despite this compression, the **model retains its full accuracy of 97.24%**, meaning there is no performance loss due to quantisation.

## 📊 Quantisation Performance

| Model Version | Precision | Accuracy |
|--------------|------------|------------|
| Baseline (No Quantisation) | FP32 | 97.24% |
| Quantised Model | INT8 | 97.24% |

- The quantised model maintains the **exact same accuracy** as the full-precision model.
- The memory footprint is **reduced by 75%**, making deployment much more efficient.

## 🏆 Key Takeaways

✅ PyTorch **dynamic quantisation** reduces model size while preserving accuracy.  
✅ **8-bit integer operations** are significantly faster than 32-bit floating point operations.  
✅ The quantised model maintains **97.24% accuracy**, making it ideal for real-world applications.  

## 🛠 Running the Code

To apply quantisation to your model, run:
```bash
python quantisation.py
```

🚀 **Quantisation is a simple yet effective way to improve model efficiency for real-world deployment!**