import qrcode
from PIL import Image, ImageDraw

# 🔗 Inserisci qui il link
data = "https://rebeccamirco.github.io/rebeccamirco/"

# Crea QR senza bordo bianco
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=0  # 👈 niente bordo bianco
)

qr.add_data(data)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# --- CREAZIONE CORNICE SOTTILE ---
cornice_spessore = 10  # 👈 cornice più sottile
colore_cornice = (180, 150, 100)  # colore beige elegante (RGB)

larghezza, altezza = qr_img.size

# Nuova immagine più grande per la cornice
img_con_cornice = Image.new(
    "RGB",
    (larghezza + cornice_spessore*2, altezza + cornice_spessore*2),
    colore_cornice
)

# Incolla QR al centro
img_con_cornice.paste(qr_img, (cornice_spessore, cornice_spessore))

# Salva file finale
img_con_cornice.save("qr_code.png")

print("QR elegante con cornice sottile generato: qr_matrimonio_cornice_sottile.png")