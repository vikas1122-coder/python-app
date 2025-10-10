# CarDealer Pro - Car Website

A modern car dealership website built with FastAPI backend and vanilla HTML/CSS/JavaScript frontend.

## Features

- **Separate Frontend and Backend**: Clean separation of concerns
- **RESTful API**: FastAPI backend with comprehensive API endpoints
- **Responsive Design**: Modern, mobile-friendly frontend
- **Car Search & Filtering**: Advanced search functionality
- **Car Details Modal**: Detailed car information display
- **Real-time Data**: Dynamic content loading from API

## Project Structure

```
├── app.py                 # FastAPI backend application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── frontend/             # Frontend directory
    ├── index.html        # Main HTML file
    ├── css/
    │   └── style.css     # CSS styles
    ├── js/
    │   └── main.js       # JavaScript functionality
    └── images/           # Car images (placeholder)
```

## API Endpoints

### Cars
- `GET /api/cars` - Get all cars
- `GET /api/cars/{car_id}` - Get specific car details
- `GET /api/featured` - Get featured cars
- `GET /api/makes` - Get all car makes
- `GET /api/models/{make}` - Get models for specific make
- `POST /api/search` - Search cars with filters

### Car Search Parameters
- `make` - Car manufacturer
- `model` - Car model
- `min_price` - Minimum price
- `max_price` - Maximum price
- `min_year` - Minimum year
- `max_year` - Maximum year
- `fuel_type` - Fuel type (Gasoline, Hybrid, Electric)
- `transmission` - Transmission type

## Installation & Setup

### Backend Setup

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the FastAPI backend:**
   ```bash
   python app.py
   ```
   
   The API will be available at: `http://localhost:8000`
   
   API documentation will be available at: `http://localhost:8000/docs`

### Frontend Setup

1. **Open the frontend:**
   - Simply open `frontend/index.html` in your web browser
   - Or use a local server (recommended):
     ```bash
     # Using Python's built-in server
     cd frontend
     python -m http.server 8001
     ```
     Then visit: `http://localhost:8001`

2. **Update API URL (if needed):**
   - If your backend runs on a different port, update the `API_BASE_URL` in `frontend/js/main.js`

## Usage

1. **Start the backend server** (FastAPI)
2. **Open the frontend** in your browser
3. **Browse cars** on the homepage
4. **Search and filter** cars using the search section
5. **View detailed information** by clicking on any car

## Sample Data

The application comes with sample car data including:
- Toyota Camry (Hybrid)
- Honda Accord
- BMW 3 Series
- Mercedes-Benz C-Class
- Audi A4
- Tesla Model 3

## Features in Detail

### Frontend Features
- **Responsive Navigation**: Mobile-friendly navigation with hamburger menu
- **Hero Section**: Eye-catching landing area
- **Featured Cars**: Highlighted vehicle showcase
- **Advanced Search**: Filter cars by multiple criteria
- **Car Details Modal**: Detailed view with specifications
- **Contact Form**: Customer inquiry form
- **Modern UI**: Clean, professional design

### Backend Features
- **CORS Enabled**: Cross-origin requests supported
- **Pydantic Models**: Type-safe data validation
- **RESTful Design**: Standard HTTP methods and status codes
- **Error Handling**: Proper error responses
- **API Documentation**: Auto-generated Swagger docs

## Customization

### Adding New Cars
Edit the `cars_data` list in `app.py` to add new vehicles.

### Styling Changes
Modify `frontend/css/style.css` to customize the appearance.

### Adding New Features
- Backend: Add new endpoints in `app.py`
- Frontend: Add new functionality in `frontend/js/main.js`

## Production Deployment

For production deployment:

1. **Backend**: Use a production ASGI server like Gunicorn
2. **Frontend**: Serve static files through a web server (Nginx, Apache)
3. **Database**: Replace in-memory data with a proper database
4. **Security**: Update CORS settings and add authentication

## Technologies Used

- **Backend**: FastAPI, Python, Pydantic
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: CSS Grid, Flexbox, Custom CSS
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Inter)

## License

This project is open source and available under the MIT License.

