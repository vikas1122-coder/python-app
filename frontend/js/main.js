// API Configuration
const API_BASE_URL = `${window.location.origin}/api`;

// DOM Elements
const navLinks = document.querySelectorAll('.nav-link');
const navToggle = document.querySelector('.nav-toggle');
const navMenu = document.querySelector('.nav-menu');
const featuredCarsContainer = document.getElementById('featuredCars');
const allCarsContainer = document.getElementById('allCars');
const searchResultsContainer = document.getElementById('searchResults');
const modal = document.getElementById('carModal');
const closeModal = document.querySelector('.close');
const makeSelect = document.getElementById('make');
const modelSelect = document.getElementById('model');
const searchBtn = document.getElementById('searchBtn');

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    initializeNavigation();
    loadFeaturedCars();
    loadAllCars();
    loadCarMakes();
    initializeSearch();
    initializeModal();
});

// Navigation Functions
function initializeNavigation() {
    // Mobile menu toggle
    navToggle.addEventListener('click', () => {
        navMenu.classList.toggle('active');
    });

    // Smooth scrolling for navigation links
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
            
            // Update active link
            navLinks.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
            
            // Close mobile menu
            navMenu.classList.remove('active');
        });
    });

    // Update active link on scroll
    window.addEventListener('scroll', updateActiveNavLink);
}

