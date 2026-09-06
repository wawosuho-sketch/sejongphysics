from PIL import Image
import os

images = {
    r"C:\Users\wawos\.gemini\antigravity-ide\brain\de107fec-117c-4089-beb1-afeb59115e49\vector_decomposition_diagram_1788670982356.png": r"r:\textbook-svelte\public\images\slides\mech_01\custom_vector_decomp.webp",
    r"C:\Users\wawos\.gemini\antigravity-ide\brain\de107fec-117c-4089-beb1-afeb59115e49\incline_forces_diagram_1788670997108.png": r"r:\textbook-svelte\public\images\slides\mech_01\custom_incline_forces.webp",
    r"C:\Users\wawos\.gemini\antigravity-ide\brain\de107fec-117c-4089-beb1-afeb59115e49\projectile_motion_diagram_1788671009542.png": r"r:\textbook-svelte\public\images\slides\mech_01\custom_projectile_motion.webp",
    r"C:\Users\wawos\.gemini\antigravity-ide\brain\de107fec-117c-4089-beb1-afeb59115e49\pendulum_oscillation_diagram_1788671022998.png": r"r:\textbook-svelte\public\images\slides\mech_01\custom_pendulum_oscillation.webp",
}

for src, dst in images.items():
    if os.path.exists(src):
        img = Image.open(src)
        img.save(dst, "WEBP", quality=85)
        print(f"Saved: {dst}")
    else:
        print(f"File not found: {src}")

print("Done converting custom diagrams!")
