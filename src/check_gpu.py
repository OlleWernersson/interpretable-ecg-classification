import torch
import sys

print(f"Python version: {sys.version}")
print(f"PyTorch version: {torch.__version__}")

if torch.cuda.is_available():
    print(f"✅ SUCCESS: CUDA is available!")
    print(f"   Device: {torch.cuda.get_device_name(0)}")
else:
    print(f"⚠️  WARNING: CPU only mode (This is expected on your laptop if you don't have an NVIDIA GPU)")