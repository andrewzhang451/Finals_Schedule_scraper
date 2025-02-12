// this is the main page where users will first see
import React from 'react';
import { Link } from'react-router-dom';

function LandingPage() {
    return (
        <div className = 'LandingPage'>
            <h1>Welcome to Schedule Finder</h1>
            <p>Save time by finding your class schedules in seconds!</p>
            <Link to='/scraper'>
                <button>Get Started</button>
            </Link>
        </div>
    )
}

export default LandingPage;

