import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import clockImage from '../assets/clock.png'; // Replace with your clock image path
import cupImage from '../assets/cup.png'; // Replace with your cup image path
import mapImage from '../assets/map.png'; // Replace with your map image path

const LandingPage = () => {
  const [code, setCode] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const handleResize = () => {
      const root = document.documentElement;
      const viewportHeight = window.innerHeight;

      if (viewportHeight < 800) {
        root.style.setProperty('--title-font-size', '3rem');
        root.style.setProperty('--section-spacing', '1rem');
        root.style.setProperty('--section-font-size', '0.9rem');
      } else {
        root.style.setProperty('--title-font-size', '4rem');
        root.style.setProperty('--section-spacing', '2rem');
        root.style.setProperty('--section-font-size', '1rem');
      }
    };

    handleResize();
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  const handleStart = (e) => {
    e.preventDefault();
    if (code.trim()) {
      console.log('Code Submitted:', code);
      navigate(`/challenge?code=${code}`);
    } else {
      alert('Please enter a valid code');
    }
  };

  return (
    <div className="min-h-screen w-full flex flex-col items-center bg-gray-100 p-4 font-sans gap-4">
      <nav className="fixed top-0 w-full flex justify-between items-center p-4 bg-white shadow-md z-10">
        <h1 className="font-bold text-gray-900 text-xl">Query Quest</h1>
        <div className="space-x-4">
          <button className="text-gray-700 hover:text-gray-900">Challenge</button>
          <button className="text-gray-700 hover:text-gray-900">Guide</button>
          <button className="bg-purple-600 text-white py-2 px-4 rounded hover:bg-purple-700">Get started</button>
        </div>
      </nav>
      
      <div className="flex-grow pt-16 w-full flex flex-col items-center ">
        <div className="bg-white p-6 md:p-10 rounded-md shadow-lg w-full max-w-5xl mt-6">
          
          <h2 className="text-3xl font-semibold text-center mb-8">Welcome!</h2>
          
          <p className="text-gray-600 mb-8 text-justify">
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry’s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
          </p>
          <br />

          <h2 className="text-3xl font-semibold text-center mb-8">Guide</h2>
          <div className="flex flex-col md:flex-row justify-between space-y-12 md:space-y-0 md:space-x-4">
            <div className="flex flex-col items-center">
              <img src={clockImage} alt="Clock" className="h-16 w-16 mb-4" />
              <h3 className="text-xl font-semibold mb-2">Timed Challenges</h3>
              <p className="text-center text-gray-600 max-w-xs">Solve a series of timed challenges and get flag</p>
            </div>

            <div className="flex flex-col items-center">
              <img src={cupImage} alt="Cup" className="h-16 w-16 mb-4" />
              <h3 className="text-xl font-semibold mb-2">Flag</h3>
              <p className="text-center text-gray-600 max-w-xs">Get a flag each time you lose to save your progress and submit it in Kaggle</p>
            </div>

            <div className="flex flex-col items-center">
              <img src={mapImage} alt="Map" className="h-16 w-16 mb-4" />
              <h3 className="text-xl font-semibold mb-2">Avoid cheating!</h3>
              <p className="text-center text-gray-600 max-w-xs">Do not share your flag with others! Each team has unique flags</p>
            </div>
          </div>
<br />
<h2 className="text-2xl font-semibold text-center mb-8">Login to get started </h2>
          <div className="mt-8 w-full">
            <form onSubmit={handleStart} className="flex justify-center">
              <input
                type="text"
                value={code}
                onChange={(e) => setCode(e.target.value)}
                placeholder="Enter your team code"
                className="w-48 md:w-64 p-2 border border-gray-300 rounded-l-md focus:outline-none focus:ring-2 focus:ring-purple-500"
              />
              <button
                type="submit"
                className="bg-purple-600 text-white py-2 px-4 rounded-r-md hover:bg-purple-700"
              >
                Login
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LandingPage;
