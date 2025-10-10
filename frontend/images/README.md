# Car Images for Scrolling Background

To use actual car images in the scrolling background, save your car images in this directory with the following names:

## Required Image Files:
- `toyota-sedan.png` - Toyota sedan (gray/silver)
- `bmw-x1.png` - BMW X1 SUV (light gray/silver) 
- `sedan.png` - Generic sedan car
- `suv.png` - Generic SUV
- `sports-car.png` - Sports car

## Image Specifications:
- **Format**: PNG or JPG
- **Size**: Recommended 300x150px or similar aspect ratio
- **Background**: Transparent PNG preferred, or cars on transparent/solid backgrounds
- **Quality**: High resolution for crisp display

## How to Add Images:
1. Save your car images in this directory (`frontend/images/`)
2. Name them exactly as listed above
3. Refresh the webpage to see the scrolling car images

## Current Setup:
The CSS is configured to display these images as 150px wide x 80px high scrolling elements with:
- Smooth scrolling animations
- Drop shadows
- Bouncing effects
- Different speeds per lane

If you don't have these specific images, you can:
1. Use any car images and rename them to match the expected filenames
2. Modify the CSS class names in `style.css` to match your image filenames
3. Update the HTML class names in `index.html` accordingly

