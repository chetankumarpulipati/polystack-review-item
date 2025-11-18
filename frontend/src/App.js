import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const API_URL = 'http://localhost:8000/api/reviews';

function App() {
  const [reviews, setReviews] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [refreshing, setRefreshing] = useState(false);

  const fetchReviews = async () => {
    try {
      setRefreshing(true);
      const response = await axios.get(API_URL);
      setReviews(response.data);
      setError(null);
    } catch (err) {
      setError('Failed to fetch reviews. Make sure the backend is running on port 8000.');
      console.error('Error fetching reviews:', err);
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  };

  useEffect(() => {
    fetchReviews();
    // Auto-refresh every 10 seconds
    const interval = setInterval(fetchReviews, 10000);
    return () => clearInterval(interval);
  }, []);

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const formatPhoneNumber = (phone) => {
    // Remove 'whatsapp:' prefix if present
    return phone.replace('whatsapp:', '');
  };

  if (loading) {
    return (
      <div className="App">
        <div className="container">
          <div className="loading">
            <div className="spinner"></div>
            <p>Loading reviews...</p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="App">
      <div className="container">
        <header className="header">
          <div className="header-content">
            <div className="header-icon">
              <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M20 0C8.954 0 0 8.954 0 20c0 3.529.914 6.842 2.512 9.712L.074 38.488a1.25 1.25 0 001.438 1.438l8.776-2.438A19.876 19.876 0 0020 40c11.046 0 20-8.954 20-20S31.046 0 20 0z" fill="#25D366"/>
                <path d="M28.75 25.312c-.437 1.25-2.187 2.313-3.562 2.563-.938.187-2.125.312-6.188-1.313-5.188-2.062-8.5-7.375-8.75-7.687-.25-.313-2.063-2.75-2.063-5.25s1.313-3.75 1.75-4.25c.438-.5.938-.625 1.25-.625.313 0 .625 0 .875.063.313.062.75-.125 1.188.875.437 1 1.5 3.625 1.625 3.875.125.25.187.563.063.875-.125.313-.25.5-.5.813-.25.312-.5.687-.687.875-.25.25-.5.562-.25.937.25.438 1.125 1.875 2.437 3.063 1.688 1.562 3.063 2.062 3.5 2.312.438.25.688.188.938-.125.25-.312 1.063-1.25 1.375-1.687.313-.438.625-.375.937-.25.313.125 2.063.938 2.438 1.125.437.187.687.312.812.437.125.188.125 1.063-.312 2.313z" fill="#fff"/>
              </svg>
            </div>
            <div>
              <h1>WhatsApp Product Reviews</h1>
              <p className="subtitle">Real-time customer feedback via WhatsApp</p>
            </div>
          </div>
          <button 
            className={`refresh-btn ${refreshing ? 'refreshing' : ''}`}
            onClick={fetchReviews}
            disabled={refreshing}
          >
            <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
              <path d="M4 2v6h6M16 18v-6h-6" stroke="currentColor" strokeWidth="2" fill="none"/>
              <path d="M2.99 8A8 8 0 0116 4m-2 12a8 8 0 01-13.01-4" stroke="currentColor" strokeWidth="2" fill="none"/>
            </svg>
            Refresh
          </button>
        </header>

        {error && (
          <div className="error-banner">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
              <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clipRule="evenodd"/>
            </svg>
            {error}
          </div>
        )}

        {reviews.length === 0 ? (
          <div className="empty-state">
            <div className="empty-icon">📝</div>
            <h2>No Reviews Yet</h2>
            <p>Reviews submitted via WhatsApp will appear here.</p>
            <div className="instruction-box">
              <h3>How to submit a review:</h3>
              <ol>
                <li>Send a message to the WhatsApp number</li>
                <li>Follow the conversation prompts</li>
                <li>Your review will appear here automatically</li>
              </ol>
            </div>
          </div>
        ) : (
          <div className="reviews-section">
            <div className="reviews-header">
              <h2>Customer Reviews</h2>
              <span className="review-count">{reviews.length} {reviews.length === 1 ? 'Review' : 'Reviews'}</span>
            </div>
            
            <div className="reviews-grid">
              {reviews.map((review) => (
                <div key={review.id} className="review-card">
                  <div className="review-header">
                    <div className="reviewer-info">
                      <div className="avatar">
                        {review.user_name.charAt(0).toUpperCase()}
                      </div>
                      <div>
                        <h3 className="reviewer-name">{review.user_name}</h3>
                        <p className="contact-number">{formatPhoneNumber(review.contact_number)}</p>
                      </div>
                    </div>
                    <span className="review-date">{formatDate(review.created_at)}</span>
                  </div>
                  
                  <div className="product-badge">
                    <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor">
                      <path d="M3 1a1 1 0 000 2h1.22l.305 1.222a.997.997 0 00.01.042l1.358 5.43-.893.892C3.74 11.846 4.632 14 6.414 14H15a1 1 0 000-2H6.414l1-1H14a1 1 0 00.894-.553l3-6A1 1 0 0017 3H6.28l-.31-1.243A1 1 0 005 1H3zM16 16.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0zM6.5 18a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"/>
                    </svg>
                    {review.product_name}
                  </div>
                  
                  <div className="review-content">
                    <p>{review.product_review}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;

