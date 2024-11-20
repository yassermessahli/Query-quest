import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import LandingPage from './pages/LandingPage';
import PreQuestion from "./pages/Prequestion.jsx";
import Question from './pages/Question';
import LostPage from './pages/LostPage';
import Congrat from './pages/Congrat';
import ErrorPage from './pages/ErrorPage';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/prequestion" element={<PreQuestion />} /> {/* Ensure the path and component name are accurate */}
      <Route path="/question" element={<Question />} /> {/* Ensure the path is all lowercase */}
      <Route path="/LostPage" element={< LostPage/>} /> {/* Ensure the path is all lowercase */}
      <Route path="/Congrat" element={< Congrat/>} /> {/* Ensure the path is all lowercase */}
      <Route path="/ErrorPage" element={< ErrorPage/>} /> {/* Ensure the path is all lowercase */}
    </Routes>
  </BrowserRouter>
);
