import React, { useState } from "react";
import CodeInput from "../component/CodeInput.jsx";
import Timer from "../component/Timer.jsx"; // Import the Timer component
import TimerIcon from "../assets/Timer.svg"

const Question = ({ questionNumber }) => {
  const [code, setCode] = useState("");
  const [output, setOutput] = useState("");
  const [isTimeUp, setIsTimeUp] = useState(false);

  const handleSubmit = () => {
    // Handle submission logic here
    console.log("Submitted code:", code);
  };

  const handleTimeUp = () => {
    setIsTimeUp(true);
    console.log("Time's up!");
    // Optional: Disable input or show a message
  };

  return (
    <div className="h-screen w-screen flex flex-col bg-gray-50">
      {/* Header */}
      <header className="w-full bg-white shadow-md py-4 px-8 flex justify-between items-center">
        <h1 className="text-xl font-bold text-gray-800">Query Quest</h1>
        <h2 className="text-xl font-bold text-gray-800">Question {questionNumber}</h2>
      </header>

      {/* Main Content */}
      <main className="flex-grow flex flex-col items-center px-6 pt-6">
        {/* Timer Section */}
        <div className="w-full flex justify-between items-center max-w-4xl mb-6">
          <p className="text-lg font-semibold text-gray-700">Fill in the blanks</p>
          <div className="flex items-center text-purple-600 text-lg font-semibold">
          <img
              src={TimerIcon}
              alt="Timer"
              className="h-6 w-6 md:h-8 md:w-8 mr-2"
            />{" "}
            <Timer initialTime={120} onTimeUp={handleTimeUp} /> {/* Timer */}
          </div>
        </div>

        {/* Question Section */}
        <div className="bg-white w-full max-w-4xl rounded-lg shadow-lg p-6">
          <p className="text-gray-700 text-base mb-4 leading-relaxed">
            The three columns in the <strong>stars</strong> DataFrame currently
            have very cumbersome names (
            <strong>Temperature (K)</strong>, <strong>Luminosity(L/Lo)</strong>,
            <strong>Radius(R/Ro)</strong>). Rename them using the provided list{" "}
            <strong>column_names</strong>.
          </p>
          <p className="font-semibold text-gray-800 mb-4">
            Task: Write the code to return the output
          </p>

          {/* Input Section */}
          <CodeInput
            code={code}
            setCode={setCode}
            output={output}
          />
        </div>

        {/* Submit Button */}
        <button
          onClick={handleSubmit}
          className="mt-6 bg-purple-600 text-white py-2 px-6 rounded-md hover:bg-purple-700"
          disabled={isTimeUp} // Disable button if time is up
        >
          Submit Answer
        </button>
        {isTimeUp && (
          <p className="text-red-600 mt-4">Time's up! Please submit your answer.</p>
        )}
      </main>
    </div>
  );
};

export default Question;
