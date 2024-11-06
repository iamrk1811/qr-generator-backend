import qrcode
from PIL import Image
from fastapi import HTTPException, APIRouter
from io import BytesIO
import base64
from app.models import SpaceQRRequest
import os

LOGO_PATH = os.getenv("QR_LOGO_PATH")
router = APIRouter()


def create_qr_with_logo(url, logo_path):
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create the QR code image
    qr_image = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # Load the logo
    logo = Image.open(logo_path).convert("RGBA")

    # Calculate the size for the logo
    logo_size = int(qr_image.size[0] / 4)
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

    # Calculate logo position
    logo_position = (
        (qr_image.size[0] - logo.size[0]) // 2,
        (qr_image.size[1] - logo.size[1]) // 2,
    )

    # Paste the logo onto the QR code with a mask for transparency handling
    qr_image.paste(logo, logo_position, mask=logo)

    # Save the QR code with logo to an in-memory file
    img_io = BytesIO()
    qr_image.save(img_io, "PNG")
    img_io.seek(0)

    return img_io


@router.post("/generate-space")
async def generate_space_qr(request: SpaceQRRequest):
    try:
        url = request.url + "?extra=" + request.extra
        # Generate the QR code with the given URL and logo in memory
        qr_image = create_qr_with_logo(url, LOGO_PATH)

        # Convert the QR code image to a base64 string without saving
        base64_img = base64.b64encode(qr_image.getvalue()).decode("utf-8")

        return {"qr_base64": base64_img}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
