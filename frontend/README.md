# WhatsApp Product Review Collector - Frontend

This is the React frontend for the WhatsApp Product Review Collector application. It displays product reviews submitted via WhatsApp in a clean, modern interface.

## Tech Stack

- **React** - UI library
- **Axios** - HTTP client for API calls
- **CSS3** - Styling with modern gradients and animations

## Prerequisites

- **Node.js 14+** and npm installed

## Setup Instructions

### 1. Install Dependencies

Navigate to the frontend folder and install dependencies:

```bash
cd frontend
npm install
```

### 2. Configure API URL

The frontend is configured to connect to the backend at `http://localhost:8000`. If your backend runs on a different port, edit `src/App.js`:

```javascript
const API_URL = 'http://localhost:YOUR_PORT/api/reviews';
```

### 3. Run the Development Server

```bash
npm start
```

The app will open in your browser at `http://localhost:3000`

## Features

- **Real-time Updates**: Automatically refreshes reviews every 10 seconds
- **Manual Refresh**: Click the refresh button to fetch latest reviews
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Modern UI**: Clean interface with gradient colors and smooth animations
- **Empty State**: Helpful instructions when no reviews exist
- **Error Handling**: Shows friendly error messages if backend is unavailable

## Build for Production

To create a production build:

```bash
npm run build
```

This creates an optimized build in the `build/` folder ready for deployment.

## Project Structure

```
frontend/
├── public/
│   └── index.html          # HTML template
├── src/
│   ├── App.js              # Main React component
│   ├── App.css             # Styling
│   ├── index.js            # Entry point
│   └── index.css           # Global styles
├── package.json            # Dependencies and scripts
└── README.md               # This file
```

## Customization

### Change Colors

Edit `src/App.css` and `src/index.css` to customize the color scheme. Current theme uses purple gradients (#667eea to #764ba2).

### Adjust Auto-Refresh Interval

In `src/App.js`, change the interval (currently 10000ms = 10 seconds):

```javascript
const interval = setInterval(fetchReviews, 10000); // Change to your preference
```

## Troubleshooting

### Backend Connection Error

If you see "Failed to fetch reviews" error:
1. Ensure backend is running on port 8000
2. Check that CORS is enabled in the backend
3. Verify API_URL in App.js

### Build Errors

Clear node_modules and reinstall:
```bash
rm -rf node_modules package-lock.json
npm install
```

## Deployment

You can deploy the frontend to:
- **Vercel**: `vercel deploy`
- **Netlify**: Drag and drop the `build/` folder
- **AWS S3**: Upload build folder to S3 bucket
- **GitHub Pages**: Use `gh-pages` package

Remember to update the API_URL to your production backend URL before building for production.

