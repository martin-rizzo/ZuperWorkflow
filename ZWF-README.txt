# Zuper Workflows
ComfyUI workflows for easily generating high-quality images with Z-Image Turbo.

## Description

Zuper Workflows are a group of workflows designed for ComfyUI, leveraging the
power of the Z-Image Turbo model. They enable you to generate spectacular
images with minimal effort, offering a balance between simplicity and advanced
customization.

## Parameters

__seed__: The initial number for random generation. Each unique seed produces
          a different image. Results in significantly more dramatic variations
          when "turbo_creativity" is turned on.

__style__: The visual style that defines the overall look of your final image.

__prompt__: The text description of what you want to see, including subjects,
            actions, and settings. Avoid style keywords such as photo, comic, or
            blur, as the selected styles handle all visual effects automatically.

__steps__: The number of iterations performed during the denoising process.
           The optimal setting is 8 steps. Increase this value only if you
           require better quality or need to fix minor hallucinations caused
           by `turbo_creativity`, keeping in mind that higher step counts
           result in longer render times.

__noise_shift__: Adjusts the starting noise to generate small variations in the
                 final image or even correct minor hallucinations. "0.0" is the
                 optimal setting and is generally best left unchanged, as its
                 effects can be unpredictable.

__turbo_creativity__: Shakes up the generation process to produce unique,
                      original compositions and avoid generic AI aesthetics.
                      It is prone to generating hallucinations and duplicate
                      elements, especially in high-contrast images. Disable this
                      feature if you require highly precise and complex images.
                      Enable this feature when exploring creative compositions
                      with substantial variations between different seeds.
                      Working with `turbo_creativity` involves testing multiple
                      seeds until you find the ideal one. Some minor defects
                      and small hallucinations can be corrected by tweaking
                      `steps` and `initial_bias`.

__contrast__: Controls the intensity of brightness transitions in the final
              image. Typically, a value of "0.2" (positive) works very well.

__color__: Adjusts the color saturation of the image. Generally, a value of
           "0.2" (positive) yields a colorful image. If the image color appears
           too intense and artificial, it is advisable to lower it to "0.0" or
           even "-0.2" (negative).

__hue__: Modifies the color tint, primarily used to calibrate skin tones.
         Typically, a value of "-0.2" (negative) works very well.

__detailed_sampling__: Applies a different sampling method in final steps for
                       finer details, although it may increase generation time.

__orientation__: Sets the orientation of the final image, vertical for portrait
                 format and horizontal for landscape.

__aspect_ratio__: Determines the proportional relationship between the width
                  and height of the final image.

__ck_attention__: Enables Comfy-Kitchen attention to accelerate generation.
                  Works best in newer ComfyUI versions and is recommended to
                  stay enabled.

__zimage_turbo_file__: The checkpoint used for the Z-Image Turbo diffusion model.

__qwen3_4b_file__: The checkpoint file used as the text encoder, which must be
                   based on the Qwen3-4b model.

__vae_file__: The checkpoint file used for the variational autoencoder.

-----------------------------------------------------------------------
Repository: https://github.com/martin-rizzo/ZuperWorkflows  
License: Creative Commons Zero v1.0 Universal (CC0 1.0)
