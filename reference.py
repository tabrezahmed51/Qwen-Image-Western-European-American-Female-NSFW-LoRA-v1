"""Qwen Image 2512 + Western European American Female NSFW LoRA v1."""

import math

import torch
from diffusers import DiffusionPipeline, FlowMatchEulerDiscreteScheduler


BASE_MODEL_ID = "Qwen/Qwen-Image-2512"
LIGHTNING_MODEL_ID = "lightx2v/Qwen-Image-2512-Lightning"
LIGHTNING_WEIGHT_NAME = "Qwen-Image-2512-Lightning-4steps-V1.0-bf16.safetensors"
LORA_MODEL_ID = "perpetual3x/Qwen-Image-Western-European-American-Female-NSFW-LoRA-v1"
LORA_WEIGHT_NAME = "Western-European-American-Female.safetensors"

DEVICE = "cuda"
DTYPE = torch.bfloat16
LORA_SCALE = 1.0


scheduler_config = {
    "base_image_seq_len": 256,
    "base_shift": math.log(3),
    "invert_sigmas": False,
    "max_image_seq_len": 8192,
    "max_shift": math.log(3),
    "num_train_timesteps": 1000,
    "shift": 1.0,
    "shift_terminal": None,
    "stochastic_sampling": False,
    "time_shift_type": "exponential",
    "use_beta_sigmas": False,
    "use_dynamic_shifting": True,
    "use_exponential_sigmas": False,
    "use_karras_sigmas": False,
}

scheduler = FlowMatchEulerDiscreteScheduler.from_config(scheduler_config)
pipe = DiffusionPipeline.from_pretrained(
    BASE_MODEL_ID,
    scheduler=scheduler,
    torch_dtype=DTYPE,
).to(DEVICE)

pipe.load_lora_weights(
    LIGHTNING_MODEL_ID,
    weight_name=LIGHTNING_WEIGHT_NAME,
    adapter_name="lightning",
)
pipe.fuse_lora(adapter_names=["lightning"], lora_scale=1.0)
pipe.unload_lora_weights()

pipe.load_lora_weights(
    LORA_MODEL_ID,
    weight_name=LORA_WEIGHT_NAME,
    adapter_name="western_female_v1",
)
pipe.set_adapters(["western_female_v1"], adapter_weights=[LORA_SCALE])

# Natural language only. No trigger word is required.
prompt = (
    "A realistic environmental portrait of a clearly adult Western European "
    "American woman, natural unretouched appearance, mature presence, "
    "believable body variation, Atlantic coastal landscape, fine-art photography"
)
negative_prompt = (
    "child, minor, underage, youthful-looking, low quality, blurry, "
    "distorted anatomy, malformed hands, extra limbs, plastic skin, "
    "watermark, logo, text"
)

generator = torch.Generator(device=DEVICE).manual_seed(42)
image = pipe(
    prompt=prompt,
    negative_prompt=negative_prompt,
    width=928,
    height=1328,
    num_inference_steps=8,
    true_cfg_scale=1.0,
    generator=generator,
).images[0]
image.save("western_european_american_female_v1.png")
