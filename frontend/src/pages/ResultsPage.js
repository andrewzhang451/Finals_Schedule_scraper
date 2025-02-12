import React from 'react';

function ResultsPage({ schedule }) {
  return (
    <div className="results-page">
      <h2>Exam Schedule Results</h2>
      <pre>{schedule.join("\n\n")}</pre>
    </div>
  );
}

export default ResultsPage;