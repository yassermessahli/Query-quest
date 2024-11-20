import React from "react";
import map from "../assets/bigmap.png"; // Import bigmap image

const LostPage = ({ score, flag, onRetry }) => {
  return (
    <div className="flex flex-col h-screen bg-gray-100">
      {/* Header */}
      <header className="bg-white shadow-md py-4 px-8 text-xl font-bold text-gray-800">
        Query Quest
      </header>

      {/* Main Content */}
      <div className="flex items-center justify-center flex-grow">
        {/* Card Container */}
        <div className="bg-white shadow-lg rounded-lg p-8 max-w-md w-full text-center">
          {/* Title */}
          <h1 className="text-2xl font-bold text-red-500 mb-4">You’ve Lost!</h1>
          {/* Dynamic Score */}
          <p className="text-lg font-medium mb-4">Score: {score}</p>
          {/* Big Map Image */}
          <div className="flex justify-center mb-6">
            <img
              src={map}
              alt="Big Map"
              className="h-32 w-32 md:h-40 md:w-40 object-contain rounded"
            />
          </div>
          {/* Flag */}
          <div className="bg-gray-800 text-white font-mono py-2 px-4 rounded mb-6">
            {flag}
          </div>
          <p className="text-gray-600 mb-6">
            Try again and save the flag to save your progress!
          </p>
          {/* Try Again Button */}
          <button
            onClick={onRetry}
            className="bg-purple-600 text-white py-2 px-6 rounded hover:bg-purple-700 focus:outline-none"
          >
            Try Again
          </button>
        </div>
      </div>
    </div>
  );
};

export default LostPage;
