from PIL import Image, ImageEnhance, ImageFilter

# Load image
img_path = 'C:\Users\adity\OneDrive\Desktop\VS code\Jupyter\WhatsApp Image 2026-04-02 at 11.56.16 AM.jpeg'
img = Image.open(img_path)

# Upscale (2x)
img_upscaled = img.resize((img.width*2, img.height*2), Image.LANCZOS)

# Enhance sharpness and contrast
enhancer_sharp = ImageEnhance.Sharpness(img_upscaled)
img_sharp = enhancer_sharp.enhance(2.0)

enhancer_contrast = ImageEnhance.Contrast(img_sharp)
img_final = enhancer_contrast.enhance(1.3)

# Slight denoise / smooth
img_final = img_final.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))

# Save enhanced image
output_path = '/mnt/data/enhanced_diagram.png'
img_final.save(output_path)

output_path
