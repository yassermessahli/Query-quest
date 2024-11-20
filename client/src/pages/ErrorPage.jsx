import React from "react";

const ErrorPage = () => {
  return (
    <div className="h-screen w-screen flex flex-col justify-center items-center bg-gray-50">
      {/* Header */}
      <header className="w-full bg-white shadow-md py-4 px-8 flex items-center justify-start">
        <h1 className="text-xl font-bold text-gray-800">Query Quest</h1>
      </header>

      {/* Error Content */}
      <main className="flex-grow flex flex-col justify-center items-center">
        <div className="bg-white rounded-lg shadow-md p-8 text-center">
          <h2 className="text-2xl font-bold text-red-600 mb-4">An Error occurred</h2>
          <div className="flex justify-center mb-6">
            <img
              src="https://cdn-icons-png.flaticon.com/512/992/992700.png" 
              alt="Error Icon"
              className="w-24 h-24"
            />
          </div>
          <ul className="text-gray-700 text-lg text-left">
            <li>• reload the page</li>
            <li>• contact mentors of the competition</li>
          </ul>
        </div>
      </main>
    </div>
  );
};

export default ErrorPage;
