# ⛑️ HelmNet: Real-Time Safety Helmet Detection

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

**HelmNet** is a production-grade computer vision system for detecting safety helmet compliance on construction sites using YOLOv8.

## 🎯 Problem Statement

Construction site accidents cost the industry $13B+ annually, with 15% of fatalities from head injuries. HelmNet provides:

- **Real-time helmet detection** with 87% mAP accuracy
- **Sub-100ms inference latency** for live monitoring
- **Worker compliance tracking** (helmet/no-helmet classification)
- **Production-ready API** with monitoring

## ⚡ Quick Start

### Installation

```bash
git clone https://github.com/PhanasN/helmnet.git
cd helmnet
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Basic Usage

```python
from src.inference.detector import HelmetDetector

detector = HelmetDetector(model_path="models/helmnet_v1.pt")
results = detector.detect("construction_site.jpg")
```

### API Server

```bash
uvicorn src.api.app:app --host 0.0.0.0 --port 8000
```

## 📊 Performance Metrics

| Metric | Value |
|--------|-------|
| **mAP@0.5** | 0.87 |
| **Inference (GPU)** | 22ms |
| **Precision** | 0.89 |
| **Recall** | 0.84 |

## 🏗️ Architecture

```
Input → Preprocessing → YOLOv8 Model → Classification → API Response
```

## 💼 Business Value

- **Average OSHA fine**: $7,000 - $70,000 per violation
- **ROI**: Prevent 1 violation = system pays for itself

## 📁 Project Structure

```
helmnet/
├── src/          # Source code
├── models/       # Model weights
├── data/         # Sample images
├── docs/         # Documentation
└── tests/        # Unit tests
```

## 🚀 Roadmap

- [ ] Multi-person tracking
- [ ] Safety vest detection
- [ ] Mobile app
- [ ] Real-time alerts

## 📄 License

MIT License

## 👤 Author

**Phanas N**
- GitHub: [@PhanasN](https://github.com/PhanasN)

## 🙏 Acknowledgments

- YOLOv8: Ultralytics
- Built with AWS Machine Learning expertise

---

⭐ **Star this repo to improve construction site safety!**
