import React from "react";

const CodeInput = ({ code, output }) => {
  return (
    <div className="w-full max-w-4xl bg-white rounded-lg shadow-lg p-6">
      {/* User Input */}
      <div className="bg-gray-100 rounded-md p-4 mb-4">
        <textarea
          className="w-full p-2 text-gray-800 font-mono bg-gray-100 border border-gray-300 rounded-md"
          placeholder="Write your code here" // Placeholder for user input
        />
      </div>

      {/* Dynamic Output */}
      <div>
        <p className="font-semibold text-gray-800 mb-2">Excepted Output</p>
        <div className="bg-gray-900 text-white rounded-md p-4">
          <pre>{output}</pre> {/* Output will be passed dynamically */}
        </div>
      </div>
    </div>
  );
};

export default CodeInput;
