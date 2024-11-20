import React from "react";
import cup from "../assets/cupbig.png"; // Replace with your trophy/cup icon path

const CongratulationsPage = ({ score, flag }) => {
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
          <h1 className="text-2xl font-bold text-gray-900 mb-4">
            Congratulations!
          </h1>
          {/* Dynamic Score */}
          <p className="text-lg font-medium text-gray-800 mb-4">
            Score: {score}
          </p>
          {/* Trophy/Cup Image */}
          <div className="flex justify-center mb-6">
            <img
              src={cup}
              alt="Trophy Icon"
              className="h-32 w-32 md:h-40 md:w-40 object-contain"
            />
          </div>
          {/* Flag */}
          <div className="bg-gray-800 text-white font-mono py-2 px-4 rounded mb-6">
            {flag}
          </div>
          {/* Save Flag Text */}
          <p className="text-gray-600 mb-6">
            Save the flag to save your progress!
          </p>
        </div>
      </div>
    </div>
  );
};

export default CongratulationsPage;
