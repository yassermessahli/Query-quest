import React from "react";
import { useNavigate } from "react-router-dom"; // Import useNavigate
import cupImage from "../assets/cup.png"; // Import cup image
import TimerIcon from "../assets/Timer.svg"; // Import Timer icon

const PreQuestion = () => {
  const navigate = useNavigate(); // Initialize navigate hook

  const handleStart = () => {
    navigate("/question"); // Navigate to the question page
  };

  return (
    <div className="h-screen w-screen flex flex-col items-center justify-start bg-gray-50">
      {/* Header */}
      <header className="w-full bg-white shadow-md py-4 px-8 text-xl font-bold text-gray-800">
        Query Quest
      </header>

      {/* Main Content */}
      <main className="flex-grow flex items-center justify-center px-4 w-full">
        <div className="bg-white p-8 md:p-12 rounded-lg shadow-lg flex flex-col items-center max-w-lg w-full">
          <h1 className="text-3xl md:text-4xl font-bold text-gray-800 mb-4 md:mb-6">
            Question 1
          </h1>
          <div className="flex items-center text-purple-600 text-lg md:text-xl font-semibold mb-6 md:mb-10">
            {/* Timer Section */}
            <img
              src={TimerIcon}
              alt="Timer"
              className="h-6 w-6 md:h-8 md:w-8 mr-2"
            />{" "}
            120s
          </div>
          {/* Cup Image */}
          <img
            src={cupImage}
            alt="Illustration"
            className="mb-6 md:mb-8 h-32 w-32 md:h-40 md:w-40"
          />
          {/* Start Button */}
          <button
            onClick={handleStart} // Call handleStart on click
            className="w-full md:w-1/2 bg-purple-600 text-white py-2 md:py-3 rounded-md hover:bg-purple-700 text-lg"
          >
            Start
          </button>
        </div>
      </main>
    </div>
  );
};

export default PreQuestion;