function updateActiveNavLink() {
    const sections = document.querySelectorAll('section[id]');
    const scrollPos = window.scrollY + 100;

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.offsetHeight;
        const sectionId = section.getAttribute('id');

        if (scrollPos >= sectionTop && scrollPos < sectionTop + sectionHeight) {
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${sectionId}`) {
                    link.classList.add('active');
                }
            });
        }
    });
}

// API Functions
async function fetchData(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error('Error fetching data:', error);
        return null;
    }
}

async function postData(url, data) {
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error('Error posting data:', error);
        return null;
    }
}

// Car Loading Functions
async function loadFeaturedCars() {
    const cars = await fetchData(`${API_BASE_URL}/featured`);
    if (cars) {
        renderCars(cars, featuredCarsContainer);
    } else {
        featuredCarsContainer.innerHTML = '<div class="loading"><p>Error loading featured cars</p></div>';
    }
}

async function loadAllCars() {
    const cars = await fetchData(`${API_BASE_URL}/cars`);
    if (cars) {
        renderCars(cars, allCarsContainer);
    } else {
        allCarsContainer.innerHTML = '<div class="loading"><p>Error loading cars</p></div>';
    }
}

async function loadCarMakes() {
    const data = await fetchData(`${API_BASE_URL}/makes`);
    if (data && data.makes) {
        makeSelect.innerHTML = '<option value="">Select Make</option>';
        data.makes.forEach(make => {
            const option = document.createElement('option');
            option.value = make;
            option.textContent = make;
            makeSelect.appendChild(option);
        });
    }
}

async function loadCarModels(make) {
    if (!make) {
        modelSelect.innerHTML = '<option value="">Select Model</option>';
        return;
    }
    
    const data = await fetchData(`${API_BASE_URL}/models/${encodeURIComponent(make)}`);
    if (data && data.models) {
        modelSelect.innerHTML = '<option value="">Select Model</option>';
        data.models.forEach(model => {
            const option = document.createElement('option');
            option.value = model;
            option.textContent = model;
            modelSelect.appendChild(option);
        });
    }
}

function normalizeImgUrl(u) {
    if (!u) return null;
    if (/^https?:\/\//i.test(u)) return u;                  // already absolute
    if (u.startsWith("/")) return `${window.location.origin}${u}`; // e.g. /static/images/...
    return `${window.location.origin}/static/images/${u}`;   // just a filename
  }
  

// Render Functions
function renderCars(cars, container) {
    if (!cars || cars.length === 0) {
        container.innerHTML = '<div class="loading"><p>No cars found</p></div>';
        return;
    }

    container.innerHTML = cars.map(car => `
        <div class="car-card" onclick="openCarDetail(${car.id})">
            <div class="car-image">
                <img src="${normalizeImgUrl(car.image_url)}" alt="${car.make} ${car.model}">    
            </div>
            <div class="car-info">
                <h3 class="car-title">${car.make} ${car.model}</h3>
                <p class="car-year">${car.year}</p>
                <div class="car-details">
                    <span><i class="fas fa-tachometer-alt"></i> ${car.mileage.toLocaleString()} mi</span>
                    <span><i class="fas fa-palette"></i> ${car.color}</span>
                    <span><i class="fas fa-gas-pump"></i> ${car.fuel_type}</span>
                </div>
                <div class="car-price">$${car.price.toLocaleString()}</div>
                <div class="car-features">
                    ${car.features.slice(0, 3).map(feature => `<span class="feature-tag">${feature}</span>`).join('')}
                    ${car.features.length > 3 ? `<span class="feature-tag">+${car.features.length - 3} more</span>` : ''}
                </div>
                <a href="#" class="view-details" onclick="event.stopPropagation(); openCarDetail(${car.id})">View Details</a>
            </div>
        </div>
    `).join('');
}

function renderSearchResults(cars) {
    if (!cars || cars.length === 0) {
        searchResultsContainer.innerHTML = `
            <div class="loading">
                <p>No cars found matching your criteria</p>
            </div>
        `;
        return;
    }

    searchResultsContainer.innerHTML = `
        <h3>Search Results (${cars.length} cars found)</h3>
        <div class="cars-grid">
            ${cars.map(car => `
                <div class="car-card" onclick="openCarDetail(${car.id})">
                    <div class="car-image">
                        <img src="${normalizeImgUrl(car.image_url)}" alt="${car.make} ${car.model}">
                    </div>
                    <div class="car-info">
                        <h3 class="car-title">${car.make} ${car.model}</h3>
                        <p class="car-year">${car.year}</p>
                        <div class="car-details">
                            <span><i class="fas fa-tachometer-alt"></i> ${car.mileage.toLocaleString()} mi</span>
                            <span><i class="fas fa-palette"></i> ${car.color}</span>
                            <span><i class="fas fa-gas-pump"></i> ${car.fuel_type}</span>
                        </div>
                        <div class="car-price">$${car.price.toLocaleString()}</div>
                        <div class="car-features">
                            ${car.features.slice(0, 3).map(feature => `<span class="feature-tag">${feature}</span>`).join('')}
                            ${car.features.length > 3 ? `<span class="feature-tag">+${car.features.length - 3} more</span>` : ''}
                        </div>
                        <a href="#" class="view-details" onclick="event.stopPropagation(); openCarDetail(${car.id})">View Details</a>
                    </div>
                </div>
            `).join('')}
        </div>
    `;
}

// Search Functions
function initializeSearch() {
    // Make selection change
    makeSelect.addEventListener('change', (e) => {
        loadCarModels(e.target.value);
    });

    // Search button click
    searchBtn.addEventListener('click', performSearch);
}

async function performSearch() {
    const searchData = {
        make: makeSelect.value || null,
        model: modelSelect.value || null,
        fuel_type: document.getElementById('fuelType').value || null,
        min_price: document.getElementById('minPrice').value ? parseInt(document.getElementById('minPrice').value) : null,
        max_price: document.getElementById('maxPrice').value ? parseInt(document.getElementById('maxPrice').value) : null,
        min_year: document.getElementById('year').value ? parseInt(document.getElementById('year').value) : null
    };

    // Remove null values
    Object.keys(searchData).forEach(key => {
        if (searchData[key] === null || searchData[key] === '') {
            delete searchData[key];
        }
    });

    const results = await postData(`${API_BASE_URL}/cars/search`, searchData);
    if (results) {
        renderSearchResults(results);
        // Scroll to search results
        document.getElementById('searchResults').scrollIntoView({
            behavior: 'smooth'
        });
    } else {
        searchResultsContainer.innerHTML = '<div class="loading"><p>Error performing search</p></div>';
    }
}

// Modal Functions
function initializeModal() {
    closeModal.addEventListener('click', () => {
        modal.style.display = 'none';
    });

    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.style.display = 'none';
        }
    });

    // Close modal on escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.style.display === 'block') {
            modal.style.display = 'none';
        }
    });
}

async function openCarDetail(carId) {
    const car = await fetchData(`${API_BASE_URL}/cars/${carId}`);
    if (car) {
        renderCarDetail(car);
        modal.style.display = 'block';
    }
}

function renderCarDetail(car) {
    const carDetailContent = document.getElementById('carDetailContent');
    carDetailContent.innerHTML = `
        <div style="padding: 40px;">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: start;">
                <div>
                    <div style="width: 100%; height: 300px; background: linear-gradient(45deg, #f0f0f0, #e0e0e0); border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                        <img src="${normalizeImgUrl(car.image_url)}" alt="${car.make} ${car.model}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 15px;">
                    </div>
                </div>
                <div>
                    <h2 style="font-size: 2rem; color: #2c3e50; margin-bottom: 10px;">${car.make} ${car.model}</h2>
                    <p style="font-size: 1.2rem; color: #7f8c8d; margin-bottom: 20px;">${car.year}</p>
                    <div style="font-size: 2.5rem; font-weight: 700; color: #e74c3c; margin-bottom: 30px;">$${car.price.toLocaleString()}</div>
                    
                    <div style="margin-bottom: 30px;">
                        <h3 style="margin-bottom: 15px; color: #2c3e50;">Specifications</h3>
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 20px;">
                            <div><strong>Mileage:</strong> ${car.mileage.toLocaleString()} mi</div>
                            <div><strong>Color:</strong> ${car.color}</div>
                            <div><strong>Fuel Type:</strong> ${car.fuel_type}</div>
                            <div><strong>Transmission:</strong> ${car.transmission}</div>
                            <div><strong>Engine:</strong> ${car.engine}</div>
                        </div>
                    </div>
                    
                    <div style="margin-bottom: 30px;">
                        <h3 style="margin-bottom: 15px; color: #2c3e50;">Features</h3>
                        <div style="display: flex; flex-wrap: wrap; gap: 10px;">
                            ${car.features.map(feature => `<span style="background: #ecf0f1; color: #2c3e50; padding: 8px 15px; border-radius: 20px; font-size: 0.9rem;">${feature}</span>`).join('')}
                        </div>
                    </div>
                    
                    <div style="margin-bottom: 30px;">
                        <h3 style="margin-bottom: 15px; color: #2c3e50;">Description</h3>
                        <p style="color: #666; line-height: 1.6;">${car.description}</p>
                    </div>
                    
                    <div style="display: flex; gap: 15px;">
                        <button style="background: #e74c3c; color: white; padding: 15px 30px; border: none; border-radius: 25px; font-size: 1rem; font-weight: 600; cursor: pointer; transition: background 0.3s;" onmouseover="this.style.background='#c0392b'" onmouseout="this.style.background='#e74c3c'">Contact Dealer</button>
                        <button style="background: #3498db; color: white; padding: 15px 30px; border: none; border-radius: 25px; font-size: 1rem; font-weight: 600; cursor: pointer; transition: background 0.3s;" onmouseover="this.style.background='#2980b9'" onmouseout="this.style.background='#3498db'">Schedule Test Drive</button>
                    </div>
                </div>
            </div>
        </div>
    `;
}

// Utility Functions
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(amount);
}

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Error Handling
window.addEventListener('error', function(e) {
    console.error('Global error:', e.error);
});

// Handle API connection errors
window.addEventListener('unhandledrejection', function(e) {
    console.error('Unhandled promise rejection:', e.reason);
});
