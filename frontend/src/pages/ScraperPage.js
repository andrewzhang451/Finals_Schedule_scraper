import React, { useState } from 'react';
import axios from 'axios';

function ScraperPage() {
  const [schedule, setSchedule] = useState(null);
  const [loading, setLoading] = useState(false);

  const fetchSchedule = async () => {
    setLoading(true);
    try {
      const response = await axios.get('http://localhost:5000/get-exam-schedule');
      setSchedule(response.data.schedule);
    } catch (error) {
      console.error("Error fetching schedule", error);
    }
    setLoading(false);
  };

  return (
    <div className="scraper-page">
      <h2>Find Your Final Exam Schedule</h2>
      <button onClick={fetchSchedule}>Fetch Schedule</button>

      {loading && <p>Loading...</p>}

      {schedule && (
        <div>
          <h3>Schedule:</h3>
          <pre>{schedule.join("\n\n")}</pre>
        </div>
      )}
    </div>
  );
}

export default ScraperPage;