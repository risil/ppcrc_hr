import { BrowserRouter, Route, Routes } from "react-router-dom";
import HomePage from "./components/Homepage/HomePage";
import Login from "./components/Login/Login";
import Navbar from "./components/Navbar/Navbar";
import Register from "./components/Register/Register";
import Jobs from "./components/Homepage/Jobs";
import Companies from "./components/Homepage/Companies";
import UploadResume from "./components/UploadResume";

import { ReactSession } from 'react-client-session'
import { useEffect, useState, createContext } from "react";

// import UserContext from './components/UserContext'

function App() {

  ReactSession.setStoreType('localStorage')
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const UserContext = createContext({})
  const [sessionData, setSessionData] = useState({})

  useEffect(() => {
    const storedSession = localStorage.getItem('session');

    if (storedSession) {
      const parsedData = JSON.parse(storedSession);
      setSessionData(parsedData)
      const currentTime = Date.now();
      const tokenExpiry = new Date(parsedData.token_expires_at).getTime();

      if (currentTime < tokenExpiry) {
        setIsLoggedIn(true)
      }
      else {
        localStorage.removeItem('session')
      }
    }
  }, [])

  return (
    <BrowserRouter>
      <div className="App">
        <UserContext.Provider value={sessionData}>
          <Navbar />
          {/* <HomePage /> */}
          <Routes>
            <Route path="/login" element={<Login />} />
            <Route path="/" element={<HomePage />} />
            <Route path="/register" element={<Register />} />
            <Route path="/jobs" element={<Jobs />} />
            <Route path="/jobs/*" element={<Jobs />} />

            <Route path="/companies" element={<Companies />} />
            <Route path="/uploadresume" element={<UploadResume />} />

            <Route path="/api/login" element={<Login />} />
            <Route path="/api/register" element={<Register />} />
          </Routes>
        </UserContext.Provider>
      </div>
    </BrowserRouter>
  );
}

export default App;
