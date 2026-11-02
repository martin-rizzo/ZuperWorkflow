## 🦸 Zuper Workflow [BASIC]

This workflow simplifies image generation with Z-Image Turbo (ZIT), featuring a reduced set of parameters for easy setup. It shares the same internal functionality as the ADVANCED version but offers fewer options to avoid complex configurations. It leverages comfy_kitchen, subgraphs, and INT8-ConvRot quantization, alongside the visual features of Node 2.0, therefore, it is recommended to run the latest version of ComfyUI with these features enabled.

## Parameters

__seed__
* The initial number for random generation. Each unique seed produces a different image.
* Results in significantly more dramatic variations when __"turbo_creativity"__ is turned on.

__style__
* The visual style that defines the overall look of your final image.

__prompt__
* The text description of what you want to see, including subjects, actions, and settings.
* Avoid style keywords such as photo, comic, or blur, as the selected styles handle all visual effects automatically.

__turbo_creativity__
* Shakes up the generation process to produce unique, original compositions and avoid generic AI aesthetics.
* It is prone to generating hallucinations and duplicate elements, especially in high-contrast images.
* Disable this feature if you require highly precise and complex images.
* Enable this feature when exploring creative compositions with substantial variations between different seeds.
* Working with __turbo_creativity__ involves testing multiple seeds until you find the ideal one.
* Some minor defects and small hallucinations can be corrected by tweaking __"steps"__ and __"initial_bias"__.

__color__
* Adjusts the color saturation of the image.
* Generally, a value of 0.2 (positive) yields a colorful image.
* If the image color appears too intense and artificial, it is advisable to lower it to 0.0 or even -0.2 (negative).

__orientation__
* Sets the orientation of the final image, where vertical creates a portrait format and horizontal creates a landscape format.

__zimage_turbo_file__
* The checkpoint file used for the Z-Image Turbo diffusion model.

__qwen3_4b_file__
* The checkpoint file used as the text encoder, which must be based on the Qwen3-4b model.

__vae_file__
* The checkpoint file used for the variational autoencoder.
