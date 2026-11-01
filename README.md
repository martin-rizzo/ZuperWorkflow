<h1 align="center">Zuper Workflow</h1>
<p align="center">ComfyUI workflows for easily generating high-quality images with Z-Image Turbo.</p>
<!--
<p align="center">
  <img alt="screenshot" src="xtra/zuper-workflow-screenshot.jpg">
</p>
-->
<p align="center">
  <a href="https://github.com/comfy-org/comfyui" target="_blank">
    <img alt="Platform" src="https://img.shields.io/badge/platform-ComfyUI-0077B6">
  </a>
  <a href="https://huggingface.co/Tongyi-MAI/Z-Image-Turbo" target="_blank">
    <img alt="Model"    src="https://img.shields.io/badge/model-Z--Image%20Turbo-FF6B6B">
  </a>
  <img alt="License"  src="https://img.shields.io/github/license/martin-rizzo/ZuperWorkflow?color=11D">
  <img alt="Last"     src="https://img.shields.io/github/last-commit/martin-rizzo/ZuperWorkflow">
</p>

**Zuper Workflow** is a workflow designed for [ComfyUI](https://github.com/comfyanonymous/ComfyUI), leveraging the power of the **Z-Image Turbo** model. It enables generate spectacular images with minimal effort, offering a balance between simplicity and advanced customization.

---

## 💎 Features

- **Effortless Generation**: Generate high-quality images with a single click using pre-configured prompt styles and optimized settings.
- **Style Customization**: Apply distinct styles for each of the three diffusion stages intentando lograr imagenes mas originales.
- **Dual Workflow Versions**:
  - **BASE**: A simplified workflow for quick and easy image generation.
  - **ADVANCED**: A fully-featured workflow with detailed controls for power users.
- **Modular Design**: The workflows are built using a source modular structure, allowing for easy updates and rebuild.
- **Inline Documentation**: Clear and concise documentation within the workflow JSON to guide users through configuration options.

---

## 📂 Project Structure

```
├── README.md                 # This file
├── LICENSE                   # License file
├── ZuperWF_basic.json        # Final generated basic workflow
├── ZuperWF_advanced.json     # Final generated advanced workflow
├── zmake.py                  # Core workflow generation script
├── zmake.sh                  # Shell wrapper for zmake.py
└── src/
    ├── ZuperWF_basic.template.json     # Template for building the BASIC version of the workflow
    ├── ZuperWF_advanced.template.json  # Template for building the ADVANCED version of the workflow
    ├── STYLES.sty.txt                  # Unified styles file with segments for each diffusion stage
    ├── zmakefile.txt                   # Build configuration file
    ├── readme-basic.md                 # README content for the BASE workflow
    ├── readme-advanced.md              # README content for the ADVANCED workflow
    ├── about.md                        # About section for workflow internal documentation
    └── requirements.md                 # Requirements section for workflow internal documentation
```

---

## Getting Started

### Prerequisites

* __[ComfyUI](https://github.com/Comfy-Org/ComfyUI)__ v0.27 or higher, preferably the latest available version.
* __[Z-Image Power Nodes](https://github.com/martin-rizzo/ComfyUI-ZImagePowerNodes)__ v2.1.2 or higher
* __[ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF)__ (only if you intend to use GGUF checkpoints)


## Checkpoints utilizados por los workflows

**diffusion_models**

- __[z_image_turbo_int8_convrot_bf16emixed.safetensors](https://huggingface.co/martin-rizzo/Z-Image-Turbo-INT8-ConvRot-ComfyUI/resolve/main/z_image_turbo_int8_convrot_bf16emixed.safetensors)__ [6.17 GB]

**text_encoders**

- __[qwen3-4b_int8_convrot_fp16emixed.safetensors](https://huggingface.co/martin-rizzo/Qwen3-4B-INT8-ConvRot-ComfyUI/resolve/main/qwen3-4b_int8_convrot_fp16emixed.safetensors)__ [4.42 GB]

**vae**

- __[Z-Image_half_natural_vae.safetensors](https://huggingface.co/easygoing0114/Z-Image_clear_vae/resolve/main/Z-Image_half_natural_vae.safetensors)__ [335 MB]


---

## 🎨 Styles

The `./src/STYLES.sty.txt` file contains segmented styles for each diffusion stage.
Este archivo es la base con la que los workflows son luego generados de manera
automatica con el script zmake.py

Example segments:
- **Core Styles**: Define the foundational appearance of the image.
- **Layout Styles**: Control the composition and structure.
- **Final Styles**: Refine the overall aesthetic.


## License

This project is licensed under the Creative Commons Zero v1.0 Universal (CC0 1.0)  
See the [LICENSE](LICENSE) file for details.

---

<div align="center">
⭐ If you like what you see, give the repository a star. Your support inspires more explorations!
</div>
