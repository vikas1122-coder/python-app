# Car Images Directory

This directory contains images for the cars displayed on the website.

## Current Images:
- `2024-Toyota-Camry-rendering-front.jpg` - Used for Toyota Camry

## How to Add More Car Images:

### 1. Add Image Files:
- Save your car images in this directory (`static/images/`)
- Use descriptive filenames (e.g., `honda-accord-2023.jpg`, `bmw-x1-silver.jpg`)
- Supported formats: JPG, PNG, WEBP

### 2. Update Backend Data:
Edit the `cars_data` list in `app.py` and update the `image_url` field:

```python
Car(
    id=2,
    make="Honda",
    model="Accord",
    year=2023,
    price=32000,
    mileage=8000,
    color="White",
    fuel_type="Gasoline",
    transmission="Automatic",
    engine="1.5L Turbo 4-Cylinder",
    features=["Heated Seats", "Apple CarPlay", "Android Auto", "Lane Assist", "Blind Spot Monitor"],
    image_url="/static/images/honda-accord-2023.jpg",  # Update this path
    description="Nearly new Honda Accord with advanced safety features and modern technology."
)
```

### 3. Image Specifications:
- **Recommended size**: 800x600 pixels or similar aspect ratio
- **File size**: Keep under 500KB for fast loading
- **Format**: JPG for photos, PNG for images with transparency

### 4. Test the Images:
1. Start the backend server: `python app.py`
2. Visit: `http://localhost:8000/static/images/your-image-name.jpg`
3. The image should load in your browser

### 5. Update Frontend (if needed):
If you want to use different images in the frontend, update the CSS in `frontend/css/style.css`:

```css
.hero {
    background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), 
                url('../images/your-new-image.jpg');
}
```

## Example Image Names:
- `toyota-camry-silver.jpg`
- `honda-accord-white.jpg`
- `bmw-x1-gray.jpg`
- `mercedes-c-class-blue.jpg`
- `audi-a4-black.jpg`
- `tesla-model-3-red.jpg`

